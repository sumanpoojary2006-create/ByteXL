## Introduction

Nadia's library system needs a patron login feature. She wants to store passwords safely so that even if the database is stolen, the passwords cannot be recovered. She also needs to generate secure session tokens so that users stay logged in between requests without the token being guessable. Both of these require cryptographic tools, and Python's standard library includes them in `hashlib` and `secrets`.

This lesson covers hashing (turning data into a fixed-length fingerprint), secure random token generation, and HMAC (verifying that a message has not been tampered with).

![Three modules shown side by side: hashlib for hashing passwords and files, secrets for generating unpredictable tokens, and hmac for verifying message integrity](images/03_hashlib_secrets_hmac.png)

## hashlib: Cryptographic Hashing

A hash function takes any data and produces a fixed-length digest. The same input always produces the same digest. Different inputs almost never produce the same digest. The digest cannot be reversed to recover the original input.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-03-hashlib-secrets-hmac-001-e4a7172eda.html"
 width="100%"
></iframe>

Common algorithms available via `hashlib.algorithms_available`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-03-hashlib-secrets-hmac-002-253fea5b71.html"
 width="100%"
></iframe>

For passwords and security, use `sha256` or `sha3_256` at minimum. MD5 and SHA-1 are broken and should not be used for security.

## Hashing Files

Hashing is useful beyond passwords. You can hash a file to verify its integrity: if the hash after downloading matches the hash the sender published, the file is unmodified.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-03-hashlib-secrets-hmac-003-0c844600e1.html"
 width="100%"
></iframe>

Reading in chunks (65536 bytes at a time) avoids loading the entire file into memory, making this work for large files.

## secrets: Cryptographically Secure Tokens

For session tokens, password reset links, and API keys, use `secrets`. Unlike `random`, it uses the operating system's cryptographically secure random source (e.g., `/dev/urandom` on Linux).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-03-hashlib-secrets-hmac-004-9fa41e0acc.html"
 width="100%"
></iframe>

`secrets.compare_digest` compares two strings in constant time, regardless of where they differ. Regular `==` short-circuits on the first mismatch, which can reveal the length and prefix of the correct token to a timing attacker.

## hmac: Message Authentication Codes

HMAC verifies that a message was created by someone who knows the secret key and has not been modified in transit. Webhooks and API request signing commonly use this pattern.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-03-hashlib-secrets-hmac-005-612cfc2fd4.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-03-hashlib-secrets-hmac-006-1bb997fb08.html"
 width="100%"
></iframe>

Note why we hash the token before storing it: even if the session store is compromised, the raw token is not exposed.

## Conclusion

`hashlib` produces deterministic fingerprints from data. `secrets` generates unpredictable tokens for authentication. `hmac` signs and verifies messages to prevent tampering. All three are part of the standard library and cover the security fundamentals you need before reaching for a third-party cryptography library. The next lesson moves to time and dates with the `datetime` module.
