from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import zipfile


def sha256_of_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_binary(dist_dir: Path, project_name: str) -> Path:
    candidates = [
        dist_dir / f"{project_name}.exe",
        dist_dir / project_name,
    ]

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate

    candidates_display = ", ".join(str(path) for path in candidates)
    raise FileNotFoundError(f"Could not find built binary. Checked: {candidates_display}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create zipped release asset and SHA256 file from PyInstaller output."
    )
    parser.add_argument("--project-name", default="mpm")
    parser.add_argument("--version", required=True)
    parser.add_argument("--platform", required=True)
    parser.add_argument("--dist-dir", default="dist")
    parser.add_argument("--output-dir", default="release")
    parser.add_argument("--extra", action="append", default=["README.md", "LICENSE"])
    args = parser.parse_args()

    dist_dir = Path(args.dist_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    binary_path = find_binary(dist_dir, args.project_name)
    archive_name = f"{args.project_name}-{args.version}-{args.platform}.zip"
    archive_path = output_dir / archive_name

    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(binary_path, arcname=binary_path.name)
        for extra_path in args.extra:
            candidate = Path(extra_path)
            if candidate.exists() and candidate.is_file():
                archive.write(candidate, arcname=candidate.name)

    checksum = sha256_of_file(archive_path)
    checksum_path = output_dir / f"{archive_name}.sha256"
    checksum_path.write_text(f"{checksum}  {archive_name}\n", encoding="utf-8")

    print(f"Archive: {archive_path}")
    print(f"Checksum: {checksum_path}")


if __name__ == "__main__":
    main()
