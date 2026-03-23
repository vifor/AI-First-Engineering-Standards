import argparse
from pathlib import Path

RULES = {
    "angular": {
        "desc": "Apply Angular Modern Standards (Signals, Resource, Standalone)",
        "globs": "**/*.{ts,html}"
    },
    "git-workflow": {
        "desc": "Guidelines for Git workflow, security checks and manual code verification",
        "globs": "**/*"
    },
    "react-next": {
        "desc": "React & Next.js standards (hydration safety, stable hooks, monorepo tsconfig)",
        "globs": "**/*.{ts,tsx}"
    },
    "aws": {
        "desc": "AWS Lambda, DynamoDB & SAM standards (CORS, TTL, template structure)",
        "globs": "**/*.{ts,yaml,yml}"
    }
}

def generate(rule_names: list[str]):
    src_dir = Path("src_rules")
    template_dir = Path("templates")
    output_dir = Path("output")

    cursor_out = output_dir / ".cursor" / "rules"
    cursor_out.mkdir(parents=True, exist_ok=True)

    with open(template_dir / "cursor_template.mdc", "r") as f:
        cursor_tmpl = f.read()

    with open(template_dir / "claude_instructions.txt", "r") as f:
        claude_tmpl = f.read()

    with open(template_dir / "copilot_template.md", "r") as f:
        copilot_tmpl = f.read()

    claude_sections = []
    copilot_sections = []

    for rule_name in rule_names:
        meta = RULES.get(rule_name)
        if not meta:
            print(f"  ⚠️  Unknown rule '{rule_name}', skipping.")
            continue

        src_path = src_dir / f"{rule_name}.md"
        if not src_path.exists():
            print(f"  ⚠️  File not found: {src_path}, skipping.")
            continue

        with open(src_path, "r") as f:
            content = f.read()

        # Cursor: one .mdc file per rule
        cursor_output = cursor_tmpl.replace("{{DESCRIPTION}}", meta["desc"])
        cursor_output = cursor_output.replace("{{GLOBS}}", meta["globs"])
        cursor_output = cursor_output.replace("{{CONTENT}}", content)
        with open(cursor_out / f"{rule_name}.mdc", "w") as f:
            f.write(cursor_output)

        # Claude: collect sections for a single CLAUDE.md
        claude_sections.append(claude_tmpl.replace("{{CONTENT}}", content))

        # Copilot: collect sections for a single copilot-instructions.md
        copilot_sections.append(copilot_tmpl.replace("{{CONTENT}}", content))

        print(f"  ✅ {rule_name}")

    # Claude: write all collected sections into one CLAUDE.md
    if claude_sections:
        claude_md_path = output_dir / "CLAUDE.md"
        with open(claude_md_path, "w") as f:
            f.write("\n\n---\n\n".join(claude_sections))
        print(f"  📄 CLAUDE.md → {claude_md_path}")

    # Copilot: write all collected sections into .github/copilot-instructions.md
    if copilot_sections:
        copilot_out = output_dir / ".github"
        copilot_out.mkdir(parents=True, exist_ok=True)
        copilot_path = copilot_out / "copilot-instructions.md"
        with open(copilot_path, "w") as f:
            f.write("\n\n---\n\n".join(copilot_sections))
        print(f"  📄 copilot-instructions.md → {copilot_path}")

    print("\n🚀 Done. Copy output/ artifacts into your project.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate AI tool guardrail files from src_rules/."
    )
    parser.add_argument(
        "rules",
        nargs="*",
        help=f"Rule names to generate. Available: {', '.join(RULES)}. Omit to generate all."
    )
    args = parser.parse_args()

    selected = args.rules if args.rules else list(RULES.keys())
    print(f"Generating {len(selected)} rule(s): {', '.join(selected)}\n")
    generate(selected)
