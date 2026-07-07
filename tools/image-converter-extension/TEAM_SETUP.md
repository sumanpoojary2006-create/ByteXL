# Team Setup

## Admin

1. Deploy the backend in `../image-converter`.
2. Set the backend environment variable:

```text
BYTEXL_UPLOAD_TOKEN=<your ByteXL bearer token>
```

3. Share the backend URL with teammates, for example:

```text
https://image-converter-pi-rouge.vercel.app
```

4. The current extension already points to:

```text
https://image-converter-pi-rouge.vercel.app
```

5. Share this extension folder or the packaged ZIP.

## Teammates

1. Unzip the extension package.
2. Open `chrome://extensions`.
3. Enable **Developer mode**.
4. Click **Load unpacked**.
5. Select the unzipped `image-converter-extension` folder.
6. Click the extension icon.
7. Choose a ZIP and click **Convert & Download**.

Teammates never need the ByteXL token.

## Hosting Note

For large course ZIP files, prefer Render, Railway, Fly, or another normal web service. Vercel Functions have a 4.5 MB request/response payload limit.
