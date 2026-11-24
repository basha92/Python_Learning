# This file writes content to the given file location.

from pathlib import Path

class FileManager:

    @staticmethod
    def write_report(file_path, content):

        file_path = Path(file_path)

        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(content, encoding="utf-8")

        print(f"File updated: {file_path}")