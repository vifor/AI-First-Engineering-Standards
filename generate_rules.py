import os
from pathlib import Path

def generate():
    # Rutas
    src_dir = Path("src_rules")
    template_dir = Path("templates")
    output_dir = Path("output")
    
    # Crear carpeta de salida para Cursor si no existe
    cursor_out = output_dir / ".cursor" / "rules"
    cursor_out.mkdir(parents=True, exist_ok=True)

    # Cargar templates
    with open(template_dir / "cursor_template.mdc", "r") as f:
        cursor_tmpl = f.read()

    # Procesar cada regla en src_rules
    rules = {
        "angular": {
            "desc": "Apply Angular 21 Modern Standards (Signals, Resource, Standalone)",
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

    for rule_name, meta in rules.items():
        src_path = src_dir / f"{rule_name}.md"
        if not src_path.exists(): continue

        with open(src_path, "r") as f:
            content = f.read()

        # Generar para Cursor
        final_cursor = cursor_tmpl.replace("{{DESCRIPTION}}", meta["desc"])
        final_cursor = final_cursor.replace("{{GLOBS}}", meta["globs"])
        final_cursor = final_cursor.replace("{{CONTENT}}", content)

        with open(cursor_out / f"{rule_name}.mdc", "w") as f:
            f.write(final_cursor)
            
    print("🚀 Guardrails generados exitosamente en /output")

if __name__ == "__main__":
    generate()