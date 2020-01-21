import os
import re
from datetime import datetime


def get_filesize_megabytes(filename):
    filesize_bytes = os.path.getsize(filename)
    return filesize_bytes / 1E6


def eumetsat_filename_to_datetime(inner_tar_name):
    p = re.compile('^MSG[23]-SEVI-MSG15-0100-NA-(\d*)\.')
    title_match = p.match(inner_tar_name)
    date_str = title_match.group(1)
    return datetime.strptime(date_str, "%Y%m%d%H%M%S")