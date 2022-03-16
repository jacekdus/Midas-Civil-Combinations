from typing import List

from App.CombinationTree.CombinationTree import CombinationTree
from App.CombinationTree.LoadCombination import LoadCombination
from App.Converter import Converter
from App.GUI.Main import GUI
from App.LogFile import CombTreeLogFile, MctCommandLogFile
from App.Midas.MidasCombination import MidasCombination
from App.Utils import get_fixed_copy_of_main_comb_with_transferred_down_factors
from App.Validator import Validator
from App.Config import Config


class Application:
    def __init__(self, main_load_combination: LoadCombination, config: Config = Config()):
        self.config = config
        self._validate_main_comb(main_load_combination)
        self.main_load_combination = get_fixed_copy_of_main_comb_with_transferred_down_factors(main_load_combination)
        self.comb_tree = CombinationTree(self.main_load_combination, self.config)

    def _get_prepared_data(self) -> List[MidasCombination]:
        comb_data = self.comb_tree.get_combination_data()

        return Converter.comb_node_data_to_midas_combination(comb_data, self.comb_tree.name, self.config)

    def create_mct_command_file(self, folder_name=None):
        log_file = MctCommandLogFile(self.main_load_combination.name, self._get_prepared_data(), self.config, folder_name)
        log_file.create()

    def create_log_file(self, folder_name=None):
        log_file = CombTreeLogFile(self.main_load_combination.name, self.comb_tree, self.config, folder_name)
        log_file.create()

    @staticmethod
    def launch_gui():
        GUI()

    @staticmethod
    def _validate_main_comb(main_load_combination: LoadCombination):
        validator = Validator()
        validator.validate_comb(main_load_combination)
