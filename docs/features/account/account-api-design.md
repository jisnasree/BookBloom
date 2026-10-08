# Account API Design

Simple authenticated API contract for Profile and Saved Addresses in the [Account Figma screens](./figma/figma.md). Order History and Order Details use the existing [Order API](../order/order-api-design.md); this document does not redefine those endpoints.

**Base path:** `/api/v1`  
**Authentication:** Bearer authentication; customer resources are scoped to the current user.

## Endpoints

| Method and path | Purpose |
|---|---|
| `GET /me` | Return the current customer's safe profile. |
| `GET /addresses` | List the current customer's saved addresses. |
| `POST /addresses` | Create a saved address owned by the current customer. |
| `GET /addresses/{addressId}` | Read one of the current customer's addresses. |
| `PATCH /addresses/{addressId}` | Update mutable fields on one of the current customer's addresses. |
| `DELETE /addresses/{addressId}` | Delete one of the current customer's addresses. |

## Profile

`GET /me` returns `id`, `firstName`, `lastName`, `email`, `termsAcceptedAt`, and read-only `isStaff`, as defined in the shared API contract. It must not return the password hash or credentials.

The Profile screen shows Edit profile and Change password controls, but the current shared contract does not define profile-write or password-change operations. Treat these controls as non-functional mockups until those workflows are separately approved and specified; do not invent or imply a successful update.

## Addresses

Address request fields use camelCase:

- Required on creation: `addressLine1`, `city`, `stateRegion`, `postalCode`, `countryCode: "IN"`, and `phone`.
- Optional: `label`, `company`, `addressLine2`, and `isDefault`.
- `PATCH` accepts one or more mutable address fields and applies the same validation as creation.

Address responses include `id`, `label`, `company`, `addressLine1`, `addressLine2`, `city`, `stateRegion`, `postalCode`, `countryCode`, `phone`, `isDefault`, `createdAt`, and `updatedAt`.

## Validation and errors

- `400 Bad Request`: malformed request, invalid address fields, unsupported country, or invalid PIN.
- `401 Unauthorized`: missing or invalid bearer token.
- `404 Not Found`: address does not exist or is not owned by the caller.
- `GET /addresses` returns an empty list when the customer has no saved addresses.
- Enforce `countryCode = "IN"` and `postalCode` matching `^[1-9][0-9]{5}$`.
- When setting an address as default, unset the previous default in the same transaction.
- Deleting an address must not change a previously placed order's shipment snapshot.
