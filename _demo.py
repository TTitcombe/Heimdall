"""
Run pdocs on this repository
"""
import configparser
from pathlib import Path

from pdocs import create_adrs, create_technical_doc, parse_config, update_changelog


if __name__ == "__main__":
    p = Path(__file__).parent

    config_path = p / ".pdocs.ini"
    if not config_path.exists():
        raise RuntimeError(f"Must create a config file at {config_path}")

    config = configparser.ConfigParser()
    config.read(config_path)
    config = parse_config(config)

    doc_dir = p / config["doc_dir"]
    if not doc_dir.exists():
        print(f"Creating {doc_dir}...")
        doc_dir.mkdir()

    if config["docs"]["technical"]:
        print("Making technical doc...")
        create_technical_doc(
            p / config["src"],
            (doc_dir / config["docs"]["technical_name"]).with_suffix(
                ".md"
            ),
            config["issues"],
            config["name"],
            config["description"],
        )

    if config["docs"]["adrs"]:
        adr_dir = doc_dir / config["docs"]["adr_dir"]
        if not adr_dir.exists():
            adr_dir.mkdir()

        print("Making ADRs...")
        create_adrs(adr_dir)

    if config["docs"]["changelog"]:
        print("Updating changelog...")
        update_changelog(p / "CHANGELOG.md")
