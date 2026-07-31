# ---- docs site (Mintlify, docs-mintlify/) ----
# Append these targets to the product repo's Makefile, and add the names to .PHONY.

# Regenerate the CLI + MCP reference (+ changelog) from source. Run + commit
# after changing the CLI or any MCP tool, or CI ("Docs Reference Freshness")
# fails on drift. Adapt the runner (python / uv run / node) to the project.
docs-reference:
	python scripts/gen_cli_reference.py
	python scripts/gen_mcp_reference.py

# Local docs preview at http://localhost:3000 (needs the Mintlify CLI).
docs:
	cd docs-mintlify && mint dev

# Strictly validate docs.json, MDX, and referenced OpenAPI documents.
docs-validate:
	cd docs-mintlify && mint validate

# Validate internal links, anchors, redirect destinations, and nav.
docs-links:
	cd docs-mintlify && mint broken-links --check-anchors --check-redirects
