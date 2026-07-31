#!/usr/bin/env bash
# Detect what a project exposes, to drive the docs IA and reference tab.
# Prints one line per detected surface: cli, mcp, api, existing-docs.
# Usage: detect-project-type.sh [project-root]   (defaults to cwd)
set -euo pipefail

root="${1:-.}"
cd "$root"

found=0

note() {
  echo "$1"
  found=1
}

# Existing docs (don't clobber).
if [ -d docs-mintlify ] || [ -f docs-mintlify/docs.json ]; then
  note "existing-docs: docs-mintlify/ already present"
fi

# CLI entry point.
if grep -qE '\[project\.scripts\]|console_scripts' pyproject.toml 2>/dev/null; then
  note "cli: pyproject console script"
elif [ -f package.json ] && grep -q '"bin"' package.json 2>/dev/null; then
  note "cli: package.json bin"
fi

# MCP server.
if grep -rqsE 'FastMCP|modelcontextprotocol|mcp\.server|@modelcontextprotocol' \
  --include='*.py' --include='*.ts' --include='*.js' \
  src 2>/dev/null; then
  note "mcp: MCP server module detected"
fi

# HTTP API (OpenAPI spec).
if [ -f openapi.json ] || [ -f openapi.yaml ] || [ -f openapi.yml ]; then
  note "api: OpenAPI spec present"
elif grep -rqs 'openapi' docs-mintlify/docs.json 2>/dev/null; then
  note "api: docs.json references openapi"
fi

if [ "$found" -eq 0 ]; then
  echo "none: no CLI/MCP/API surface auto-detected; ask the user"
fi
