from App.Application import Application
from Input_test import main_comb

from App.Utils import merge_mct_command_files

app = Application(main_comb)
# app.launch_gui()
app.create_mct_command_file()
app.create_log_file()

# This line of code merges txt files in ./Output directory:
# merge_mct_command_files()

