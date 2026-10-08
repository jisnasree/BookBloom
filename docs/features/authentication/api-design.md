# Authentication API Design

**Scope:** Authentication-only API proposal. Base path: `/api/v1`. JSON uses camelCase. Public error responses must not reveal whether an email address has an account.

## 1. Signup

`POST /auth/register` — Public.

Purpose: Create a new user account.

User enters:
Email
Password
firstName etc.
     ↓
POST /auth/register
     ↓
Backend creates the account
     ↓
Backend sends email OTP

Access: Public — the user is not logged in yet.

Request:

```json
{
  "firstName": "Asha",
  "lastName": "Menon",
  "email": "asha@example.in",
  "password": "example-password",
  "passwordConfirmation": "example-password",
  "termsAccepted": true
}
```

Success: `202 Accepted`

```json
{
  "status": "verification_required",
  "message": "If registration can proceed, a verification code has been sent."
}
```

Common errors: `400` invalid fields/password mismatch/Terms not accepted; `429` rate limit. Avoid disclosing whether an email is already registered; choose a generic signup response policy.

## 2. Login

`POST /auth/login` — Public.

Purpose: Log an existing user into the application.

Email + Password
       ↓
POST /auth/login
       ↓
Backend checks credentials
       ↓
Returns authentication token

Access: Public — you need to be able to log in before you are authenticated.

Request: `{ "email": "asha@example.in", "password": "example-password" }`

Success: `200 OK`

```json
{
  "accessToken": "<opaque-token>",
  "tokenType": "Bearer",
  "expiresAt": "2026-01-01T00:00:00Z",
  "user": {
    "id": "<uuid>",
    "firstName": "Asha",
    "lastName": "Menon",
    "email": "asha@example.in",
    "emailVerifiedAt": "2026-01-01T00:00:00Z",
    "isStaff": false
  }
}
```

Common errors: `400` malformed input; `401` generic invalid credentials or unverified account; `429` rate limit.

## 3. Signup email OTP verification

`POST /auth/register/verify-email` — Public.

Purpose: Verify that the email address used during signup actually belongs to the user.

Signup
  ↓
OTP sent to email
  ↓
User enters OTP
  ↓
POST /auth/register/verify-email
  ↓
Email verified

Access: Public because the user isn't fully authenticated yet.

Request: `{ "email": "asha@example.in", "code": "123456" }`

Success: `200 OK`

```json
{
  "status": "verified",
  "message": "Email address verified."
}
```

Common errors: `400` malformed request; `401` invalid/expired/used code; `404` generic invalid challenge response if needed; `429` attempt limit/rate limit. Whether verification also creates a login session remains undecided.

`POST /auth/register/resend-code` — Public.

Request: `{ "email": "asha@example.in" }`

Success: `202 Accepted` with a generic acknowledgement to avoid account enumeration.

Common errors: `400` malformed request; `429` resend cooldown/rate limit. Exact policy is open.

## 4. Forgot password and reset

`POST /auth/password/forgot` — Public.

Purpose: Start the password-reset process.

User clicks "Forgot Password?"
             ↓
Enters email
             ↓
POST /auth/password/forgot
             ↓
Backend sends reset OTP/code

Access: Public because the user has forgotten their password.

Request: `{ "email": "asha@example.in" }`

Success: `202 Accepted`; return the same generic response whether or not the account exists.

Common errors: `400` malformed request; `429` rate limit.

`POST /auth/password/verify-reset-code` — Public.

Purpose: Check whether the OTP/code entered by the user is correct.

User receives OTP
       ↓
Enters OTP
       ↓
POST /auth/password/verify-reset-code
       ↓
OTP is valid
       ↓
Backend allows password reset

Usually, the backend gives the frontend a short-lived reset token after successful verification.

Request: `{ "email": "asha@example.in", "code": "123456" }`

Success: `200 OK`: `{ "resetToken": "<short-lived-one-time-token>" }`. The token is scoped to password reset and must not be usable as an access token.

Common errors: `400` malformed request; `401` invalid/expired/used code; `429` attempt limit/rate limit.

`POST /auth/password/reset` — Public, requires the reset token.

Purpose: Actually set the user's new password.

New Password
     +
Reset Token
     ↓
POST /auth/password/reset
     ↓
Password changed

This is why your table says:

Public, needs the reset token

The user doesn't need to be logged in, but they must prove they successfully completed the password-reset verification.

Request: `{ "resetToken": "<short-lived-one-time-token>", "newPassword": "...", "passwordConfirmation": "..." }`

Success: `204 No Content`.

Common errors: `400` weak/mismatched password; `401` missing/invalid/expired/used reset token; `429` rate limit.

`POST /auth/password/resend-code` — Public.

Purpose: Send another OTP if the password-reset OTP was not received or expired.

Forgot password
      ↓
OTP not received
      ↓
Resend
      ↓
POST /auth/password/resend-code
      ↓
New OTP sent

Request: `{ "email": "asha@example.in" }`

Success: `202 Accepted` with a generic acknowledgement.

Common errors: `400` malformed request; `429` resend cooldown/rate limit.

## 5. Logout

`POST /auth/logout` — Authenticated.

Purpose: Log the user out.

Logged-in user
      ↓
POST /auth/logout
      ↓
Authentication/session/token is invalidated
      ↓
User is logged out

Access: Authenticated — only a logged-in user should be able to call this endpoint.

Request: no body; bearer token in the Authorization header.

Success: `204 No Content`; revoke the current token/session.

Common errors: `401` missing, expired, or revoked token.

## Shared error example

```json
{
  "code": "validation_error",
  "message": "The request could not be completed.",
  "requestId": "<request-id>",
  "fieldErrors": {
    "code": ["The verification code is invalid or expired."]
  }
}
```
