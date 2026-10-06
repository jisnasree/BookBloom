# Cart Requirements

## Scope

This document describes the desktop Shopping Cart screen in the [BookBloom Figma file](https://www.figma.com/design/CMaYhdVPa2mBS0diJ57KGm/BookBloom?node-id=437-3).

## Cart screen

- Show the shared site header and a Shopping Cart page title and subtitle.
- List each cart item with its cover, title, author, selected `PhysicalVariant` format, availability, quantity, current price, and a remove control.
- Show a crossed-out original price when one is available for the item.
- Let the customer change item quantities and apply them with **Update cart**.
- Provide **Empty cart** to remove all items and **Continue shopping** to return to the catalog.
- Show an order summary with subtotal, estimated shipping, and total.
- Show a secure-checkout message and accepted payment-method marks (Visa, Mastercard, American Express, and PayPal).
- Provide **Checkout** to proceed to the checkout flow.
- Display an empty-cart state when there are no items.

## Behavior and rules

- Cart operations require an authenticated customer. Each customer can access only their own cart.
- The cart contains physical variants (paperback or hardcover); identical variants are consolidated into one line.
- Quantity must be at least 1 and cannot exceed currently available stock. Stock and price are checked again during checkout.
- The server supplies prices and calculates line totals, subtotal, estimated shipping, and total. Never accept a price or total from the client.
- Show currency in INR. Shipping is free under the current store policy; the final payable order total is recalculated during checkout.
- Removing an item updates the cart summary. Emptying the cart removes all cart lines.
- Checkout is a separate flow; the cart screen does not create or confirm an order.

## Not specified by the screen

Anonymous carts, cart expiration, discount eligibility, inventory reservation, and behavior when a displayed price changes are not defined by this screen. Cart contents are not purchase-time price records.
