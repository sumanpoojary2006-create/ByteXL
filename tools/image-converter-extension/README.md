# ByteXL Image Converter Chrome Extension

This is the teammate-safe Chrome extension version of the image converter. It does not ask teammates for a ByteXL token. It sends ZIP files to the team converter backend, and that backend uses the private ByteXL token from its environment.

Current backend:

```text
https://image-converter-pi-rouge.vercel.app
```

## Install locally

1. Open `chrome://extensions`.
2. Turn on **Developer mode**.
3. Click **Load unpacked**.
4. Select this folder:

```text
image-converter-extension
```

## Use

1. Click the extension icon.
2. Choose a ZIP file.
3. Click **Convert & Download**.

The ByteXL token is never stored in the extension. It belongs only on the backend as `BYTEXL_UPLOAD_TOKEN`.

## Admin setup

1. Host `../image-converter` somewhere that supports large uploads, such as Render, Railway, or Fly.
2. Set the backend environment variable:

```text
BYTEXL_UPLOAD_TOKEN=<your ByteXL bearer token>
```

3. If the backend URL changes, update `BACKEND_URL` in `popup.js` and rebuild the extension ZIP.
4. Share this extension folder, or zip it and ask teammates to load it unpacked.

## Notes

- The extension calls only the configured team converter backend.
- The backend calls `https://bytexl.app/api/upload/s3`.
- If the backend token expires, update `BYTEXL_UPLOAD_TOKEN` on the backend. Teammates do not need to change anything.
- If the backend is deployed on Vercel, large ZIP files can fail because Vercel Functions have a 4.5 MB payload limit.
