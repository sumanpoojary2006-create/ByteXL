# ByteXL Uploader - Reading Material

Hosted browser app for converting ByteXL reading-material Markdown code blocks into OneCompiler iframes.

This is one standalone tool in the ByteXL Uploader suite. The coding-question uploader remains a separate Vercel project.

## Flow

1. Open the hosted app.
2. Upload a folder, Markdown files, or a ZIP.
3. Click **Generate ZIP**.
4. Download the converted ZIP.
5. Use the converted Markdown in ByteXL.

The app does not read server folders. Files are selected by the user and processed in the browser.

## Deploy To Vercel

From this folder:

```bash
npx vercel --prod
```

After deployment, the app URL will look like:

```text
https://vercel-onecompiler-builder.vercel.app
```

The wrapper URL used in generated iframes will be:

```text
https://vercel-onecompiler-builder.vercel.app/embed.html
```

## Local Preview

```bash
python3 -m http.server 8765
```

Then open:

```text
http://127.0.0.1:8765
```

## Link The Separate Coding Tool

The sidebar links to the separate coding-question uploader at `https://vercel-coding-question-uploader.vercel.app`.

## Important

The generated `/embed.html#...` links are temporary wrapper links. They render a
OneCompiler editor, but they are not saved OneCompiler projects. Final published
reading material should use saved OneCompiler URLs such as:

```text
https://onecompiler.com/embed/python/PROJECT_ID
```

See `../../docs/ONECOMPILER_LINK_STRATEGY.md` for the migration path and audit
command.
