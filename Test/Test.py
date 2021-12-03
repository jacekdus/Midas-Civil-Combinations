import filecmp
import os
from pathlib import Path

from App.Application import Application
from App.Config import Config
from .Input.Input_marta import Q_ch_komb
from .Input.Input_WD3_gr1 import G_obl_komb

subjects = [
    Q_ch_komb,
    G_obl_komb
]

config = Config()
config.MCT_COMMAND_FILE_PATH = Path(__file__).parent / 'Output'
config.PRINT_MESSAGES = False


def test():
    for subject in subjects:
        app = Application(subject, config)
        app.create_mct_command_file()

    _compare_prepared_mct_command_files()


def _compare_prepared_mct_command_files():
    messages = []

    for file in os.listdir(config.MCT_COMMAND_FILE_PATH):
        if file.endswith(config.MCT_COMMAND_FILE_SUFFIX):

            output_file_path = config.MCT_COMMAND_FILE_PATH / file
            output_confirmed_file_path = config.MCT_COMMAND_FILE_PATH.parent / 'Output_confirmed' / file

            if not filecmp.cmp(output_file_path, output_confirmed_file_path):
                messages.append('Test failed for: ' + output_file_path.name)

    if len(messages) > 0:
        for msg in messages:
            _print_failed_test_msg(msg)
    else:
        _print_passed_test_msg()


def _print_failed_test_msg(msg):
    WARNING = '\033[93m'
    ENDC = '\033[0m'

    print(WARNING + msg + ENDC)


def _print_passed_test_msg():
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

    print(OKGREEN + 'All tests went well.' + ENDC)
