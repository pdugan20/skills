import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import {
  copyFileSync,
  cpSync,
  existsSync,
  mkdtempSync,
  mkdirSync,
  readFileSync,
  readdirSync,
  rmSync,
  statSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const sourceSkillsRoot = join(repositoryRoot, "skills");
const agentPluginSchema =
  "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json";
const installationRoot = mkdtempSync(
  join(tmpdir(), "patrick-skills-install-")
);
const npxCommand = process.platform === "win32" ? "npx.cmd" : "npx";

function listFiles(root) {
  const files = [];

  function visit(directory) {
    for (const entry of readdirSync(directory, { withFileTypes: true })) {
      if (entry.name === "__pycache__" || entry.name.endsWith(".pyc")) {
        continue;
      }

      const path = join(directory, entry.name);
      if (entry.isDirectory()) {
        visit(path);
      } else if (entry.isFile() || entry.isSymbolicLink()) {
        files.push(relative(root, path));
      }
    }
  }

  visit(root);
  return files.sort();
}

try {
  execFileSync("git", ["init", "-q", installationRoot]);
  execFileSync(
    npxCommand,
    [
      "--yes",
      "skills@1.5.21",
      "add",
      repositoryRoot,
      "--agent",
      "claude-code",
      "codex",
      "cursor",
      "--skill",
      "*",
      "--copy",
      "--yes",
    ],
    {
      cwd: installationRoot,
      env: { ...process.env, DISABLE_TELEMETRY: "1" },
      stdio: "pipe",
    }
  );

  const skillNames = readdirSync(sourceSkillsRoot)
    .filter((name) => statSync(join(sourceSkillsRoot, name)).isDirectory())
    .sort();

  const portablePluginRoot = join(
    installationRoot,
    "agent-plugins",
    "patrick-skills"
  );
  mkdirSync(portablePluginRoot, { recursive: true });
  copyFileSync(
    join(repositoryRoot, "plugin.json"),
    join(portablePluginRoot, "plugin.json")
  );
  cpSync(sourceSkillsRoot, join(portablePluginRoot, "skills"), {
    recursive: true,
  });

  const portableManifest = JSON.parse(
    readFileSync(join(portablePluginRoot, "plugin.json"), "utf8")
  );
  assert.equal(portableManifest.$schema, agentPluginSchema);
  assert.equal(portableManifest.name, "patrick-skills");
  assert.deepEqual(
    readdirSync(join(portablePluginRoot, "skills"))
      .filter((name) =>
        existsSync(join(portablePluginRoot, "skills", name, "SKILL.md"))
      )
      .sort(),
    skillNames,
    "Portable Agent Plugin did not discover every immediate skill child"
  );

  for (const skillName of skillNames) {
    const sourceFiles = listFiles(join(sourceSkillsRoot, skillName));

    assert.deepEqual(
      listFiles(join(portablePluginRoot, "skills", skillName)),
      sourceFiles,
      `${skillName} resources differ in the portable Agent Plugin package`
    );

    for (const clientRoot of [".claude/skills", ".agents/skills"]) {
      const installedSkill = join(installationRoot, clientRoot, skillName);
      assert.ok(
        existsSync(join(installedSkill, "SKILL.md")),
        `${skillName} was not installed under ${clientRoot}`
      );
      assert.deepEqual(
        listFiles(installedSkill),
        sourceFiles,
        `${skillName} resources differ under ${clientRoot}`
      );
    }
  }

  assert.ok(
    existsSync(join(installationRoot, "skills-lock.json")),
    "Skills CLI did not create skills-lock.json"
  );

  console.log(
    `Installation validation passed for ${skillNames.length} skills across the portable Agent Plugin, Claude Code, Codex, and Cursor packages.`
  );
} finally {
  rmSync(installationRoot, { recursive: true, force: true });
}
