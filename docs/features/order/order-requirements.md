# Order Requirements

## Scope

This module covers customer order history and the details view for one order, based on the [Order Details Figma screen](https://www.figma.com/design/CMaYhdVPa2mBS0diJ57KGm/BookBloom?node-id=449-55) and its related Order History screen.

## Order History

- Show the authenticated customer's previous orders, newest first.
- Each order summary shows its order number, placed date, status, a representative book and edition, order total, and a **View details** action.
- Selecting **View details** opens that order's detail screen.
- Do not show orders belonging to another customer.

## Order Details

- Show the order number, placed date, order status, and delivery estimate/status information when available.
- Show each ordered book's cover, title, author, physical format, quantity, and line price.
- Show the delivery address captured when the order was placed.
- Show safe payment-method information, such as payment method and card brand/last four when available. Never show card credentials.
- Show subtotal, shipping, and total in INR. Shipping is free under the current store policy.
- Show delivery progress from order placement through processing, shipment, and delivery based on shipment status.
- Provide navigation back to Order History and a **Continue shopping** action.

## Behavior and rules

- Both screens require authentication and only return the current customer's orders.
- Order items, prices, and the delivery address are historical snapshots; later catalog, price, or address changes must not rewrite past orders.
- Order/payment confirmation and physical fulfillment are separate: a paid/confirmed order is not necessarily shipped or delivered.
- Order status becomes `CONFIRMED` only after authoritative payment success. The displayed delivery progress comes from the independent shipment status.
- Totals are server-calculated; money is displayed in INR.
- If an order is missing or not owned by the customer, return the same not-found behavior.

## Out of scope

The screen does not define customer cancellation/refund behavior, shipment tracking-provider integration, or a precise delivery-estimate calculation. These require separate product decisions.
