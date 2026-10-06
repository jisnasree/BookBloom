# Cart API Design

Simple authenticated REST contract for the Shopping Cart screen in the [BookBloom Figma file](https://www.figma.com/design/CMaYhdVPa2mBS0diJ57KGm/BookBloom?node-id=437-3). These endpoints follow the conventions in the project API contract; the complete feature spec is [cart-openapi.yaml](./cart-openapi.yaml).

**Base path:** `/api/v1`  
**Authentication:** Bearer token; operations are scoped to the current customer.  
**Money:** Decimal strings in INR (for example, `"2249.00"`), not JSON floating-point values.

## Endpoints

| Method and path | Purpose |
|---|---|
| `GET /cart` | Return the current customer's cart, including an empty cart. |
| `POST /cart/items` | Add a `PhysicalVariant` by `physicalVariantId` and `quantity`; consolidate an existing matching variant. |
| `PATCH /cart/items/{itemId}` | Update a line's quantity. |
| `DELETE /cart/items/{itemId}` | Remove one line from the current customer's cart. |
| `DELETE /cart/items` | Empty the current customer's cart. |

### Example: `GET /cart`

```json
{
  "id": "cart-uuid",
  "items": [
    {
      "id": "item-uuid",
      "physicalVariantId": "variant-uuid",
      "title": "Atomic Habits",
      "author": "James Clear",
      "coverUrl": "https://example.test/atomic-habits.jpg",
      "format": "hardcover",
      "quantity": 1,
      "unitPrice": "2249.00",
      "lineTotal": "2249.00",
      "currency": "INR",
      "inStock": true
    }
  ],
  "subtotal": "2249.00",
  "estimatedShipping": "0.00",
  "total": "2249.00",
  "currency": "INR",
  "updatedAt": "2026-10-05T12:00:00Z"
}
```

### Request examples

Add a physical variant:

```json
{ "physicalVariantId": "variant-uuid", "quantity": 1 }
```

Update quantity:

```json
{ "quantity": 2 }
```

The **Update cart** button submits quantity changes for the affected lines and then refreshes the displayed cart totals. Do not send prices in mutation requests.

## Validation and errors

- `400 Bad Request`: invalid quantity or request fields.
- `401 Unauthorized`: missing or invalid authentication.
- `404 Not Found`: physical variant unavailable or cart item not found in the caller's cart.
- `409 Conflict`: requested quantity exceeds currently available stock.
- Adding an inactive or unavailable physical variant is rejected. Stock and current catalog prices are revalidated at checkout.
- Checkout uses the separate checkout operation; the cart API does not place orders.
