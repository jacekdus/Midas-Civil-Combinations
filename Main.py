from App.Application import Application
from Input import main_comb
# from Input_WGP11P import str_comb, ch_comb, fr_comb, qp_comb, acc_comb
from App.Utils import merge_mct_command_files

app = Application(main_comb)

app.create_mct_command_file()
app.create_log_file()

# This line of code merges txt files in ./Output directory:
# merge_mct_command_files()
