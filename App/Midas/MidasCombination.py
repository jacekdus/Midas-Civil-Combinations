from typing import List

from App.Midas.MidasLoadCase import MidasLoadCase


class MidasCombination:
    def __init__(self, name, midas_load_cases: List[MidasLoadCase],
                 kind='GEN', active='ACTIVE', b_es=0, i_type=0, desc='', i_serv_type=0, n_lcomtype=0, n_seistype=0):
        self.name = name
        self.kind = kind        # GEN/CONC/STEEL
        self.active = active    # ACTIVE/INACTIVE/STRENGTH/SERVICE
        self.b_es = b_es
        self.i_type = i_type    # If envelop 1, otherwise 0
        self.desc = desc        # Description
        self.i_serv_type = i_serv_type
        self.n_lcomtype = n_lcomtype
        self.n_seistype = n_seistype
        self.midas_load_cases = midas_load_cases

    def print_mct_command_midas_combination(self):
        self._print_mct_command_basic_combination_info()
        print(end='        ')
        print(*self._get_midas_print_list(), sep=', ')

    def _print_mct_command_basic_combination_info(self):
        print("   NAME={}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.name, self.kind, self.active, self.b_es,
                                                                  self.i_type, self.desc, self.i_serv_type,
                                                                  self.n_lcomtype, self.n_seistype))

    def _get_midas_print_list(self) -> list:
        print_list = []

        unique_names = []
        for m_load_case in self._get_effective_list():
            lc_name = m_load_case.lcname
            if lc_name in unique_names:
                # Midas Civil doesnt let have duplicate load cases in a load combination so we need to omit them
                pass
            else:
                print_list += m_load_case.get_properties_as_mct_command_list()
                unique_names.append(lc_name)

        return print_list

    def _get_effective_list(self) -> List[MidasLoadCase]:
        effective_list = []
        factor = 1.0
        for lc in self.midas_load_cases:
            if lc.anal == 'CB':
                factor *= lc.fact
            else:
                lc.fact *= factor
                effective_list.append(lc)
                factor = 1.0

        return effective_list
