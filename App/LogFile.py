import sys
from typing import List

from App.CombinationTree.CombinationTree import CombinationTree
from App.Midas.MidasCombination import MidasCombination


class LogFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.encoding = 'utf-8'


class CombTreeLogFile(LogFile):
    def __init__(self, file_name, comb_tree):
        LogFile.__init__(self, file_name)
        self.comb_tree: CombinationTree = comb_tree

    def log(self):
        print('Preparing Combination-Tree log file...', flush=True)
        f = open(self.file_name, 'w', encoding=self.encoding)
        original_stdout = sys.stdout  # Save a reference to the original standard output

        sys.stdout = f  # Change the standard output to the file we created.

        self.comb_tree.log_basic_info()
        self.comb_tree.log_tree_structure()

        sys.stdout = original_stdout  # Reset the standard output to its original value
        f.close()
        print('Combination-Tree log file succesfully created.', flush=True)


class MctCommandLogFile(LogFile):
    def __init__(self, file_name, midas_comb_list: List[MidasCombination]):
        LogFile.__init__(self, file_name)
        self.midas_comb_list: List[MidasCombination] = midas_comb_list

    def log(self):
        print('Preparing MCT Command log file...', flush=True)
        f = open(self.file_name, 'w', encoding=self.encoding)
        original_stdout = sys.stdout  # Save a reference to the original standard output

        sys.stdout = f  # Change the standard output to the file we created.

        self._print_mct_command_prefix()

        for midas_comb in self.midas_comb_list:
            midas_comb.print_mct_command_midas_combination()

        sys.stdout = original_stdout  # Reset the standard output to its original value
        f.close()
        print('MCT Command log file succesfully created.', flush=True)

    @staticmethod
    def _print_mct_command_prefix():
        print('*LOADCOMB    ; Combinations')
        print('; NAME=NAME, KIND, ACTIVE, bES, iTYPE, DESC, iSERV-TYPE, nLCOMTYPE, nSEISTYPE   ; line 1')
        print(';      ANAL1, LCNAME1, FACT1, ...                                               ; from line 2')
