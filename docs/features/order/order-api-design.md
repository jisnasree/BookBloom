# Order API Design

Simple customer-facing API for Order History and Order Details, based on the [Order Details Figma screen](https://www.figma.com/design/CMaYhdVPa2mBS0diJ57KGm/BookBloom?node-id=449-55). It follows the broader project contract in `docs/api/api-design.md`.

**Base path:** `/api/v1`  
**Authentication:** Bearer token; every operation is scoped to the current customer.  
**Money:** INR decimal strings with two fractional digits, for example `"3448.00"`.

## Endpoints

| Method and path | Purpose |
|---|---|
| `GET /orders` | Return the customer's paginated order history, newest first. |
| `GET /orders/{orderId}` | Return one of the customer's orders with its items, totals, payment summary, and shipment details. |

### `GET /orders`

Optional query parameters:

| Parameter | Meaning |
|---|---|
| `page` | 1-based page number; defaults to `1` |
| `pageSize` | Results per page; defaults to `20`, maximum `100` |
| `status` | Filter by order status |
| `fulfillmentStatus` | Filter by independent shipment status |

Return order summary fields needed by the history cards: order ID/number, status, placed date, representative item details, and total. Include pagination metadata.

### `GET /orders/{orderId}`

Returns:

- Order number, status, and placed/confirmed timestamps.
- Immutable order items with title, format, quantity, unit price, line total, and optional cover URL.
- Subtotal, free shipping amount, tax amount, discount amount, total, and currency.
- Shipping snapshot and shipment status/timestamps/tracking reference when available.
- Safe payment attempt summaries only.

Return `404 Not Found` if the order does not exist or is not owned by the caller.

## Rules

- Validate pagination and status filters; return `400 Bad Request` for invalid values and `401 Unauthorized` for missing or invalid authentication.
- Customer order queries must be restricted in the data-access layer to the authenticated user.
- Do not expose provider secrets, PAN, CVV, or raw payment-provider payloads.
- Order confirmation state and shipment fulfillment state remain separate.
