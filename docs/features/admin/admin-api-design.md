# Admin API Design

Authenticated, permission-protected operations for the Admin screens in [Figma](./figma.md). Routes use `/api/v1`; request and response JSON uses camelCase. All operations below require staff authentication and the corresponding Django permission.

## Book management

| Method and path | Purpose |
|---|---|
| `GET /admin/books` | Search and paginate books. |
| `POST /admin/books` | Create a book and its physical variants. |
| `GET /admin/books/{bookId}` | Read a book for admin editing. |
| `PATCH /admin/books/{bookId}` | Update book metadata, author/category assignments, or variants. |
| `POST /admin/books/{bookId}/archive` | Archive a book without removing historical order references. |

Book create/update fields for relationships:

```json
{
  "title": "Atomic Habits",
  "slug": "atomic-habits",
  "authorId": "author-uuid",
  "categoryIds": ["category-uuid-1", "category-uuid-2"]
}
```

`authorId` identifies exactly one existing Author and is required when creating a book. `categoryIds` identifies zero or more existing categories; BookCategory rows are replaced only when `categoryIds` is present in a PATCH. An empty array explicitly clears all category assignments. Do not accept `authorName` or category display labels as relationship identifiers.

## Author management

| Method and path | Purpose |
|---|---|
| `GET /admin/authors` | Search and paginate authors; optionally include associated-book counts. |
| `POST /admin/authors` | Create an author from a required display name. |
| `GET /admin/authors/{authorId}` | Read an author and associated-book count. |
| `PATCH /admin/authors/{authorId}` | Update an author's display name. |

There is no hard-delete operation because Author has no archive field and books require an Author foreign key. Return `409 Conflict` if a future delete operation is attempted for an author referenced by a book.

## Category management

| Method and path | Purpose |
|---|---|
| `GET /admin/categories` | Search and paginate categories. |
| `POST /admin/categories` | Create a category. |
| `GET /admin/categories/{categoryId}` | Read a category and associated-book count. |
| `PATCH /admin/categories/{categoryId}` | Update name or slug. |

A category's slug is unique. When omitted on creation, the service may derive it from the normalized name and must still enforce uniqueness.

## Order management

| Method and path | Purpose |
|---|---|
| `GET /admin/orders` | Search and paginate orders for the Order Management screen. |
| `GET /admin/orders/{orderId}` | Retrieve the selected order's customer, item, payment, and shipment details for the separate Order Details screen. |
| `PATCH /admin/orders/{orderId}/fulfillment` | Update shipment status and optional carrier/tracking information from Order Details; does not change order or payment status. |

The order list's View action navigates to `/admin/orders/{orderId}`. The detail response includes the immutable shipping-address snapshot and safe payment metadata; it must not expose payment secrets or raw provider events.

## Dropdown behavior

- The Author control is a single-select dropdown populated from authorized admin author data; submit the selected `authorId`.
- The Categories control is a multi-select dropdown populated from existing categories; submit selected `categoryIds`.
- An edit form shows current assignments and does not silently replace them when the field is omitted.
- Author/category management screens provide the create/edit actions to maintain dropdown choices.

## Errors and conventions

- `400`: invalid fields, malformed UUIDs, unsupported relationship payloads, or invalid pagination.
- `401`: missing or invalid authentication.
- `403`: authenticated user lacks staff/admin permission.
- `404`: requested book, author, category, or associated resource is unavailable.
- `409`: duplicate book slug/ISBN or category slug; invalid conflict with referenced data.
- Restrict every query to authorized admin access. Do not expose credentials or protected user information.
- Book/author/category CRUD does not alter immutable `OrderItem` purchase snapshots.