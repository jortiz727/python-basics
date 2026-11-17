from pathlib import Path
import shutil

SOURCE_FOLDER = Path.home() / "Downloads"

def unique_destination(folder, file):
    """Return a path in folder that doesn't exist yet, adding (1), (2)... if needed."""
    target = folder / file.name
    counter = 1
    while target.exists():
        target = folder / f"{file.stem} ({counter}){file.suffix}"
        counter += 1
    return target


def main():
    for file in list(SOURCE_FOLDER.iterdir()):
        if file.is_file():
            extension = file.suffix.lower()
            destination_folder = SOURCE_FOLDER / extension[1:]
            destination_folder.mkdir(exist_ok=True)
            target = unique_destination(destination_folder, file)
            try:
                file.rename(target)
            except OSError as error:
                print(f"Skipped {file.name}: {error.strerror}")
                continue
            print(f"{file.name} -> {destination_folder.name}/{target.name}")

if __name__ == "__main__":
    main()