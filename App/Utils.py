import os

from App.CombinationTree.LoadCombination import LoadCombination
from App.Config import MCT_COMMAND_SUMMARY_FILE_PATH, MCT_COMMAND_FILE_PATH


def merge_mct_command_files():
    if os.path.exists(MCT_COMMAND_SUMMARY_FILE_PATH):
        os.remove(MCT_COMMAND_SUMMARY_FILE_PATH)
        print('Erased old SUMMARY.txt file')

    print('Merging mct command files...')
    for file in os.listdir(MCT_COMMAND_FILE_PATH):
        file_path = MCT_COMMAND_FILE_PATH / file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f1:
                for line in f1:
                    with open(MCT_COMMAND_SUMMARY_FILE_PATH, 'a') as f2:
                        f2.write(line)

    print('Merge completed.')


def fix_main_comb(main_comb: LoadCombination):
    for lc_f in main_comb.load_cases:
        _prepare_comb(lc_f)


def _prepare_comb(lc_f):
    if lc_f[0].__class__.__name__ == 'LoadCase':
        pass
    else:
        for lc_f_2 in lc_f[0].load_cases:
            lc_f_2[1] *= lc_f[1]
            _prepare_comb(lc_f_2)