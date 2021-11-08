from App.Application import Application
from Input import main_comb

app = Application(main_comb)
app.create_mct_command_file()
app.create_log_file()
