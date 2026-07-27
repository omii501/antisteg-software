import os


def load_file(file_path):
    """
    Validates file and returns basic file information.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist")

    file_info = {
        "path": file_path,
        "size": os.path.getsize(file_path),
        "extension": os.path.splitext(file_path)[1].lower()
    }

    return file_info
