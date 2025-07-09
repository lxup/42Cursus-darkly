# Insecure Cookie

The website sets a cookie `I_am_admin` with the value `68934a3e9455fa72420237eb05902327` which is the encrypted value of `false` in MD5 format. As we are able to set cookies, we can set the value of `I_am_admin` to `true` (hashed in MD5 format: `b326b5062b2f0e69046810717534cb09`) and gain admin access.

# How to prevent it
Use server-side session management to store user roles and permissions. Do not rely on client-side cookies for security-sensitive information. Always validate user roles and permissions on the server side before granting access to admin functionalities. If you need to use cookies, ensure they are signed(JWT, HMAC, etc.), encrypted, and have appropriate flags set (e.g., `HttpOnly`, `Secure`, `SameSite`) to prevent tampering and cross-site scripting attacks.