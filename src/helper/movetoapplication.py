from pathlib import Path
import shutil


def copy_to_applications(file: str) -> Path:

    applications_dir = (
        Path("~/.local/share/applications").expanduser()
    )

    source = Path(file).expanduser()

    applications_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = applications_dir / source.name

    if destination.exists():
        return destination

    shutil.copy2(
        source,
        destination
    )

    return destination