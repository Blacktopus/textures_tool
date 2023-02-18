from window import *


# global variables
# this shit not works
source_path = r'' # look field1/2
target_path = r''
source_file = '' # look field1_1
get_mode = int()

def read_actions():
    global source_path, target_path, source_file, get_mode
    source_path = r'' + field1.get() # look field1/2
    target_path = r'' + field2.get()
    source_file = field1_1.get() # look field1_1
    get_mode = mode.get()
    #print(f'{source_path},\n{target_path},\n{source_file},\n{get_mode}')