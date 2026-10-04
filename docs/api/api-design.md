# BookBloom API Design

**Status:** Proposed contract; decisions below remain open.  
**Contract:** [OpenAPI 3.0.3](openapi.yaml)  
**Source of truth:** `docs/plan/online-bookstore-requirements.md` and `docs/database/database-architecture.md`.  
**Base URL assumption:** `/api/v1`; deployed host and token implementation are not specified.

## Architecture and DRF Conventions

Use domain-owned Django models as specified in the database document: `User`, `Address`, `Book`, `Author`, `Category`, `PhysicalVariant`, `Cart`, `CartItem`, `Order`, `OrderItem`, `Shipment`, and `Payment`. Keep serializers separated by intent: request serializers validate input, response serializers expose safe read models, and admin serializers require staff permissions. Do not expose password hashes, provider credentials, PAN, CVV, or raw provider events.

Use `APIView` or narrowly scoped viewsets for domain actions. Customer resources must be scoped to `request.user`; use object-level ownership checks for addresses, carts, and orders. Admin endpoints require authenticated Django staff/group permissions, including reads; writes are never available to customers. `User.is_staff` is server-managed and must never be customer-editable or exposed as an account update field. The current application user schema does not define `is_active` or `is_superuser`; use authentication lifecycle policy and Django groups/permissions without adding those user fields. Use explicit pagination (`page`, `pageSize`, maximum 100), allowlisted ordering/filter parameters, and a shared validation/error envelope. Rate-limit registration, login, and payment initiation. Audit staff catalog changes, shipment transitions, and access to order/contact data.

Persist creation/update timestamps only on models where they support history, editing, or operations; do not add them to every model by default. In this contract, `Address` exposes `createdAt` and `updatedAt`, `Cart` exposes `updatedAt`, `Order` exposes `createdAt`, and payment-attempt summaries expose `createdAt`. Order business-event fields `placedAt`/`confirmedAt` and Shipment business-event fields `shippedAt`/`deliveredAt` are also exposed. Generic model timestamps on `Book`, `PhysicalVariant`, and `Shipment`, plus `updatedAt` on `Payment`, are not exposed in their API response schemas. `CartItem`, `OrderItem`, `Author`, and `Category` have no generic creation/update timestamps in the current schema.

All monetary API values are two-decimal INR decimal **strings**, never JSON floats. `PhysicalVariant.price` is the current catalog price; checkout recalculates it server-side and persists immutable `OrderItem.unit_price`/`line_total` and `Order` totals. `Order.shippingAmount` is always `"0.00"`. The India tax amount is not determined by this contract. Catalog `Book.rating` is independent catalog data, not customer reviews; no rating write source is specified.

## Workflows and State

- **Identity:** `POST /auth/register` validates required name, email, phone, matching passwords, and true Terms acceptance. It discards `passwordConfirmation` and sets `terms_accepted_at` server-side. `User.is_staff` is server-managed and returned read-only in the profile; the current application schema does not define `is_active` or `is_superuser`. `POST /auth/login` returns a bearer token; `POST /auth/logout` revokes it; `GET /me` returns only the authenticated account. Registration/login are public; account endpoints require authentication.
- **Catalog:** Public `GET /books` and `GET /books/{bookId}` expose published physical books and variants. Each book has exactly one author for the current scope. Search spans title, author, and category; filters include category, inclusive INR price bounds, physical format, and 1–5 rating; ordering is allowlisted and paginated. Unavailable/out-of-stock variants cannot be added to cart. Rating data source and fractional rating bucket boundaries remain open.
- **Cart and addresses:** Authenticated customers use `GET /cart`, `POST /cart/items`, `PATCH /cart/items/{itemId}`, and `DELETE /cart/items/{itemId}` for their own cart. `GET/POST /addresses` and `GET/PATCH/DELETE /addresses/{addressId}` manage only their own saved addresses. Address country must be `IN`; `postalCode` must match `^[1-9][0-9]{5}$`. No alternate/gift recipient is supported: checkout snapshots the registered user's name into `Shipment.recipient_name` along with the selected address.
- **Order placement and payment:** `POST /checkout` requires a non-empty cart and idempotency key. Re-read current prices and lock/check stock transactionally; reject insufficient stock without a partial order. Create `Order` as `PENDING_PAYMENT`, immutable `OrderItem` snapshots, required `Shipment` address snapshot, and stock reservation/decrement atomically. `POST /orders/{orderId}/payment-attempts` initiates a separate attempt using `CARD` with `AMEX`, `VISA`, or `MASTERCARD`, or `PAYPAL`. Provider-hosted/tokenized payment is required; no card/payment secrets are accepted. `POST /payments/webhooks/{provider}` is provider-to-server only and must verify signatures, amount, currency, reference, and event deduplication. Browser return/redirect is not payment confirmation.
- **Confirmation and fulfillment:** A verified authoritative payment success may transition `Order.status` from `PENDING_PAYMENT` to `CONFIRMED`; a failed attempt leaves the order pending. Only after that transaction commits may the customer see the completion receipt (`GET /orders/{orderId}/confirmation`) and may an email be dispatched to the registered `User.email`. Dispatch is post-commit, retried on transient failure, and idempotent per confirmation event; email failure does not undo confirmation. `Shipment.status` is independent of `Order.status`. Staff change fulfillment through `PATCH /admin/orders/{orderId}/fulfillment`; it must not change payment or order confirmation state. Exact shipment transition policy is open.
- **History and operations:** `GET /orders` and `GET /orders/{orderId}` return only the customer's orders. Staff use `GET /admin/orders`, `GET /admin/orders/{orderId}`, and the fulfillment operation. Staff manage catalog records through `POST /admin/books`, `PATCH /admin/books/{bookId}`, and `POST /admin/books/{bookId}/archive`. Each enabled paperback/hardcover variant requires an explicit nonnegative `stockQuantity` on creation; archived records remain in historical order snapshots.

## Endpoint and Entity Traceability

| Requirement / screen interaction | API operations | Principal entities and rules |
| --- | --- | --- |
| Registration, login, sign out, account view | `POST /auth/register`, `POST /auth/login`, `POST /auth/logout`, `GET /me` | `User`; password confirmation is request-only; Terms acceptance timestamp is server-set. |
| Catalog/search results, category/price/format/rating filters, rating sort, detail | `GET /books`, `GET /books/{bookId}` | `Book` (each book has exactly one `Author`), `Category`, `BookCategory`, `PhysicalVariant`; rating is independent data, with source and fractional buckets unresolved. |
| Shopping cart controls | `GET /cart`, `POST /cart/items`, `PATCH /cart/items/{itemId}`, `DELETE /cart/items/{itemId}` | `Cart`, `CartItem`, `PhysicalVariant`; server-owned price and stock checks. |
| Saved delivery addresses and checkout address | `/addresses` collection and item operations; `POST /checkout` | `Address`; owner-only access, India-only country and PIN validation; checkout snapshots address to `Shipment`. |
| Address/payment and place order screens | `POST /checkout`, `POST /orders/{orderId}/payment-attempts`, `POST /payments/webhooks/{provider}` | `Order`, `OrderItem`, `Shipment`, `Payment`; INR strings, shipping `0.00`, no oversell, provider confirmation boundary. |
| Order-completed screen/email and customer order history | `GET /orders/{orderId}/confirmation`, `GET /orders`, `GET /orders/{orderId}` | `Order.status=CONFIRMED` only after verified success; email to registered `User.email` after commit; shipment remains independent. |
| Admin book management and archive | `GET /admin/books`, `GET /admin/books/{bookId}`, `POST /admin/books`, `PATCH /admin/books/{bookId}`, `POST /admin/books/{bookId}/archive` | `Book`, `PhysicalVariant`, `Author`, `Category`; staff-only, explicit price/stock per created format, archive rather than hard delete. |
| Admin order list/detail and shipment update | `GET /admin/orders`, `GET /admin/orders/{orderId}`, `PATCH /admin/orders/{orderId}/fulfillment` | `Order`, `OrderItem`, `Payment`, `Shipment`; staff-only; fulfillment update changes shipment only. |

## Entity Fields, Keys, and Relationships

The following is the persisted entity inventory. Types are Django model field types; API serializers map these storage fields to the documented camelCase JSON properties. `PK` denotes a primary key, `FK` a foreign key, and `UK` a unique field or constraint. Full validation, deletion, and index rules are specified in the [database architecture](../database/database-architecture.md).

| Entity | Fields and data types |
| --- | --- |
| `User` | `id: UUIDField (PK)`; `email: EmailField (required, UK)`; `first_name`, `last_name: CharField(150)`; `phone_number: CharField(32)`; `password: Django auth password field (encoded hash only)`; `terms_accepted_at: DateTimeField (nullable only for provisioned/legacy accounts)`; `is_staff: BooleanField`; `date_joined: DateTimeField`. |
| `Address` | `id: UUIDField (PK)`; `user_id: UUIDField (FK → User)`; `label: CharField(40, nullable)`; `company: CharField(200, nullable)`; `address_line1`, `address_line2: CharField(255, with line2 nullable)`; `city`, `state_region: CharField(120)`; `postal_code: CharField(6)`; `country_code: CharField(2)`; `phone: CharField(32)`; `is_default: BooleanField`; `created_at`, `updated_at: DateTimeField`. |
| `Author` | `id: UUIDField (PK)`; `name: CharField(200)`. |
| `Category` | `id: UUIDField (PK)`; `name: CharField(100)`; `slug: SlugField(120, UK)`; `parent_id: UUIDField (nullable self-FK → Category)`; `is_active: BooleanField`. |
| `Book` | `id: UUIDField (PK)`; `author_id: UUIDField (FK → Author)`; `title: CharField(300)`; `slug: SlugField(320, UK)`; `description: TextField (nullable)`; `isbn_10: CharField(10, nullable, conditionally unique)`; `isbn_13: CharField(13, nullable, conditionally unique)`; `cover_image: ImageField or storage key (nullable)`; `rating: DecimalField(2,1, nullable)`; `status: CharField(16)`; `published_at: DateTimeField (nullable)`; `created_at`, `updated_at: DateTimeField`. |
| `BookCategory` | `id: UUIDField (PK)`; `book_id: UUIDField (FK → Book)`; `category_id: UUIDField (FK → Category)`; unique constraint on `(book_id, category_id)`. |
| `PhysicalVariant` | `id: UUIDField (PK)`; `book_id: UUIDField (FK → Book)`; `format: CharField(16)`; `price: DecimalField(12,2)`; `currency: CharField(3)`; `stock_quantity: PositiveIntegerField`; `is_available: BooleanField`; `updated_at: DateTimeField`. |
| `Cart` | `id: UUIDField (PK)`; `user_id: UUIDField (one-to-one FK → User, unique)`; `updated_at: DateTimeField`. |
| `CartItem` | `id: UUIDField (PK)`; `cart_id: UUIDField (FK → Cart)`; `physical_variant_id: UUIDField (FK → PhysicalVariant)`; `quantity: PositiveSmallIntegerField`. |
| `Order` | `id: UUIDField (PK)`; `order_number: CharField(32, UK)`; `user_id: UUIDField (FK → User)`; `status: CharField(20)`; `currency: CharField(3)`; `subtotal`, `shipping_amount`, `tax_amount`, `discount_amount`, `total: DecimalField(12,2)`; `placed_at`, `confirmed_at: DateTimeField (nullable)`; `created_at: DateTimeField`. |
| `OrderItem` | `id: UUIDField (PK)`; `order_id: UUIDField (FK → Order)`; `book_id: UUIDField (FK → Book)`; `physical_variant_id: UUIDField (FK → PhysicalVariant)`; `title_snapshot: CharField(300)`; `format_snapshot: CharField(20)`; `quantity: PositiveSmallIntegerField`; `unit_price`, `line_total: DecimalField(12,2)`; `currency: CharField(3)`. |
| `Shipment` | `id: UUIDField (PK)`; `order_id: UUIDField (one-to-one FK → Order, unique)`; `status: CharField(20)`; `recipient_name: CharField(200)`; `company: CharField(200, nullable)`; `address_line1`, `address_line2: CharField(255, with line2 nullable)`; `city`, `state_region: CharField(120)`; `postal_code: CharField(6)`; `country_code: CharField(2)`; `phone: CharField(32)`; `carrier: CharField(100, nullable)`; `tracking_reference: CharField(200, nullable)`; `shipped_at`, `delivered_at: DateTimeField (nullable)`; `created_at`, `updated_at: DateTimeField`. |
| `Payment` | `id: UUIDField (PK)`; `order_id: UUIDField (FK → Order)`; `provider: CharField(40)`; `provider_reference: CharField(200, nullable, unique per provider when set)`; `status: CharField(20)`; `amount: DecimalField(12,2)`; `currency: CharField(3)`; `method_type: CharField(30)`; `method_brand: CharField(30, nullable)`; `last_four: CharField(4, nullable)`; `idempotency_key: UUIDField (UK)`; `failure_code: CharField(100, nullable)`; `created_at`, `updated_at: DateTimeField`. |

| Relationship | Cardinality and key |
| --- | --- |
| `User` — `Address` | One user has zero or many addresses; each address has one required `user_id` FK. |
| `User` — `Cart` | One user has zero or one cart; each cart has one unique `user_id` FK. |
| `Cart` — `CartItem` | One cart has zero or many items; each item has one required `cart_id` FK. |
| `PhysicalVariant` — `CartItem` | One variant may appear in many cart items; each item selects one required `physical_variant_id` FK. |
| `Author` — `Book` | One author has zero or many books; each book has exactly one required `author_id` FK. |
| `Book` — `Category` | Many-to-many through `BookCategory`, whose required `book_id` and `category_id` FKs are unique as a pair. |
| `Book` — `PhysicalVariant` | One book has zero or more variants; each variant belongs to one required book. At most one variant per supported format per book. |
| `User` — `Order` | One user has zero or many orders; each order has one required `user_id` FK. |
| `Order` — `OrderItem` | One order has one or more items; each item has one required `order_id` FK. |
| `Book` / `PhysicalVariant` — `OrderItem` | Each item references one book and one physical variant; the variant must belong to the same book. Snapshot fields preserve purchase-time display and price. |
| `Order` — `Shipment` | One order has exactly one shipment; `Shipment.order_id` is a unique one-to-one FK. |
| `Order` — `Payment` | One order has zero or more payment attempts; each attempt has one required `order_id` FK. |

## Security and Error Behavior

Bearer authentication is an API contract assumption; token type, expiry/refresh, and revocation storage must be selected consistently with the deployed Django/DRF authentication setup. Do not place bearer tokens in URLs. Return a stable error object (`code`, `message`, `requestId`, optional structured `details`); use `400` for validation, `401` for missing/invalid identity, `403` for missing staff permission, `404` for missing or non-owned resources, `409` for stock/state/idempotency conflicts, and `429` with `Retry-After` for throttling. Never leak whether a foreign customer's private order/address exists.

Payment callbacks are not customer-authenticated. Provider identity/signature format is adapter-specific and cannot be finalized until a provider is selected. Validate event authenticity and matching order, amount, and `INR` currency before state changes. Do not persist or return PAN, CVV, provider credentials/secrets, or raw webhook payloads. Safe provider references and approved display metadata only.

## Assumptions and Open Decisions

- **Provider:** Provider selection, hosted/tokenized integration details, capture behavior, and callback formats are unresolved. Accepted methods are fixed: card brands AMEX/VISA/MASTERCARD and PayPal.
- **India tax:** Tax applicability, calculation, inclusion, and rounding are unresolved; no rate or exemption is assumed. Shipping is fixed at INR 0.00.
- **Cancellation/refund:** Customer cancellation, staff cancellation, refund eligibility, and provider refund lifecycle are unresolved; no cancellation/refund endpoint is defined.
- **Tracking:** Shipment tracking support, carrier integration, tracking guarantees, and exact fulfillment transition graph are unresolved. Order confirmation does not mean shipment/delivery completion.
- **Inventory reservation:** Checkout reserves/decrements tracked stock transactionally and prevents oversell. Reservation expiry and release/restock behavior after payment failure or cancellation are unresolved; no timeout policy is implied.
- **Terms:** Registration requires acceptance and records server time. Terms document versioning is unresolved; no version identifier is assumed.
- **Rating:** Rating is an independent catalog field. Its source/maintenance process, fractional filter bucket semantics, and unrated-sort policy require product confirmation; the contract does not add customer reviews or rating submissions.
- **Authentication and hosting:** API host, token implementation/lifetime, email provider/queue, and deployment details are not present in the source documents and must be selected before implementation.

The API deliberately excludes ebooks, gifts, customer reviews, generic notifications, guest checkout, and customer payment credentials. It does not claim successful payment until verified provider confirmation.
