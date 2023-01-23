import argparse
import typing as t
from pathlib import Path


def process_file(file: Path) -> None:
    """Replace all instances of `"good"` in the provided source with `"gouda"`."""
    src = file.read_text()

    # Instead of trying to be clever while matching case, just replace twice
    src = src.replace("good", "gouda").replace("Good", "Gouda")

    file.write_text(src)


def main(argv: t.Optional[t.Sequence[str]] = None) -> None:  # pragma: no cover  # noqa: D103
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", type=Path)
    args = parser.parse_args(argv)

    for file in args.filenames:
        process_file(file)


if __name__ == "__main__":
    main()
