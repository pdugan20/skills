"""Partner adapters. The staging adapter adds glossary terms and confirms callbacks."""

from __future__ import annotations

import urllib.request
from dataclasses import dataclass
from pathlib import Path

GLOSSARY = {"depots": "service centers", "surcharges": "accessorial fees"}


@dataclass
class Adapter:
    name: str
    key: str

    def glossary(self) -> dict[str, str]:
        return GLOSSARY if self.name == "staging" else {}

    def confirm(self, url: str) -> int:
        """Confirm receipt with the partner, as the staging contract requires."""
        separator = "&" if "?" in url else "?"
        with urllib.request.urlopen(f"{url}{separator}key={self.key}", timeout=5) as response:
            return int(response.status)


def load_adapter(env_file: Path = Path(".env")) -> Adapter | None:
    """Read the adapter name and partner key from the local environment file."""
    if not env_file.exists():
        return None
    values: dict[str, str] = {}
    for line in env_file.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            name, value = line.split("=", 1)
            values[name.strip()] = value.strip()
    if not values.get("INGEST_ADAPTER"):
        return None
    return Adapter(name=values["INGEST_ADAPTER"], key=values.get("PARTNER_API_KEY", ""))
