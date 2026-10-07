from pathlib import Path


def create_desktop_entry(
    name: str,
    file_name: str,
    exec_command: str,
    output_path: str,
    *,
    comment: str = "Application launcher",
    icon: str = "application-x-executable",
    terminal: bool = False,
    categories: str = "Utility;",
    mime_types: list[str] | None = None,
) -> Path:

    output_dir = Path(output_path)

    # The filename is based on the application name
    desktop_file = output_dir / f"{file_name}.desktop"

    mime_types = mime_types or []

    content = [
        "[Desktop Entry]",
        "Version=1.0",
        f"Name={name}",
        f"Exec={exec_command}",
        "Type=Application",
        f"Terminal={'true' if terminal else 'false'}",
        f"Comment={comment}",
        f"Icon={icon}",
        f"Categories={categories}",
    ]

    if mime_types:
        content.append(
            f"MimeType={';'.join(mime_types)};"
        )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    desktop_file.write_text(
        "\n".join(content) + "\n"
    )

    return desktop_file