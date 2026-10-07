# Admin Management Requirements

## Scope

Admin users manage books, authors, categories, and orders through the screens on the [Admin Figma page](./figma.md). All admin operations require an authenticated staff account with the appropriate permission.

## Book management

- List, search, create, update, and archive catalog books.
- Require exactly one existing author per book, selected through a single-select Author dropdown.
- Allow zero or more categories per book, selected through a multi-select Categories control.
- Author and category choices reference existing records; provide navigation to their management screens for adding or editing those records.
- Preserve existing ISBN, description, cover, status, physical-variant price, format, and stock management.
- The database relationships are one `Author` to many `Book` records and many-to-many `Book` to `Category` through `BookCategory`. A book therefore has an Author foreign key and category links through the join table, not a singular category foreign key.
- Reject saving when the selected author or category does not exist.

## Author management

- List/search authors and show how many books are associated with each.
- Create an author using a required display name; edit the name of an existing author.
- Do not hard-delete an author referenced by a book. The current Author model has no active/archive field.
- Selecting an author in Book Management uses the Author record ID, not its display name as an identity.

## Category management

- List/search categories and show their name and unique slug.
- Create and edit categories.
- Provide existing categories as choices for book assignments.
- Ensure each category slug is unique.

## Order management

- List and search orders in the Order Management screen.
- Each order's View action opens a separate Order Details screen; do not embed an individual order's details in the list page.
- Show the selected order's customer, items, payment state, shipping snapshot, and fulfillment state on the detail screen.
- Allow authorized staff to update shipment fulfillment status from the detail screen without changing payment or order-confirmation status.
- Provide a clear return action to the order list.

## Access, validation, and screen behavior

- Restrict every admin list, detail, create, and update operation to staff with the relevant permission; customer accounts cannot access these screens or operations.
- Validate unique book slugs/ISBNs and category slugs, and preserve existing price, stock, and status rules.
- Figma forms, dropdowns, tables, and buttons are design mockups; this document describes intended behavior, not implemented interactivity.

## Out of scope

- Multiple authors per book, hard deletion of referenced authors/categories, bulk import, and category analytics are not defined.
- The precise author/category permission split and audit-retention policy remain implementation decisions.