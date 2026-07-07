# ByteXL Uploader - Coding Questions

Hosted tool for uploading ByteXL coding-question Excel sheets.

This is one standalone tool in the ByteXL Uploader suite. It is not bundled into the reading-material uploader.

## What It Does

1. Reads a `.xlsx`, `.xls`, or `.csv` file in the browser.
2. Converts each row into ByteXL coding-question JSON.
3. Validates the questions with ByteXL.
4. Uploads valid questions through ByteXL's batch question API.

The ByteXL token is used only for the current browser request. It is not saved.

## Run Locally

```bash
cd /Users/suman/Desktop/ByteXL/vercel-coding-question-uploader
npm run dev
```

Open `http://127.0.0.1:8770`.

## Deploy To Vercel

```bash
cd /Users/suman/Desktop/ByteXL/vercel-coding-question-uploader
npx vercel --prod
```

No environment variables are required.

Production URL:

```text
https://vercel-coding-question-uploader.vercel.app
```

## Link The Reading Tool

The brand link returns to the reading-material uploader at `https://image-converter-pi-rouge.vercel.app`.

## Expected Columns

The app supports the current coding-question template:

- `title`
- `description`
- `explanation`
- `score`
- `status`
- `difficulty`
- `bloomTaxonomy`
- `tags`
- `subjects`
- `topics`
- `subTopics`
- `companies`
- `codingType`
- `language`
- `supportAllLanguages`
- `enablePartialScore`
- `ignoreCase`
- `testcase1_input`, `testcase1_output`
- `testcase2_input`, `testcase2_output`
- `testcase3_input`, `testcase3_output`
- `preloadCode_python`
- `solution_python`
- `hints`

Extra testcase columns like `testcase4_input` and `testcase4_output` are also supported.
