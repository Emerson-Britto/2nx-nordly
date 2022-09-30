import re
import os


def read_as_binary(filepath, fileFormat=None):
  newfilepath = ""
  if fileFormat:
    newfilepath = re.sub(r'\.\w*$', f".{fileFormat}", filepath)
    os.rename(filepath, newfilepath)
  data = open(newfilepath or filepath, "rb")
  os.remove(newfilepath or filepath)
  return data