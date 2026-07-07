# Coding Question Upload Automation

## User Flow

1. Open the hosted **Coding Questions** uploader.
2. Upload the coding-question Excel file.
3. Paste your ByteXL token.
4. Click **Validate**.
5. Review the table.
6. Click **Upload** only when there are no errors.

This tool is part of the ByteXL Uploader suite, but it is a separate app from the reading-material uploader.

## What The Tool Does

- Reads the Excel file in the browser.
- Converts each row into a ByteXL coding question.
- Sends the converted questions to ByteXL validation.
- Shows duplicate questions, missing fields, and other errors before upload.
- Uploads valid questions through ByteXL's batch question API.

## Important Notes

- The token is not saved by the app.
- Validation does not create questions.
- Upload creates questions in ByteXL.
- If ByteXL says a question is a duplicate, the tool blocks that row.
- Blank `bloomTaxonomy` cells are treated as `apply` and shown as warnings.

## Local App

The app is here:

`/Users/suman/Desktop/ByteXL/vercel-coding-question-uploader`

Run locally:

```bash
cd /Users/suman/Desktop/ByteXL/vercel-coding-question-uploader
npm run dev
```

Open:

`http://127.0.0.1:8770`

## Hosted App

Use the production app here:

`https://vercel-coding-question-uploader.vercel.app`

## Vercel Deployment

```bash
cd /Users/suman/Desktop/ByteXL/vercel-coding-question-uploader
npx vercel --prod
```

No environment variables are required.

## Product Linking

Keep the two tools as separate Vercel projects:

- Reading Material: `https://image-converter-pi-rouge.vercel.app`
- Coding Questions: `https://vercel-coding-question-uploader.vercel.app`
