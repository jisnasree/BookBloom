# BookBloom Authentication Requirements

**Scope:** Authentication only. This feature brief covers customer signup, email verification, login, password recovery, OTP verification and logout. 

## Goal and users

Allow customers to create and securely access an account. Staff use the same login flow; staff authorization is enforced separately through server-managed permissions.

## Requirements

### 1. Signup

- Collect first name, last name, email, password, password confirmation, and explicit Terms & Conditions acceptance.
- Validate fields and matching passwords before creating the account.
- Normalize and enforce unique email addresses.
- Create an unverified account and send a one-time code to the submitted email address.
- Do not grant an authenticated session until email verification succeeds.
- Do not store password confirmation or the OTP in plaintext.

### 2. Login

- Accept email and password.
- Authenticate only verified accounts.
- On success, issue an authenticated session/token and return the safe account profile.
- Use a generic error for invalid credentials; do not disclose whether an email is registered.
- Rate-limit repeated login attempts.

### 3. Email OTP verification

- Verify a signup email using a one-time code sent to that email.
- Verify a forgot-password request using a one-time code sent to the account email.
- A code is single-use, expires, and is limited against guessing and resend abuse.
- Do not reveal account existence in password-recovery or resend responses.
- OTP length, lifetime, retry limit, resend cooldown, and delivery provider require approval before implementation.

### 4. Forgot password

- Let a user request password recovery using their email address.
- Return the same public response whether or not the account exists.
- Send a one-time code only when an eligible account exists.
- After successful OTP verification, allow the user to set and confirm a new password.
- Invalidate outstanding password-reset challenges and applicable sessions after password change; exact session policy must be finalized.

### 5. Logout

- Revoke the current authenticated session/token.
- Return success even if the client subsequently discards its local credential.
- Define token lifetime, refresh behavior, persistence, and revocation implementation before launch.


## User flows

**Signup:** Signup form → submit → email OTP screen → verify → account becomes verified → proceed to login or receive a session (decision pending).

**Login:** Login form → submit credentials → success/session and redirect; otherwise show a generic credential error.

**Password recovery:** Forgot-password form → generic request acknowledgement → email OTP screen → verify code → set new password → success → return to login.

Logout is an account action with a confirmation/feedback state, not necessarily a standalone page. Include loading, invalid/expired OTP, resend cooldown, validation error, and service failure states where applicable.

## Open decisions

- OTP code length, validity period, attempt limit, resend cooldown, and maximum sends.
- Email delivery provider and failure/retry behavior.
- Whether successful signup verification automatically signs the user in.
- Whether login is session-cookie based or bearer-token based; expiration, refresh, persistence, and revocation policy.
- Whether existing sessions are all revoked after password reset.
- Account retention and cleanup policy for unverified signup records.
