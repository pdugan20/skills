#!/usr/bin/env node
/** Refresh skills.sh through its supported install-telemetry path. */

import { execFileSync, spawnSync } from "node:child_process";
import { mkdtempSync, readdirSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import process from "node:process";

const repository = "pdugan20/skills";
const cliVersion = "1.5.21";
const ciVariables = [
  "CI",
  "GITHUB_ACTIONS",
  "GITLAB_CI",
  "CIRCLECI",
  "TRAVIS",
  "BUILDKITE",
  "JENKINS_URL",
  "TEAMCITY_VERSION",
];

if (ciVariables.some((name) => process.env[name])) {
  throw new Error(
    "Run this command locally; the Skills CLI disables telemetry in CI.",
  );
}
if (process.env.DISABLE_TELEMETRY || process.env.DO_NOT_TRACK) {
  throw new Error(
    "Skills CLI telemetry is disabled, so skills.sh cannot be refreshed.",
  );
}

const temporaryDirectory = mkdtempSync(
  join(tmpdir(), "pdugan20-skills-sh-refresh-"),
);
const npx = process.platform === "win32" ? "npx.cmd" : "npx";

try {
  execFileSync("git", ["init", "--quiet"], {
    cwd: temporaryDirectory,
    stdio: "inherit",
  });
  execFileSync(
    npx,
    [
      "--yes",
      `skills@${cliVersion}`,
      "add",
      repository,
      "--agent",
      "codex",
      "--skill",
      "*",
      "--copy",
      "--yes",
      "--full-depth",
    ],
    {
      cwd: temporaryDirectory,
      env: process.env,
      stdio: "inherit",
    },
  );

  const installedDirectory = join(temporaryDirectory, ".agents", "skills");
  const installed = readdirSync(installedDirectory, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();
  const local = readdirSync(join(process.cwd(), "skills"), {
    withFileTypes: true,
  })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();

  if (JSON.stringify(installed) !== JSON.stringify(local)) {
    throw new Error(
      `GitHub main does not match this checkout. Installed: ${installed.join(", ")}; local: ${local.join(", ")}`,
    );
  }

  const snapshotCheck = spawnSync(
    "python3",
    [
      "scripts/check_skills_sh.py",
      "--skills-root",
      installedDirectory,
      "--snapshots-only",
      "--no-refresh-guidance",
    ],
    { cwd: process.cwd(), stdio: "inherit" },
  );
  if (snapshotCheck.status !== 0) {
    throw new Error(
      "skills.sh did not replace every stored snapshot; add the stale-file evidence to https://github.com/vercel-labs/skills/issues/780.",
    );
  }

  const pageCheck = spawnSync(
    "python3",
    ["scripts/check_skills_sh.py", "--page-only", "--no-refresh-guidance"],
    {
      cwd: process.cwd(),
      stdio: "inherit",
    },
  );
  if (pageCheck.status !== 0) {
    console.log(
      "Snapshots are current, but the public page may take about two hours to reindex; run `npm run check:skills-sh` later.",
    );
  }
} catch (error) {
  console.error(
    `skills.sh refresh failed: ${error instanceof Error ? error.message : error}`,
  );
  process.exitCode = 1;
} finally {
  rmSync(temporaryDirectory, { recursive: true, force: true });
}
