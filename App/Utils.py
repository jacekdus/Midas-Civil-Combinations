import copy
import os

from App.CombinationTree.LoadCombination import LoadCombination
from App.Config import Config


def merge_mct_command_files(config: Config = Config()):
    if os.path.exists(config.MCT_COMMAND_SUMMARY_FILE_PATH):
        os.remove(config.MCT_COMMAND_SUMMARY_FILE_PATH)
        print('Erased old SUMMARY.txt file')

    print('Merging mct command files...')
    for file in os.listdir(config.MCT_COMMAND_FILE_PATH):
        if file.endswith(config.MCT_COMMAND_FILE_SUFFIX):
            file_path = config.MCT_COMMAND_FILE_PATH / file
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f1:
                    for line in f1:
                        with open(config.MCT_COMMAND_SUMMARY_FILE_PATH, 'a') as f2:
                            f2.write(line)

    print('Merge completed.')


def get_fixed_copy_of_main_comb_with_transferred_down_factors(main_comb: LoadCombination):
    main_comb = copy.deepcopy(main_comb)

    for idx, lc_f in enumerate(main_comb.load_cases):
        lc_f = main_comb.load_cases[idx] = copy.deepcopy(lc_f)
        _transfer_factor_to_next(lc_f)

    return main_comb


def _transfer_factor_to_next(lc_f):
    if lc_f[0].__class__.__name__ == 'LoadCase':
        pass
    else:
        for idx, lc_f_2 in enumerate(lc_f[0].load_cases):
            # Override reference with new [LoadCase, factor]
            lc_f_2 = lc_f[0].load_cases[idx] = copy.deepcopy(lc_f_2)

            # Transfer factor to [LoadCase, factor] list
            # print(str(lc_f_2[0].name) + ': ' + str(lc_f_2[1]) + ' * ' + str(lc_f[1]) + ' = ' + str(lc_f_2[1] * lc_f[1]))
            lc_f_2[1] *= lc_f[1]
            _transfer_factor_to_next(lc_f_2)
