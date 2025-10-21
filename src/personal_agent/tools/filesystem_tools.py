import os

FOLDER_PATH = os.getenv("FILES_FOLDER_PATH")

def create_file(filename: str, content: str) -> None:
    """
    Write a string to a markdown file in the local filesystem.

    Args:
        filename (str): Name of the file to be created
        content (str): Text to save in the .md file

    Returns:
        None
    """
    file_path = f"{FOLDER_PATH}/{filename}.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    