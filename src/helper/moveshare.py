from pathlib import Path
import shutil


def copy_to_local_share(
    app_name: str,
    file: str,
) -> Path:

    share_dir = Path("~/.local/share").expanduser()
    app_dir = share_dir / app_name
    source = Path(file).expanduser()

    app_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = app_dir / source.name

    if source.is_dir():
        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True
        )
    else:
        shutil.copy2(
            source,
            destination
        )

    return destination