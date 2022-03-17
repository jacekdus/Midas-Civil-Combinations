import os.path
from pathlib import Path

from App.Application import Application
from App.Options import Options
from Test import Test
from Input.example import main_comb
# from Input_WGP11P import str_comb, ch_comb, fr_comb, qp_comb, acc_comb
from App.Utils import merge_mct_command_files

# Test.test()

app = Application(main_comb, options=Options(kind='CONC', active='SERVICE', i_serv_type='CH'))

app.create_mct_command_file(folder_name="WD-555/UN")
app.create_log_file()

# This line of code merges txt files in ./Output directory by default, but you can specify directory path:
# merge_mct_command_files()
# or
# path = Path("C:\\Users\\user\\Desktop\\Programy\\Combinations\\Output\\WD-555\\UN")
# merge_mct_command_files(directory=path)
