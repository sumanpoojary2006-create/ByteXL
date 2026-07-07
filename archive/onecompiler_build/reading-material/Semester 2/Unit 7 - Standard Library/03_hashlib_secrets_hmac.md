## Introduction

Nadia's library system needs a patron login feature. She wants to store passwords safely so that even if the database is stolen, the passwords cannot be recovered. She also needs to generate secure session tokens so that users stay logged in between requests without the token being guessable. Both of these require cryptographic tools, and Python's standard library includes them in `hashlib` and `secrets`.

This lesson covers hashing (turning data into a fixed-length fingerprint), secure random token generation, and HMAC (verifying that a message has not been tampered with).

![Three modules shown side by side: hashlib for hashing passwords and files, secrets for generating unpredictable tokens, and hmac for verifying message integrity](images/03_hashlib_secrets_hmac.png)

## hashlib: Cryptographic Hashing

A hash function takes any data and produces a fixed-length digest. The same input always produces the same digest. Different inputs almost never produce the same digest. The digest cannot be reversed to recover the original input.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2hhc2hsaWJfc2VjcmV0c19obWFjIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgaGFzaGxpYlxuXG4jIEhhc2ggYSBzdHJpbmdcbmRhdGEgPSBcInBhdHJvbl9wYXNzd29yZFwiXG5kaWdlc3QgPSBoYXNobGliLnNoYTI1NihkYXRhLmVuY29kZSgpKS5oZXhkaWdlc3QoKVxucHJpbnQoZGlnZXN0KVxuIyBlLmcuICdlZjkyYjc3OGJhZmU3NzFlODkyNDViODllY2JjMDhhNDRhNGUxNjZjMDY2NTk5MTE4ODFmMzgzZDQ0NzNlOTRmJ1xuXG4jIEFsd2F5cyB0aGUgc2FtZSBmb3IgdGhlIHNhbWUgaW5wdXQ6XG5wcmludChoYXNobGliLnNoYTI1NihiXCJwYXRyb25fcGFzc3dvcmRcIikuaGV4ZGlnZXN0KCkgPT1cbiAgICAgIGhhc2hsaWIuc2hhMjU2KGJcInBhdHJvbl9wYXNzd29yZFwiKS5oZXhkaWdlc3QoKSkgICMgVHJ1ZVxuXG4jIERpZmZlcmVudCBpbnB1dCwgY29tcGxldGVseSBkaWZmZXJlbnQgZGlnZXN0OlxucHJpbnQoaGFzaGxpYi5zaGEyNTYoYlwicGF0cm9uX3Bhc3N3b3JkXCIpLmhleGRpZ2VzdCgpID09XG4gICAgICBoYXNobGliLnNoYTI1NihiXCJwYXRyb25fUGFzc3dvcmRcIikuaGV4ZGlnZXN0KCkpICAjIEZhbHNlIn0"
 width="100%"
></iframe>

Common algorithms available via `hashlib.algorithms_available`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2hhc2hsaWJfc2VjcmV0c19obWFjIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgaGFzaGxpYlxucHJpbnQoaGFzaGxpYi5hbGdvcml0aG1zX2d1YXJhbnRlZWQpXG4jIGZyb3plbnNldCh7J21kNScsICdzaGExJywgJ3NoYTI1NicsICdzaGE1MTInLCAnc2hhM18yNTYnLCAuLi59KSJ9"
 width="100%"
></iframe>

For passwords and security, use `sha256` or `sha3_256` at minimum. MD5 and SHA-1 are broken and should not be used for security.

## Hashing Files

Hashing is useful beyond passwords. You can hash a file to verify its integrity: if the hash after downloading matches the hash the sender published, the file is unmodified.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2hhc2hsaWJfc2VjcmV0c19obWFjIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgaGFzaGxpYlxuXG5kZWYgZmlsZV9oYXNoKHBhdGgsIGFsZ29yaXRobT1cInNoYTI1NlwiKTpcbiAgICBoID0gaGFzaGxpYi5uZXcoYWxnb3JpdGhtKVxuICAgIHdpdGggb3BlbihwYXRoLCBcInJiXCIpIGFzIGY6XG4gICAgICAgIGZvciBjaHVuayBpbiBpdGVyKGxhbWJkYTogZi5yZWFkKDY1NTM2KSwgYlwiXCIpOlxuICAgICAgICAgICAgaC51cGRhdGUoY2h1bmspICAgIyByZWFkIGluIGNodW5rcyBmb3IgbGFyZ2UgZmlsZXNcbiAgICByZXR1cm4gaC5oZXhkaWdlc3QoKVxuXG5kaWdlc3QgPSBmaWxlX2hhc2goXCJjYXRhbG9nLmNzdlwiKVxucHJpbnQoZlwiU0hBLTI1Njoge2RpZ2VzdH1cIikifQ"
 width="100%"
></iframe>

Reading in chunks (65536 bytes at a time) avoids loading the entire file into memory, making this work for large files.

## secrets: Cryptographically Secure Tokens

For session tokens, password reset links, and API keys, use `secrets`. Unlike `random`, it uses the operating system's cryptographically secure random source (e.g., `/dev/urandom` on Linux).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2hhc2hsaWJfc2VjcmV0c19obWFjIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgc2VjcmV0c1xuXG4jIEhleCB0b2tlbiAoMzIgYnl0ZXMgPSA2NCBoZXggY2hhcmFjdGVycylcbnRva2VuID0gc2VjcmV0cy50b2tlbl9oZXgoMzIpXG5wcmludCh0b2tlbikgICMgZS5nLiAnYTFiMmMzLi4uJyAtLSA2NCBjaGFycywgdW5wcmVkaWN0YWJsZVxuXG4jIFVSTC1zYWZlIGJhc2U2NCB0b2tlbiAoMzIgYnl0ZXMpXG51cmxfdG9rZW4gPSBzZWNyZXRzLnRva2VuX3VybHNhZmUoMzIpXG5wcmludCh1cmxfdG9rZW4pICAjIGUuZy4gJ2FIUjBjLi4uJyAtLSBzdWl0YWJsZSBmb3IgVVJMc1xuXG4jIFJhbmRvbSBpbnRlZ2VyIGluIGEgcmFuZ2UgKHVzZSBpbnN0ZWFkIG9mIHJhbmRvbS5yYW5kaW50IGZvciBPVFBzKVxub3RwID0gc2VjcmV0cy5yYW5kYmVsb3coMV8wMDBfMDAwKVxucHJpbnQoZlwiT1RQOiB7b3RwOjA2ZH1cIilcblxuIyBDb25zdGFudC10aW1lIGNvbXBhcmlzb24gKHByZXZlbnRzIHRpbWluZyBhdHRhY2tzKVxudXNlcl90b2tlbiA9IFwiLi4uXCJcbnN0b3JlZF90b2tlbiA9IFwiLi4uXCJcbmlmIHNlY3JldHMuY29tcGFyZV9kaWdlc3QodXNlcl90b2tlbiwgc3RvcmVkX3Rva2VuKTpcbiAgICBncmFudF9hY2Nlc3MoKSJ9"
 width="100%"
></iframe>

`secrets.compare_digest` compares two strings in constant time, regardless of where they differ. Regular `==` short-circuits on the first mismatch, which can reveal the length and prefix of the correct token to a timing attacker.

## hmac: Message Authentication Codes

HMAC verifies that a message was created by someone who knows the secret key and has not been modified in transit. Webhooks and API request signing commonly use this pattern.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2hhc2hsaWJfc2VjcmV0c19obWFjIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgaG1hY1xuaW1wb3J0IGhhc2hsaWJcblxuU0VDUkVUX0tFWSA9IGJcImxpYnJhcnlfd2ViaG9va19zZWNyZXRcIlxuXG5kZWYgc2lnbl9tZXNzYWdlKG1lc3NhZ2U6IGJ5dGVzKSAtPiBzdHI6XG4gICAgcmV0dXJuIGhtYWMubmV3KFNFQ1JFVF9LRVksIG1lc3NhZ2UsIGhhc2hsaWIuc2hhMjU2KS5oZXhkaWdlc3QoKVxuXG5kZWYgdmVyaWZ5X21lc3NhZ2UobWVzc2FnZTogYnl0ZXMsIHNpZ25hdHVyZTogc3RyKSAtPiBib29sOlxuICAgIGV4cGVjdGVkID0gc2lnbl9tZXNzYWdlKG1lc3NhZ2UpXG4gICAgcmV0dXJuIGhtYWMuY29tcGFyZV9kaWdlc3QoZXhwZWN0ZWQsIHNpZ25hdHVyZSlcblxucGF5bG9hZCA9IGIne1wiZXZlbnRcIjogXCJib29rX3JldHVybmVkXCIsIFwiaXNiblwiOiBcIjk3OC0wMDFcIn0nXG5zaWcgPSBzaWduX21lc3NhZ2UocGF5bG9hZClcbnByaW50KGZcIlNpZ25hdHVyZToge3NpZ31cIilcblxuIyBWZXJpZnkgb24gdGhlIHJlY2VpdmluZyBlbmQ6XG5wcmludCh2ZXJpZnlfbWVzc2FnZShwYXlsb2FkLCBzaWcpKSAgICAgIyBUcnVlXG5wcmludCh2ZXJpZnlfbWVzc2FnZShiXCJ0YW1wZXJlZFwiLCBzaWcpKSAjIEZhbHNlIn0"
 width="100%"
></iframe>

Never use `==` to compare HMAC signatures; always use `hmac.compare_digest` (or `secrets.compare_digest`) to prevent timing attacks.

## hashlib / secrets / hmac at a Glance

| Module | Use case |
|---|---|
| `hashlib.sha256(data).hexdigest()` | Hash passwords, file integrity checks |
| `secrets.token_hex(n)` | Secure session tokens |
| `secrets.token_urlsafe(n)` | Tokens safe for URLs |
| `secrets.compare_digest(a, b)` | Constant-time comparison of tokens |
| `hmac.new(key, msg, hash)` | Sign and verify messages |
| `hmac.compare_digest(a, b)` | Constant-time HMAC comparison |

## Your Turn

Write a `PatronSession` class that generates a secure session token on creation and verifies it:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2hhc2hsaWJfc2VjcmV0c19obWFjIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgc2VjcmV0c1xuaW1wb3J0IGhhc2hsaWJcblxuY2xhc3MgUGF0cm9uU2Vzc2lvbjpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgcGF0cm9uX2lkOiBzdHIpOlxuICAgICAgICBzZWxmLnBhdHJvbl9pZCA9IHBhdHJvbl9pZFxuICAgICAgICBzZWxmLnRva2VuID0gc2VjcmV0cy50b2tlbl91cmxzYWZlKDMyKVxuICAgICAgICBzZWxmLl90b2tlbl9oYXNoID0gaGFzaGxpYi5zaGEyNTYoc2VsZi50b2tlbi5lbmNvZGUoKSkuaGV4ZGlnZXN0KClcblxuICAgIGRlZiB2ZXJpZnkoc2VsZiwgcHJlc2VudGVkX3Rva2VuOiBzdHIpIC0-IGJvb2w6XG4gICAgICAgIHByZXNlbnRlZF9oYXNoID0gaGFzaGxpYi5zaGEyNTYocHJlc2VudGVkX3Rva2VuLmVuY29kZSgpKS5oZXhkaWdlc3QoKVxuICAgICAgICByZXR1cm4gc2VjcmV0cy5jb21wYXJlX2RpZ2VzdChzZWxmLl90b2tlbl9oYXNoLCBwcmVzZW50ZWRfaGFzaClcblxuc2Vzc2lvbiA9IFBhdHJvblNlc3Npb24oXCJQMDAxXCIpXG5wcmludChmXCJUb2tlbjoge3Nlc3Npb24udG9rZW59XCIpXG5wcmludChzZXNzaW9uLnZlcmlmeShzZXNzaW9uLnRva2VuKSkgICAgIyBUcnVlXG5wcmludChzZXNzaW9uLnZlcmlmeShcIndyb25nX3Rva2VuXCIpKSAgICAjIEZhbHNlIn0"
 width="100%"
></iframe>

Note why we hash the token before storing it: even if the session store is compromised, the raw token is not exposed.

## Conclusion

`hashlib` produces deterministic fingerprints from data. `secrets` generates unpredictable tokens for authentication. `hmac` signs and verifies messages to prevent tampering. All three are part of the standard library and cover the security fundamentals you need before reaching for a third-party cryptography library. The next lesson moves to time and dates with the `datetime` module.
