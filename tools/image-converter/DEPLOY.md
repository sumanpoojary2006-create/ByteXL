# ByteXL Content Converter Deployment

## Required environment variable

Set this in your hosting provider before uploading real images or publishing topics to ByteXL:

```text
BYTEXL_UPLOAD_TOKEN=<your ByteXL bearer token>
```

Optional:

```text
BYTEXL_CONTENT_TOKEN=<separate ByteXL bearer token for content updates>
BYTEXL_API_BASE=https://bytexl.app
BYTEXL_READING_ID=44sqshkgw
BYTEXL_UPLOAD_URL=https://bytexl.app/api/upload/s3
ONECOMPILER_WEB_BASE=https://onecompiler.com
PORT=8000
```

If `BYTEXL_CONTENT_TOKEN` is not set, the app uses `BYTEXL_UPLOAD_TOKEN` for both image uploads and content updates. Keep tokens server-side only.

## Vercel

Vercel can deploy this FastAPI app from `server.py`.

Important: Vercel Functions have a request/response payload limit. The hosted page uses a team workflow: choose Images, Code, Upload, or a combination with the top checkboxes; upload one ZIP; then download the updated ZIP or preview and push the updated markdown into ByteXL. It avoids sending the whole ZIP through Vercel by sending images one at a time to `/upload-image`. Direct ByteXL upload sends only markdown text and paths to `/preview-product-upload` first, then `/upload-to-product` after the user confirms in the UI. OneCompiler editor conversion saves code through `/onecompiler/workspace` and writes direct `https://onecompiler.com/embed/<language>/<codeId>` links into the markdown. A single oversized image can still fail and should be compressed or handled by a non-Vercel backend.

Current production deployment:

```text
https://image-converter-pi-rouge.vercel.app
```

1. Push the `image-converter` folder changes to Git.
2. In Vercel, import the connected repository.
3. Set the project Root Directory to `image-converter`.
4. Leave Framework Preset as Vercel-detected/Other.
5. Add Environment Variables:
   - `BYTEXL_UPLOAD_TOKEN`
   - `BYTEXL_CONTENT_TOKEN` if content updates should use a different token
   - `BYTEXL_READING_ID` for the default product shown in Upload mode
   - `BYTEXL_UPLOAD_URL` = `https://bytexl.app/api/upload/s3`
6. Deploy.
7. Open `/convert` on the Vercel deployment URL.
8. Convert a small ZIP with Code Editors checked and confirm the output Markdown
   contains `https://onecompiler.com/embed/python/` links for Python blocks.

Vercel uses `server.py` as the FastAPI entrypoint. `run.py` is only for local development.

## Render

1. Create a new Web Service.
2. Use `image-converter` as the root directory if this folder is inside a larger repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `python run.py`
5. Add `BYTEXL_UPLOAD_TOKEN` in Environment.
6. Health check path: `/healthz`

The included `render.yaml` can also be used as a blueprint when this folder is deployed as the service root.

## Docker

```bash
docker build -t bytexl-image-converter .
docker run --rm -p 8000:8000 -e BYTEXL_UPLOAD_TOKEN="$BYTEXL_UPLOAD_TOKEN" bytexl-image-converter
```

Open:

```text
http://127.0.0.1:8000/convert
```
