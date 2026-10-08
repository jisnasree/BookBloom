# Account Requirements

## Scope

This module covers the customer account dashboard, profile, saved addresses, and navigation to order history. It is based on the screens on the [06 Account Figma page](https://www.figma.com/design/CMaYhdVPa2mBS0diJ57KGm/BookBloom?node-id=456-2). Order history and order details reuse the [Order module](../order/order-requirements.md); they are not defined as separate account-order behavior here.

## Account Dashboard

- Show the signed-in customer's account entry points: Profile, Orders, Saved Addresses, and Sign out.
- The existing dashboard includes a Recent orders panel. Recent-order presentation is not part of this module's scope; customers use the Order module's order history and detail screens.

## Profile

- Require authentication and show the signed-in customer's name, email address, and account information available to the service.
- Show the account profile and security sections represented in the Figma screen.
- Never show a password, password hash, or authentication token.
- Profile edit and password-change buttons are visual mockups only until corresponding write workflows are approved and specified. Do not imply they save changes.
- Do not allow customers to change server-managed staff permissions or Terms acceptance evidence.

## Saved Addresses

- Require authentication and list only the signed-in customer's saved addresses.
- Show each saved address's label, recipient/customer name, address details, phone number, and default state when available.
- Provide visual actions to add, edit, and remove an address.
- Allow at most one default address per customer. Changing the default must be atomic.
- Validate required address fields, India-only country, and Indian PIN format (`^[1-9][0-9]{5}$`).
- Reject access to an address that is not owned by the caller.
- Address controls shown in Figma are visual mockups, not wired interactions.

## Orders

- Provide a path to the Order module's Order History and Order Details screens.
- Show the order-history data, statuses, and detail behavior defined in the Order module; do not substitute the dashboard's Recent orders preview for order history.
- Restrict order reads to the signed-in customer's own orders.

## Security and data rules

- Profile, saved-address, and order resources require authentication.
- Scope all customer reads and writes to the authenticated user in the data-access layer.
- Do not serialize credentials or sensitive payment data.
- Saved addresses are mutable delivery preferences. Orders must preserve their own immutable shipment-address snapshots.
- Account identity and address examples in Figma are illustrative and are not real customer records.

## Out of scope

- Profile editing, password changes from the Profile screen, account deletion/anonymization, and changing email or phone ownership are not defined by the current account API contract.
- Order placement, payments, shipment updates, cancellation, and refunds remain owned by the Cart/Checkout and Order modules.
