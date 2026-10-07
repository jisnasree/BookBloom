# Catalog Requirements

## Scope

The catalog experience covers three desktop screens in the [BookBloom Figma file](https://www.figma.com/design/CMaYhdVPa2mBS0diJ57KGm/BookBloom?node-id=410-3):

- **Home** (`410:3`): shared navigation and search, a hero image at the top, and a featured-books carousel.
- **Catalog Search + Filters** (`410:185`): searchable, filterable, sortable book results.
- **Book Detail** (`410:293`): book information, rating, format prices, and an add-physical-book action.

## Functional requirements

### Home

- Show the shared navigation, including Home, Books, Categories, and Orders, and a search field.
- Show the hero image above the featured-books section. The image comes from the React template, not an API.
- Present featured books in a carousel with cover, title, author, format, INR price, and rating.
- Load featured books via the catalog books endpoint with `featured=true`; include only books whose catalog `featured` flag is `true`; books default to not featured.
- Provide carousel navigation and a link to see all featured books.

### Catalog results

- Show a catalog title, search field, result count, filters, and book cards.
- Search by title, author, or keyword.
- Allow filtering by category (Kids, Fiction, Romance, Literature, Mystery & Thrillers), price band (under ₹500, ₹500–₹1000, over ₹1000), format (Hardcover, Paperback), and rating (1–5 stars).
- Provide sorting by Newest, Title A–Z, Price low–high, and Price high–low.
- Preserve the existing/default result order when no sort is selected. The design labels this “Default order”; its result-count example also says “sorted by popularity”.
- Each result card shows a cover, title, author, format, INR price, and rating.
- Show numbered pagination beneath the results: Previous, current page, nearby pages, an ellipsis when pages are omitted, and Next.
- Show the current result range and total, for example, “Showing 1–12 of 128 books”. Use 12 results per page; 128 results therefore span 11 pages, with 8 results on the last page.
- Disable or omit Previous on the first page and Next on the last page. Keep the current search, filters, and sort when changing pages.
- Return to page 1 when search, filters, or sort changes.
- Allow the catalog results to be filtered to featured books for the Home screen's “see all featured books” link.
- Show a clear empty state when a search or filter combination has no matches.

### Book detail

- Show the book cover, title, author, description, and rating.
- Show available formats and the price for each format.
- Provide an action to add the physical book to the cart.

## Shared behavior

- Prices use Indian rupees (₹).
- Search, filters, and sorting should work together and update the result count and displayed books.
- Selecting a book from Home or the catalog opens that book’s detail screen.
- The catalog cards and detail screen should use consistent book and `PhysicalVariant` data.
