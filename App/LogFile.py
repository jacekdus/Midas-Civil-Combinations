import sys
from typing import List

from App.CombinationTree.CombinationTree import CombinationTree
from App.Config import MCT_COMMAND_COMB_LIMIT
from App.Midas.MidasCombination import MidasCombination
from App.Midas.MidasLoadCase import MidasLoadCase
from App.Midas.MidasLoadCaseCollection import MidasLoadCaseCollection


class LogFile:
    def __init__(self, file_name):
        self.file_path = file_name
        self.encoding = 'utf-8'


class CombTreeLogFile(LogFile):
    def __init__(self, file_path, comb_tree):
        LogFile.__init__(self, file_path)
        self.comb_tree: CombinationTree = comb_tree

    def create(self):
        print('Preparing Combination-Tree log file...', flush=True)
        f = open(self.file_path, 'w', encoding=self.encoding)
        original_stdout = sys.stdout  # Save a reference to the original standard output

        sys.stdout = f  # Change the standard output to the file we created.

        self.comb_tree.log_basic_info()
        self.comb_tree.log_tree_structure()

        sys.stdout = original_stdout  # Reset the standard output to its original value
        f.close()
        print('Combination-Tree log file succesfully created.', flush=True)


class MctCommandLogFile(LogFile):
    def __init__(self, file_path, midas_comb_list: List[MidasCombination]):
        LogFile.__init__(self, file_path)
        self.midas_comb_list: List[MidasCombination] = midas_comb_list

    def create(self):
        print('Preparing MCT Command log file...', flush=True)
        f = open(self.file_path, 'w', encoding=self.encoding)
        original_stdout = sys.stdout  # Save a reference to the original standard output

        sys.stdout = f  # Change the standard output to the file we created.

        self._print_mct_command_prefix()

        for midas_comb in self.midas_comb_list:
            midas_comb.print_mct_command_midas_combination()

        self._print_indirect_combinations()

        sys.stdout = original_stdout  # Reset the standard output to its original value
        f.close()
        print('MCT Command log file succesfully created.', flush=True)

    def _print_indirect_combinations(self):
        new_midas_combs = []
        counter = 0
        midas_comb = MidasCombination('MidComb_' + str(counter + 1), midas_load_cases=[])
        for midas_comb in self.midas_comb_list:
            if counter < MCT_COMMAND_COMB_LIMIT:
                midas_load_case = MidasLoadCase('CB', midas_comb.name, 1.00)
                midas_comb.midas_load_cases.append(midas_load_case)
                counter += 1
            else:
                new_midas_combs.append(midas_comb)
                counter = 0

        new_midas_combs.append(midas_comb)

        for midas_comb in new_midas_combs:
            print(midas_comb.print_mct_command_midas_combination())

    @staticmethod
    def _print_mct_command_prefix():
        print('*LOADCOMB    ; Combinations')
        print('; NAME=NAME, KIND, ACTIVE, bES, iTYPE, DESC, iSERV-TYPE, nLCOMTYPE, nSEISTYPE   ; line 1')
        print(';      ANAL1, LCNAME1, FACT1, ...                                               ; from line 2')


class MctCommandLogFileManager:
    def __init__(self, midas_comb_list: List[MidasCombination]):
        self.midas_comb_list: List[MidasCombination] = midas_comb_list

    def create_mct_command_log_file(self, file_path):
        mct_command_log_file = MctCommandLogFile(file_path, self.midas_comb_list)
        mct_command_log_file.create()
