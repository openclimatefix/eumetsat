import os


def get_filesize_megabytes(filename):
    filesize_bytes = os.path.getsize(filename)
    return filesize_bytes / 1E6