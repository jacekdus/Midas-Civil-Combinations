import sys
from typing import List

from App.CombinationTree.CombinationTree import CombinationTree
from App.CombinationTree.LoadCombination import LoadCombination
from App.Converter import Converter
from App.Midas.MidasCombination import MidasCombination


class Application:
    def __init__(self, main_load_combination: LoadCombination):
        self.comb_tree = CombinationTree(main_load_combination)

    def _get_prepared_data(self) -> List[MidasCombination]:
        comb_data = self.comb_tree.get_combination_data()

        return Converter.translate_combination_node_data_to_midas_combination(comb_data, self.comb_tree.name)

    def print_midas_mct_command(self):
        original_stdout = sys.stdout  # Save a reference to the original standard output

        with open('mct_command.txt', 'w', encoding='utf-8') as f:
            sys.stdout = f  # Change the standard output to the file we created.

            self._print_mct_command_prefix()  # Change the standard output to the file we created.

            midas_load_cases = []
            for m_comb in self._get_prepared_data():
                m_comb.print_mct_command()

            sys.stdout = original_stdout  # Reset the standard output to its original value

    def log(self):
        original_stdout = sys.stdout  # Save a reference to the original standard output

        with open('log.txt', 'w', encoding='utf-8') as f:
            sys.stdout = f  # Change the standard output to the file we created.

            self.comb_tree.log()

            sys.stdout = original_stdout  # Reset the standard output to its original value

    @staticmethod
    def _print_mct_command_prefix():
        print('*LOADCOMB    ; Combinations')
        print('; NAME=NAME, KIND, ACTIVE, bES, iTYPE, DESC, iSERV-TYPE, nLCOMTYPE, nSEISTYPE   ; line 1')
        print(';      ANAL1, LCNAME1, FACT1, ...                                               ; from line 2')
