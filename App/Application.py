from typing import List

from App.CombinationTree.CombinationTree import CombinationTree
from App.CombinationTree.LoadCombination import LoadCombination
from App.Config import MCT_COMMAND_FILE_PATH, LOG_FILE_PATH
from App.Converter import Converter
from App.GUI.Main import GUI
from App.LogFile import CombTreeLogFile, MctCommandLogFileManager
from App.Midas.MidasCombination import MidasCombination


class Application:
    def __init__(self, main_load_combination: LoadCombination):
        self.comb_tree = CombinationTree(main_load_combination)
        self.comb_name = main_load_combination.name

    def _get_prepared_data(self) -> List[MidasCombination]:
        comb_data = self.comb_tree.get_combination_data()

        return Converter.comb_node_data_to_midas_combination(comb_data, self.comb_tree.name)

    def create_mct_command_file(self):
        file_path = MCT_COMMAND_FILE_PATH / '{}_mct_command.txt'.format(self.comb_name)

        manager = MctCommandLogFileManager(self._get_prepared_data())
        manager.create_mct_command_log_file(file_path)

    def create_log_file(self):
        file_path = LOG_FILE_PATH / '{}_log.txt'.format(self.comb_name)

        log_file = CombTreeLogFile(file_path, self.comb_tree)
        log_file.create()

    @staticmethod
    def launch_gui():
        GUI()
