# OneCompiler Link Strategy

## Problem

Several reading-material editors currently point to a ByteXL-owned wrapper URL,
for example:

```text
https://image-converter-pi-rouge.vercel.app/embed.html#...
```

or to uploaded wrapper HTML on S3:

```text
https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/.../onecompiler-embeds/...html
```

Those links can render a OneCompiler iframe today, but they are not saved
OneCompiler projects. If the wrapper app, Vercel deployment, or uploaded HTML is
removed, the URL no longer tells us where the actual editable code lives.

## Correct Target

For a durable reading-material editor, keep a OneCompiler-owned URL as the
source of truth.

For simple code snippets, the iframe should use a saved OneCompiler code ID:

```html
<iframe
 frameBorder="0"
 height="350px"
 src="https://onecompiler.com/embed/python/PROJECT_ID"
 width="100%"
></iframe>
```

Keep the matching edit/open URL in metadata:

```text
https://onecompiler.com/python/PROJECT_ID
```

## What OneCompiler Supports

OneCompiler documents:

- Editor embeds by language: `https://onecompiler.com/embed/python`
- Editor embeds by saved code ID: `https://onecompiler.com/embed/javascript/3wyne344h`
- Code injection into an embed with `postMessage` and `populateCode`
- Public editor save through `https://onecompiler.com/api/editorx/save`

The current ByteXL wrapper uses the `populateCode` approach. That is fine for a
temporary generated preview, but it does not create or preserve a OneCompiler
project ID by itself.

## Recommended Fix

1. Create a OneCompiler project/workspace for every code editor that appears in
   reading material.
2. Store a manifest with:
   - `source_file`
   - `snippet_id`
   - `language`
   - `code_sha1`
   - `onecompiler_url`
   - `onecompiler_embed_url`
   - `created_at`
   - `updated_at`
3. Rewrite reading-material iframes to use `onecompiler_embed_url`.
4. Keep the manifest under version control or in the content database so future
   edits can find the original OneCompiler project without relying on the app
   URL.
5. Run the audit script before upload and block any reading material that still
   contains wrapper/app URLs.

## Migration Options

### Option A: Manual Saved-Code Migration

Use this when there are only a few affected lessons.

1. Open each generated editor.
2. Save or run the code in OneCompiler until the browser URL has a project ID.
3. Copy the OneCompiler URL.
4. Convert it to the embed URL:
   - editor URL: `https://onecompiler.com/python/abc123`
   - embed URL: `https://onecompiler.com/embed/python/abc123`
5. Replace the reading-material iframe source.

### Option B: Automated Saved-Code Migration

Use this for the ByteXL ZIP converter.

1. Extract each fenced code block from markdown.
2. Call `https://onecompiler.com/api/editorx/save` with `title`,
   `visibility`, and `properties.language/files/stdin`.
3. Store the returned `_id` as `codeId` in the manifest.
4. Use `https://onecompiler.com/embed/<language>/<codeId>` in reading material.
5. Keep `https://onecompiler.com/<language>/<codeId>` in the manifest for
   future review.

### Option C: Keep Wrapper Only As Fallback

If OneCompiler saved links cannot be generated immediately, the wrapper can stay
as a temporary bridge, but it should not be treated as final published content.
At minimum, keep the decoded snippet manifest and S3 wrapper files backed up so
the code can be recovered if the app URL is deleted.

## Audit Command

Run:

```bash
python3 tools/scripts/audit_onecompiler_links.py archive/onecompiler_build/reading-material-uploaded
```

The output classifies iframe sources as durable OneCompiler links, temporary
wrapper links, unsaved generic embeds, or other URLs.
