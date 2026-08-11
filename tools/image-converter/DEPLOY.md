# ByteXL Content Converter Deployment

## Required environment variable

Set this in your hosting provider before uploading real images or publishing topics to ByteXL:

```text
BYTEXL_UPLOAD_TOKEN=<your ByteXL bearer token>
```

Optional:

```text
BYTEXL_CONTENT_TOKEN=<separate ByteXL bearer token for content updates>
BYTEXL_API_BASE=https://app.bytexl.ai
BYTEXL_READING_ID=44sqshkgw
BYTEXL_UPLOAD_URL=https://app.bytexl.ai/api/upload/s3
ONECOMPILER_WEB_BASE=https://onecompiler.com
FRONTEND_ORIGINS=https://image-converter-pi-rouge.vercel.app
PORT=8000
```

If `BYTEXL_CONTENT_TOKEN` is not set, the app uses `BYTEXL_UPLOAD_TOKEN` for both image uploads and content updates. Keep tokens server-side only.

## Architecture

Vercel is a static frontend host only. It must never run `server.py` or receive
image, assessment, OneCompiler, preview, or product-update requests. The browser
sends those requests directly to the external API configured in `config.js`.

The FastAPI service runs on Render (or another non-Vercel host), where the ByteXL
tokens remain server-side. This removes image payloads and update traffic from
Vercel Fast Origin Transfer.

## Vercel (static frontend only)

Current production deployment:

```text
https://image-converter-pi-rouge.vercel.app
```

1. Push the `image-converter` folder changes to Git.
2. In Vercel, import the connected repository.
3. Set the project Root Directory to `image-converter`.
4. Leave Framework Preset as Vercel-detected/Other. Do not add a Python build or function.
5. Do not add ByteXL tokens to Vercel.
6. Set the external API origin in `config.js`.
7. Deploy.
8. Open `/convert` on the Vercel deployment URL.
9. Convert a small ZIP with Code Editors checked and confirm the output Markdown
   contains `https://onecompiler.com/embed/python/` links for Python blocks.

`vercel.json` contains only static rewrites. There is no Vercel Function entrypoint.

## Render

1. Create a new Web Service.
2. Use `image-converter` as the root directory if this folder is inside a larger repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `python run.py`
5. Add `BYTEXL_UPLOAD_TOKEN` in Environment.
6. Add `FRONTEND_ORIGINS=https://image-converter-pi-rouge.vercel.app`.
7. Health check path: `/healthz`.
8. Update `config.js` if Render assigns a different service URL.

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
