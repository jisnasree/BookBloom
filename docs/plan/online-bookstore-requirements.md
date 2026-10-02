# BookBloom Web App Requirements

## 1. Simple Requirements Brief

### 1.1 Working Title

BookBloom Web App

### 1.2 Background

The product is a customer-facing online bookstore where registered customers can browse, search, and purchase all kinds of books. The store will support both physical books and ebooks.

### 1.3 Problem To Solve

Customers need a simple online place to discover books, purchase them, send physical books as gifts, and access ebook purchases. Store administrators need a way to manage the book catalog and customer orders.

### 1.4 Target Users

- Registered customers who want to buy books online.
- Gift buyers who want to send physical books to another person.
- Store administrators who manage books, pricing, inventory, reviews, notifications, and orders.

### 1.5 Desired Outcome

Customers should be able to create an account, find books, purchase physical books or ebooks, send physical books as gifts, access purchased ebooks from their account, leave reviews, and receive useful order-related notifications.

Administrators should be able to manage the bookstore catalog, customer orders, reviews, and key operational updates.

### 1.6 Initial Scope

The first version should include:

- Web-only customer and admin views for the MVP.
- Responsive web application behavior for desktop, tablet, and mobile viewports.
- Figma MVP designs focused on desktop web frames only.
- Static homepage promotional section with featured book imagery and a clear shopping call-to-action.
- Customer account creation and login.
- Book catalog for all kinds of books.
- Search and filtering by title, author, category, price, and format.
- Book detail pages.
- Customer reviews and ratings.
- Shopping cart.
- Checkout for registered customers.
- Purchase support for physical books and ebooks.
- Shipping address collection for physical books.
- Gift purchase option for physical books.
- Gift recipient name and shipping address.
- Optional personal gift message.
- Ebook download after purchase.
- Ebook access from the customer account library.
- Advanced notifications for important customer and order events.
- Admin area for managing books and orders.

### 1.7 Out Of Scope For Now

The following can be considered later unless needed immediately:

- Guest checkout.
- Loyalty program or rewards.
- Subscription plans.
- Used book marketplace features.
- Seller or vendor accounts.
- Advanced in-browser ebook reader tools.
- International tax and complex shipping rules.
- Promotional campaigns and coupons.
- Wishlists.
- Book recommendations or personalization.
- Native mobile applications.
- Tablet-only or mobile-only MVP designs that do not cover standard desktop web layouts.
- Separate tablet and mobile Figma screen sets for the MVP design pass.

### 1.8 Key User Workflows

#### Customer Registration And Login

A customer creates an account or logs into an existing account before purchasing books.

#### Browse And Search Books

A customer browses the catalog or searches for books by title, author, category, price, or format.

#### View Book Details

A customer opens a book detail page to view information such as title, author, description, format, price, availability, ratings, and reviews.

#### Purchase Physical Book

A customer adds a physical book to the cart, enters shipping details, completes checkout, and receives order confirmation.

#### Send Physical Book As Gift

A customer selects a gift option for a physical book, enters the recipient name and shipping address, adds an optional personal message, and completes checkout.

#### Purchase Ebook

A customer adds an ebook to the cart, completes checkout, and can then download the ebook or access it from their account library.

#### Review A Book

A registered customer can leave a rating and review for a book.

#### Receive Notifications

A customer receives notifications for order confirmation, ebook access, shipping updates, gift order updates, and relevant account messages.

#### Manage Books And Orders

An administrator can add, update, or remove books, manage pricing and format options, view customer orders, and support fulfillment.

### 1.9 Business Rules Or Constraints

- Customers must have an account to purchase books.
- Books may be available as physical books, ebooks, or both.
- Physical book purchases require a shipping address.
- Gift purchases require recipient name and recipient shipping address.
- Gift purchases may include a personal message.
- Ebook purchases must be available for download after purchase.
- Ebook purchases must also appear in the customer's account library.
- Reviews and ratings should be tied to registered customer accounts.
- Notifications should be triggered by key order, ebook, shipping, gift, and account events.
- Admin users must be able to manage the catalog and orders.
- All customer-facing and admin-facing book prices, cart totals, order totals, and checkout amounts must be displayed in INR.

### 1.10 Open Questions

- What payment methods should be supported?
- Should physical book orders include delivery tracking?
- Should customers receive email confirmations in addition to in-app notifications?
- Should inventory be tracked for physical books?
- Should ebooks have file format options such as PDF, EPUB, or MOBI?
- Should customers be able to refund or cancel orders?
- Should admins moderate reviews before they appear publicly?
- What information should be shown on the customer account page?
- Should there be tax, shipping fee, or discount calculations in the first version?

### 1.11 Recommended Next Step

The next step is to define the highest-priority workflows in more detail: account creation, book search, checkout, gift shipping, ebook access, reviews, notifications, and admin catalog management. After that, these requirements can be converted into user stories and acceptance criteria.

## 2. Module And Feature Planning

### 2.1 Major Application Modules

1. Customer Account Module
2. Book Catalog Module
3. Search and Filtering Module
4. Book Detail Module
5. Reviews and Ratings Module
6. Shopping Cart Module
7. Checkout and Payment Module
8. Shipping and Gift Module
9. Ebook Library Module
10. Order Management Module
11. Admin Management Module
12. Notification Module

### 2.2 Features By Module

| Module | Features / Functions |
| --- | --- |
| Customer Account Module | Customer registration, login, logout, profile management, saved shipping addresses, order history |
| Book Catalog Module | Display all books, organize books by category, support physical and ebook formats, show pricing and availability |
| Search and Filtering Module | Search by title and author, filter by category, price, format, and rating |
| Book Detail Module | Show book title, author, description, format options, price, availability, ratings, and reviews |
| Reviews and Ratings Module | Allow registered customers to submit ratings and reviews, display average rating, display customer reviews |
| Shopping Cart Module | Add books to cart, update quantities, remove items, show cart subtotal |
| Checkout and Payment Module | Confirm cart, collect payment details, calculate order total, place order |
| Shipping and Gift Module | Collect shipping address, support gift recipient name and address, allow personal gift message |
| Ebook Library Module | Provide ebook download after purchase, show purchased ebooks in customer account library |
| Order Management Module | Store customer orders, show order status, separate physical book and ebook fulfillment needs |
| Admin Management Module | Add, edit, and remove books; manage prices and formats; view and update orders |
| Notification Module | Send order confirmation, ebook access confirmation, shipping updates, gift order updates, and account-related messages |

### 2.3 Module Dependencies

| Module | Depends On | Reason |
| --- | --- | --- |
| Book Detail Module | Book Catalog Module | Book details come from catalog data |
| Search and Filtering Module | Book Catalog Module | Search and filters operate on catalog data |
| Reviews and Ratings Module | Customer Account Module, Book Detail Module | Reviews must be tied to registered customers and specific books |
| Shopping Cart Module | Customer Account Module, Book Catalog Module | Customers add catalog items to their cart |
| Checkout and Payment Module | Customer Account Module, Shopping Cart Module | Checkout requires a logged-in customer and cart items |
| Shipping and Gift Module | Checkout and Payment Module | Shipping and gift details are collected during checkout for physical books |
| Ebook Library Module | Customer Account Module, Checkout and Payment Module | Ebooks become available after purchase |
| Order Management Module | Customer Account Module, Checkout and Payment Module | Orders are created after checkout |
| Admin Management Module | Book Catalog Module, Order Management Module | Admins manage books and customer orders |
| Notification Module | Order Management Module, Ebook Library Module, Shipping and Gift Module | Notifications are triggered by order, ebook, and shipping events |

### 2.4 MVP Features To Complete First

The MVP should focus on the smallest complete web buying experience, including customer trust features and essential communication.

1. Responsive web customer experience for desktop, tablet, and mobile in implementation requirements.
2. Desktop-only Figma designs for the MVP customer screens.
3. Desktop-first web admin experience for operational use.
4. Static homepage promotional section with desktop layout.
5. Customer registration and login.
6. Book catalog with physical and ebook formats.
7. Search and filtering by title, author, category, price, and format.
8. Book detail pages.
9. Customer reviews and ratings.
10. Shopping cart.
11. Checkout for registered customers.
12. Shipping address collection for physical books.
13. Gift recipient details and personal message for physical books.
14. Ebook download after purchase.
15. Customer ebook library.
16. Basic order history.
17. Admin ability to add and edit books.
18. Admin ability to view and manage orders.
19. Advanced notifications, including order confirmation, ebook access confirmation, shipping updates, and gift order notifications.

## 3. UI/UX Design - Figma Instructions

### 3.1 Objective

Create a Figma design for an online bookstore web application. The design should cover the MVP modules and major customer and admin workflows, including browsing books, purchasing physical books and ebooks, gifting physical books, accessing ebooks, leaving reviews, receiving notifications, and managing books and orders as an admin.

The MVP is explicitly a responsive web application. For the Figma MVP design pass, create desktop web frames only. Tablet and mobile behavior should be captured as implementation requirements and responsive notes, not as separate Figma screen sets.

These instructions are intended to be used later with a Figma plugin. Do not create the Figma file yet.

### 3.2 Required Page / Screen Structure

Create the following screens in Figma:

1. Home Page
2. Book Catalog Page
3. Search Results Page
4. Book Detail Page
5. Customer Registration Page
6. Customer Login Page
7. Customer Account Dashboard
8. Shopping Cart Page
9. Address & Payment Page
10. Checkout Page
11. Gift Details Page / Checkout Section
12. Order Confirmation Page
13. Customer Order History Page
14. Ebook Library Page
15. Review Submission Flow
16. Notifications / Message Center Page
17. Admin Login Page
18. Admin Dashboard
19. Admin Book Management Page
20. Admin Add / Edit Book Page
21. Admin Order Management Page

### 3.3 Main Customer Screens

#### Home Page

Design a welcoming bookstore homepage with:

- Header navigation.
- Search bar.
- Static promotional hero or feature area for key bookstore merchandising.
- Featured books.
- Popular categories.
- New arrivals.
- Best sellers.
- Physical book and ebook highlights.
- Login / account access.
- Cart icon.
- Footer links.

Primary actions:

- Search for books.
- Browse categories.
- View featured books.
- Sign in or create account.
- Open cart.

Homepage promotional section requirements:

- Do not include a carousel in the MVP homepage design or implementation.
- Use a static promotional section instead of moving slides.
- The static section should use the heading `Discover Your Next Great Story` with supporting copy `Explore New Worlds, Meet Unforgettable Characters, and Find Books That Stay With You Long After the Last Page.` and a `Shop now` call-to-action.
- Use a book-filled background treatment inspired by bookstore merchandising banners, with many real published book covers arranged around the promotional text.
- Position the Discover Your Next Great Story text and CTA group on the left side of the promotional section.
- Do not use a visible border around the Discover Your Next Great Story text/CTA group.
- Do not use Barnes & Noble branding, `Holiday Gift Guide`, or `Find the Perfect Gift` copy in the MVP New Releases section.
- Do not use a green background or green promotional text treatment for the Discover Your Next Great Story section.
- Use a neutral or light background treatment that lets the book covers and Discover Your Next Great Story message stand out clearly.
- Use real free/publicly available book cover imagery where available.
- Size the promotional book imagery larger so it visually balances the section and avoids excessive unused whitespace.
- Keep all important text readable over the busy book background using sufficient contrast, spacing, overlay treatment, or a solid/tinted text area.
- Keep promotional content inside the desktop content container with balanced left and right margins.
- Avoid horizontal overflow; the promotional section must fit within the 1440px desktop frame.
- Because the carousel has been removed from MVP scope, no auto-rotation, slide indicators, or previous/next carousel controls are required.

New Releases and Featured Books title set:

- Include only the following titles in the New Releases promotional section and Featured Books carousel where space allows.
- Use real/original published book cover imagery for these titles where available, rather than typographic placeholders.
- `Atomic Habits` by James Clear.
- `To Kill a Mockingbird` by Harper Lee.
- `Charlotte's Web` by E. B. White.
- `Matilda` by Roald Dahl.
- `Lord of the Flies` by William Golding.
- `The Catcher in the Rye` by J. D. Salinger.
- `Rich Dad Poor Dad` by Robert T. Kiyosaki.
- `The Kite Runner` by Khaled Hosseini.
- `Mockingjay` by Suzanne Collins.
- `Pocketful of Poesies` by Salley Mavor.
- `Fireflies`.
- `The Lord of the Rings` by J. R. R. Tolkien.
- `Young Sheldon`.
- `Randamoozham`.

Featured books section requirements:

- Present featured books as a horizontal carousel on the homepage.
- Include a visible `See all` link near the Featured Books section heading.
- Show a row of featured book cards with real cover images, title, author, available format, price, and rating.
- Use larger featured book cards with cover-dominant layouts so the original book cover artwork is easy to recognize.
- For each featured book card, show one available format option: `Paperback`, `Hardcover`, or `Ebook`.
- Show the price on a separate line below the format option.
- Show the rating as star icons on a separate line below the price.
- Use one filled star for a 1-star rating, two filled stars for a 2-star rating, and so on through five filled stars for a 5-star rating.
- Show book prices in INR, not dollars.
- Include carousel navigation controls for moving through featured books.
- Keep the featured books carousel inside the desktop content container without horizontal page overflow.
- Ensure carousel controls are keyboard accessible and have visible focus states in implementation.

#### Book Catalog Page

Design a catalog page where users can browse all books.

Include:

- Book grid or list view.
- Filters for category, price, format, and rating.
- Sort options such as newest, price, popularity, and rating.
- Book cards showing cover, title, author, price, format, rating, and availability.
- All prices must be shown in INR.
- Add to cart or view details action.

Catalog filter options:

- Category: Kids, Fiction, Romance, Literature, Mystery & Thrillers.
- Price: Under ₹500, ₹500-₹1000, Over ₹1000.
- Format: Hardcover, Paperback, Ebook.
- Reviews: 5 stars, 4 stars, 3 stars, 2 stars, 1 star.

#### Search Results Page

Design a search results page similar to the catalog page.

Include:

- Search term display.
- Result count.
- Filters.
- Sorting.
- Empty state for no results.
- Suggested categories or popular books when no results are found.

#### Book Detail Page

Design a detailed book page with:

- Book cover.
- Title.
- Author.
- Description.
- Category.
- Format options: physical, ebook, or both.
- Price by format.
- Availability.
- Quantity selector for physical books.
- Add to cart button.
- Gift option for physical books.
- Ratings summary.
- Customer reviews.
- Write review action for eligible logged-in customers.

On the individual book detail screen, show the format options as borderless choices for Hardcover, Ebook, and Paperback. Display the price directly below each format option.

### 3.4 Account Screens

#### Registration Page

Design a customer registration form with:

- Full name.
- Email address.
- Password.
- Confirm password.
- Create account button.
- Link to login page.
- Basic validation and error states.

#### Login Page

Design a customer login form with:

- Email address.
- Password.
- Login button.
- Forgot password link.
- Link to create account page.
- Error state for invalid login.

#### Customer Account Dashboard

Design an account dashboard with navigation to:

- Profile.
- Order history.
- Ebook library.
- Saved addresses.
- Notifications.
- Reviews.

Show a summary of:

- Recent orders.
- Recently purchased ebooks.
- Latest notifications.

### 3.5 Shopping And Checkout Screens

#### Shopping Cart Page

Rename the cart and checkout entry point as **Shopping Cart** in the screen title and navigation labels.

Design the Shopping Cart page as a desktop two-column layout:

- Left side: cart books and item controls.
- Right side: order total and checkout actions.

Each cart book row should show:

- Book cover.
- Book title, author, and selected format such as paperback, hardcover, or ebook.
- Availability status for purchasable items.
- Quantity control where applicable.
- Current price, with optional original price shown separately as a strikethrough when discounted.
- Remove item action.

The right-side order total area should show:

- Subtotal and total.
- Update cart action.
- Checkout button.
- Safe and secure checkout note.
- Payment method indicators limited to Visa, Mastercard, and Amex.

The page should also include Empty Cart and Continue Shopping actions. Do not include a separate "Next step: checkout" note on the Shopping Cart page. Use the same green accent color used on other pages for primary cart actions instead of pink. Use the same warm off-white page background as the other desktop screens. Keep book cover image sizing and font sizing consistent with the other desktop pages. Clearly distinguish physical books from ebooks.

#### Checkout Page

Design a checkout flow for registered customers.

Include sections for:

- Order summary.
- Shipping address for physical books.
- Gift option for physical books.
- Payment details.
- Final review.
- Place order button.

For ebook-only orders, shipping should not be required.

#### Address & Payment Page

Add a dedicated screen after the Shopping Cart page where registered customers enter or confirm shipping address details and choose a payment method.

The address section should include:

- Country/region selector.
- First name and last name.
- Company field marked optional.
- Address search/input field.
- Apartment, suite, or unit field marked optional.
- City.
- State selector.
- ZIP/postal code.
- Phone number.

The payment section should include:

- Secure payment helper text.
- Credit card payment option selected by default.
- Payment method indicators for Visa, Mastercard, and Amex.
- Card number field.
- Expiration date field.
- Security code field.
- Name on card field.
- Checkbox for using the shipping address as the billing address.
- PayPal payment option as an alternate method.

#### Gift Details Section

When a physical book is marked as a gift, include fields for:

- Recipient name.
- Recipient shipping address.
- Optional personal message.

The gift section should appear only for physical book purchases.

#### Order Confirmation Page

Design a confirmation screen showing:

- Order number.
- Purchased books.
- Delivery details for physical books.
- Ebook access instructions.
- Gift recipient details, if applicable.
- Link to order history.
- Link to ebook library.

### 3.6 Ebook Screens

#### Ebook Library Page

Design a customer ebook library with:

- List or grid of purchased ebooks.
- Book cover.
- Title.
- Author.
- Purchase date.
- Download button.
- Read or access button.
- Search within library.

### 3.7 Reviews And Ratings Flow

Design the review flow for registered customers.

Include:

- Write review button on book detail page.
- Rating selector.
- Review text field.
- Submit review button.
- Success message.
- Error and validation states.

Reviews should display:

- Customer name or display name.
- Rating.
- Review text.
- Review date.
- Ratings should use individual star icons/images matching the numeric rating instead of written text such as `5 stars`.

### 3.8 Notifications

Design a notification or message center covering:

- Order confirmation.
- Ebook access confirmation.
- Shipping updates.
- Gift order updates.
- Account-related messages.

Each notification should show:

- Notification title.
- Short message.
- Date/time.
- Read/unread state.
- Related order or book link where applicable.

### 3.9 Admin Screens

#### Admin Dashboard

Design an admin dashboard with:

- Total books.
- Recent orders.
- Pending physical shipments.
- Recent ebook purchases.
- Review activity.
- Quick links to book and order management.

#### Admin Book Management Page

Design a table or list for managing books.

Include:

- Book title.
- Author.
- Category.
- Format availability.
- Price.
- Stock for physical books.
- Status.
- Edit action.
- Delete or remove action.
- Add new book button.

#### Admin Add / Edit Book Page

Design a form with:

- Book title.
- Author.
- Description.
- Category.
- Cover image upload placeholder.
- Format selection: physical, ebook, or both.
- Physical book price.
- Ebook price.
- Physical stock quantity.
- Ebook file upload placeholder.
- Publish/unpublish status.
- Save button.

#### Admin Order Management Page

Design an order management table with:

- Order number.
- Customer name.
- Order date.
- Order type: physical, ebook, or mixed.
- Gift indicator.
- Payment status.
- Fulfillment status.
- View details action.

Order detail view should show:

- Customer details.
- Shipping address.
- Gift recipient details.
- Gift message.
- Purchased items.
- Ebook delivery status.
- Physical shipping status.

### 3.10 Navigation Requirements

Use consistent navigation across the customer-facing app.

Customer navigation should include:

- Home.
- Books.
- Categories.
- Ebook Library.
- Orders.
- Notifications.
- Account.
- Cart.

Admin navigation should include:

- Dashboard.
- Books.
- Orders.
- Reviews.
- Notifications.
- Settings.

Define clear navigation links between:

- Home to Catalog.
- Catalog/Search to Book Detail.
- Book Detail to Cart.
- Cart to Address & Payment.
- Address & Payment to Checkout or Order Confirmation.
- Checkout to Order Confirmation.
- Order Confirmation to Order History.
- Order Confirmation to Ebook Library.
- Account Dashboard to Orders, Ebook Library, and Notifications.
- Admin Dashboard to Book Management and Order Management.

### 3.11 Component Consistency

Create reusable Figma components for:

- Header.
- Footer.
- Navigation menu.
- Book card.
- Search bar.
- Filter panel.
- Sort dropdown.
- Buttons.
- Form fields.
- Checkbox or toggle.
- Rating stars.
- Cart item row.
- Order summary.
- Notification item.
- Admin table.
- Status badge.
- Modal/dialog.
- Empty state.
- Error state.
- Success state.

The footer must appear on every desktop page as a footer band with a light background and top border. It must show the centered text: **© 2026 Bookbloom.org. All Rights Reserved**. The footer must sit below the page content and must not overlap text, cards, or other content above it.

### 3.12 Design Style Guidance

Use a clean, modern ecommerce layout.

The design should feel:

- Trustworthy.
- Easy to browse.
- Comfortable for reading.
- Suitable for a broad bookstore audience.
- Simple enough for first-version development.

Maintain consistency in:

- Typography.
- Button styles.
- Form layouts.
- Spacing.
- Card layouts.
- Table layouts.
- Icons.
- Error and success messages.

Use the same typography scale across all customer-facing desktop screens:

- Font family: Inter.
- Brand: 22px bold.
- Page and hero titles: 38px bold.
- Section headings: 32px bold.
- Panel headings such as Filters, Payment, Shipping address, and Order Summary: 24px bold.
- Body copy and form input values: 16px regular.
- Book/card titles: 16px semi-bold.
- Navigation, prices, ratings, buttons, and form labels: 14px.
- Secondary metadata such as authors and search placeholder text: 13px.
- Small metadata such as format labels: 12px.
- Footer text: 13px regular.

### 3.13 Responsive Web Layout Requirements

Use standard web layout definitions aligned with Tailwind CSS defaults. Safe defaults should be used unless a later design system says otherwise.

Recommended breakpoints:

| Viewport | Tailwind Breakpoint | Intended Use |
| --- | --- | --- |
| Mobile | Default / below 640px | Single-column browsing, account, cart, and checkout flows |
| Small | `sm` / 640px and up | Larger mobile and small tablet refinements |
| Medium | `md` / 768px and up | Tablet layout with wider forms and two-column opportunities |
| Large | `lg` / 1024px and up | Primary desktop web layout |
| Extra Large | `xl` / 1280px and up | Wide desktop layout with comfortable content width |
| 2XL | `2xl` / 1536px and up | Large monitor layout with constrained content, not stretched full width |

Layout rules:

- Use desktop web as the Figma layout for MVP screens.
- Do not create separate tablet or mobile Figma frames in the MVP design pass.
- Provide clearly labeled responsive notes for mobile and tablet behavior where useful.
- Use a centered content container on desktop with safe max widths, such as `max-w-7xl` for catalog/admin pages and narrower containers for forms.
- Use standard Tailwind-style spacing rhythm such as `4`, `6`, `8`, `10`, `12`, and `16` spacing units.
- Use consistent page gutters: 16px on mobile, 24px on tablet, and 32px or more on desktop.
- Avoid horizontal scrolling on standard web viewports.
- Ensure right and left page margins are visually balanced.
- Ensure text, buttons, cards, forms, tables, images, and badges do not overlap.
- Ensure content is not unintentionally truncated.
- Use wrapping, larger containers, or responsive rearrangement when content does not fit.

### 3.14 Book Cover And Image Requirements

Use real published book cover images in the Figma design to make the bookstore feel practical and realistic.

Image rules:

- Book covers should use realistic image proportions.
- Text should not be placed directly over detailed cover art unless the image is darkened or the text is placed in a separate readable container.
- Cover images must not overlap book titles, prices, format badges, ratings, or action buttons.
- Book card layouts should reserve fixed image space so cards remain aligned across rows.
- Use object-fit behavior equivalent to `cover` or `contain` consistently.
- Use cover images from publicly accessible sources where possible.
- Do not use generated text-heavy cover art that causes overlap or readability issues.
- If a cover image cannot be loaded during generation, use a clean temporary placeholder without text overlap and mark it as replaceable.

### 3.15 Minimum Figma Deliverable

The Figma file should include:

1. Customer-facing screen designs.
2. Admin screen designs.
3. Main user flow connections.
4. Reusable component library.
5. Form and validation states.
6. Empty states.
7. Success and confirmation states.
8. Desktop web layouts for all MVP customer and admin screens.
9. Mobile and tablet responsive behavior notes for key customer screens, without separate mobile/tablet Figma frames.
10. Tailwind-aligned breakpoint, margin, gutter, and spacing guidance.
11. Real published book cover imagery without text overlap.
12. Layout QA showing there is no horizontal scroll, content overlap, or unintended truncation.
13. Static homepage promotional section with clear merchandising content, larger real book imagery, and no carousel behavior.
14. Featured Books carousel with real book cards, carousel navigation controls, and a visible `See all` link.
