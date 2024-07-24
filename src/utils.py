import os

def list_files(directory):
    """
    List all files in the given directory.
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_file_extension(filename):
    """
    Get the extension of a file.
    """
    return os.path.splitext(filename)[1].lower()

# Add any other utility functions here