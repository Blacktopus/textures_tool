import os
from errors import error_codes

def open_help():
    try:
        os.startfile('Help textures tool.txt')
        error_codes()
    except:
        error_codes(5)