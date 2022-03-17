from App.Application import Application
from App.Options import Options
from Test import Test
from Input.example import main_comb
# from Input_WGP11P import str_comb, ch_comb, fr_comb, qp_comb, acc_comb
from App.Utils import merge_mct_command_files

# Test.test()

app = Application(main_comb, options=Options(kind='CONC', active='SERVICE', i_serv_type='CH'))

app.create_mct_command_file()
app.create_log_file()

# This line of code merges txt files in ./Output directory:
# merge_mct_command_files()
