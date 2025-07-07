# Insecure Cookie

The website sets a cookie `I_am_admin` with the value `68934a3e9455fa72420237eb05902327` which is the encrypted value of `true` in MD5 format. As we are able to set cookies, we can set the value of `I_am_admin` to `true` (hashed in MD5 format: `b326b5062b2f0e69046810717534cb09`) and gain admin access.