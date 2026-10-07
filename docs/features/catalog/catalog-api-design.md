# Catalog API Design

This is a simple REST contract for the three catalog screens in the [BookBloom Figma file](https://www.figma.com/design/CMaYhdVPa2mBS0diJ57KGm/BookBloom?node-id=410-3). Routes use `/api`; request and response examples are illustrative.

## Endpoints

### `GET /api/catalog/books`

Returns catalog results for search, filters, and sorting.

| Query parameter | Meaning |
|---|---|
| `q` | Search title, author, or keyword |
| `category` | Category name or ID; repeatable |
| `minPrice`, `maxPrice` | Inclusive INR price bounds |
| `format` | `hardcover` or `paperback`; repeatable |
| `minRating` | Minimum rating, from 1 to 5 |
| `featured` | Optional boolean filter; when supplied, match books with that `featured` value. Omit to include both featured and non-featured books. |
| `sort` | `default`, `newest`, `title_asc`, `price_asc`, or `price_desc` |
| `page` | 1-based page number; defaults to `1` |
| `pageSize` | Number of results per page; defaults to `12` |

With no `sort`, return results in the configured default order. The Figma example calls this “Default order” and describes results as sorted by popularity; confirm the precise ranking rule when implementing the service.

Apply search, filters, and sorting before pagination. Return only the requested page in `items`, while `total` is the number of matching books before pagination. The UI can calculate the number of pages as `ceil(total / pageSize)` and the displayed range from `page`, `pageSize`, and `total`. When search, filters, or sort changes, the client should request page `1`. Reject invalid page values and constrain `pageSize` to a server-defined maximum.

Response:

```json
{
  "items": [{
    "id": "book-id",
    "title": "Atomic Habits",
    "author": "James Clear",
    "coverUrl": "https://example.test/cover.jpg",
    "featured": false,
    "physicalVariantId": "variant-id",
    "format": "HARDCOVER",
    "price": "2249.00",
    "currency": "INR",
    "rating": 5
  }],
  "total": 128,
  "page": 1,
  "pageSize": 12
}
```

Prices are decimal strings in INR. The displayed rating is on a 1–5 scale. For this example, the UI displays “Showing 1–12 of 128 books” and 11 pages; the final page contains 8 books.

### `GET /api/catalog/books/{bookId}`

Returns book details and available physical variants for the detail screen. The `variants` array uses the same `PhysicalVariant` concept as the catalog and cart models.

Response:

```json
{
  "id": "book-id",
  "title": "Atomic Habits",
  "author": "James Clear",
  "description": "A practical guide to building better habits.",
  "coverUrl": "https://example.test/cover.jpg",
  "featured": true,
  "rating": 5,
  "variants": [
    { "id": "variant-id", "format": "HARDCOVER", "price": "2249.00", "currency": "INR", "inStock": true },
    { "id": "variant-id-2", "format": "PAPERBACK", "price": "1699.00", "currency": "INR", "inStock": true }
  ]
}
```

Return `404 Not Found` if the book does not exist.

## Notes

- The Figma file defines the visible catalog fields and controls, not authentication, cart, or checkout contracts.
- `coverUrl` represents the cover art shown in the design.
- The catalog Figma screen shows Previous/Next controls, numbered pages with an ellipsis, a selected page, and a result-range summary below the grid.
- Pagination state is request state; it does not require a database table.
