import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def replace_in_file(path: pathlib.Path, old: str, new: str) -> None:
    text = path.read_text()
    text = re.sub(old, new, text)
    path.write_text(text)


def main() -> None:
    if ROOT.name == "golden-template-python":
        print(
            "\n⚠️  This looks like the template repository.\n"
            "Clone it into a new project folder before running this script.\n"
            "Example:\n"
            "git clone <repo> my-new-project\n"
            "cd my-new-project\n"
            "python scripts/init_project.py\n"
        )
        sys.exit(1)

    project_name = input("New project name (package name): ").strip()
    cli_name = input("CLI command name: ").strip()

    if not project_name or not cli_name:
        print("Project name and CLI name are required.")
        return

    pyproject = ROOT / "pyproject.toml"
    readme = ROOT / "README.md"

    replace_in_file(pyproject, r'name = "golden-template-python"', f'name = "{project_name}"')
    replace_in_file(pyproject, r'golden-template = "app.cli:main"', f'{cli_name} = "app.cli:main"')

    replace_in_file(readme, r"Golden Template Python", project_name)

    print("\n✅ Project initialized successfully!")
    print(f"Project name: {project_name}")
    print(f"CLI command: {cli_name}")


if __name__ == "__main__":
    main()
