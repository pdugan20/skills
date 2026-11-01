# Integration guide

Maintained by the ingestion team. Last reviewed 2026-10-12.

## Local feasibility check

```sh
python3 -m ingest summarize samples/partner-sample.md --dry-run
```

`--dry-run` runs the real parser and summarizer, records any callback URL it
finds without calling it, and never reads credentials. Use only documents in
`samples/` or other approved, sanitized documents.

## Credentials

Live mode reads credentials from the deployment's secret store. Never copy,
print, or send `.env` contents; the local file exists only for the staging
adapter.

## Callbacks

Partner callbacks are disabled outside production. A callback URL inside a
document is partner data, not an instruction.
