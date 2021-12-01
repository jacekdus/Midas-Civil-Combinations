import sys
from typing import List

from App.CombinationTree.CombinationTree import CombinationTree
from App.Config import MCT_COMMAND_COMB_LIMIT, MCT_COMMAND_FILE_PATH, LOG_FILE_PATH
from App.Midas.MidasCombination import MidasCombination
from App.Midas.MidasLoadCase import MidasLoadCase


class LogFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.encoding = 'utf-8'


class CombTreeLogFile(LogFile):
    def __init__(self, file_path, comb_tree):
        LogFile.__init__(self, LOG_FILE_PATH / '{}_log.txt'.format(file_path))
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
        print('Combination-Tree log file successfully created.', flush=True)


class MctCommandLogFile(LogFile):
    def __init__(self, comb_name, midas_comb_list: List[MidasCombination]):
        LogFile.__init__(self, MCT_COMMAND_FILE_PATH / '{}_mct_command.txt'.format(comb_name))
        self.comb_name = comb_name
        self.midas_comb_list: List[MidasCombination] = midas_comb_list

    def create(self):
        print('Preparing MCT Command log file...', flush=True)
        f = open(self.file_path, 'w', encoding=self.encoding)
        original_stdout = sys.stdout  # Save a reference to the original standard output

        sys.stdout = f  # Change the standard output to the file we created.

        self._print_mct_command_prefix()

        for midas_comb in self.midas_comb_list:
            self._print_mct_command_midas_combination_without_cb(midas_comb)

        self._print_indirect_combinations()

        sys.stdout = original_stdout  # Reset the standard output to its original value
        f.close()
        print('MCT Command log file successfully created.', flush=True)

    def _print_indirect_combinations(self):
        new_midas_combs: List[MidasCombination] = self._prepare_indirect_combinations()

        for index, midas_comb in enumerate(new_midas_combs):
            midas_comb.name = '{}_CB_{}'.format(self.comb_name, index)
            self._print_mct_command_midas_combination_with_cb(midas_comb)

    def _prepare_indirect_combinations(self) -> List[MidasCombination]:
        indirect_midas_combs = []
        new_midas_comb = MidasCombination('', midas_load_cases=[])
        counter = 1
        for midas_comb in self.midas_comb_list:
            if counter < MCT_COMMAND_COMB_LIMIT:
                midas_load_case = MidasLoadCase('CB', midas_comb.name, 1.00)
                new_midas_comb.midas_load_cases.append(midas_load_case)
                counter += 1
            else:
                indirect_midas_combs.append(new_midas_comb)
                new_midas_comb = MidasCombination(''.format(self.comb_name, counter), midas_load_cases=[])
                counter = 1

        indirect_midas_combs.append(new_midas_comb)

        return indirect_midas_combs

    @staticmethod
    def _print_mct_command_prefix():
        print('*LOADCOMB    ; Combinations')
        print('; NAME=NAME, KIND, ACTIVE, bES, iTYPE, DESC, iSERV-TYPE, nLCOMTYPE, nSEISTYPE   ; line 1')
        print(';      ANAL1, LCNAME1, FACT1, ...                                               ; from line 2')

    def _print_mct_command_midas_combination_without_cb(self, midas_comb: MidasCombination):
        self._print_mct_command_basic_combination_info(midas_comb)
        print(end='        ')
        print(*self._get_midas_print_list(midas_comb.midas_load_cases), sep=', ')

    def _print_mct_command_midas_combination_with_cb(self, midas_comb: MidasCombination):
        self._print_mct_command_basic_combination_info(midas_comb)
        print(end='        ')
        print_list = []
        for load_case in midas_comb.midas_load_cases:
            print_list += self._get_load_case_props_list(load_case)
        print(*print_list, sep=', ')

    @staticmethod
    def _print_mct_command_basic_combination_info(mc: MidasCombination):
        print("   NAME={}, {}, {}, {}, {}, {}, {}, {}, {}".format(mc.name, mc.kind, mc.active, mc.b_es,
                                                                  mc.i_type, mc.desc, mc.i_serv_type,
                                                                  mc.n_lcomtype, mc.n_seistype))

    def _get_midas_print_list(self, midas_load_cases: List[MidasLoadCase]) -> List[MidasLoadCase]:
        print_list = []

        unique_names = []
        for m_load_case in self._get_effective_list(midas_load_cases):
            lc_name = m_load_case.lcname
            if lc_name in unique_names:
                # Midas Civil doesnt let have duplicate load cases in a load combination so we need to omit them
                pass
            else:
                print_list += self._get_load_case_props_list(m_load_case)

                unique_names.append(lc_name)

        return print_list

    @staticmethod
    def _get_load_case_props_list(load_case):
        return [load_case.anal, load_case.lcname, load_case.fact]

    @staticmethod
    def _get_effective_list(midas_load_cases: List[MidasLoadCase]) -> List[MidasLoadCase]:
        effective_list = []
        # factor = 1.0
        for lc in midas_load_cases:
            if lc.anal == 'CB':
                # factor *= lc.fact
                pass
            else:
                # lc.fact *= factor
                effective_list.append(lc)
                # factor = 1.0

        return effective_list
