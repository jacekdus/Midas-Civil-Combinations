from typing import List

from App.Midas.MidasLoadCase import MidasLoadCase


class MidasLoadCaseCollection:
    def __init__(self, load_cases: List[MidasLoadCase]):
        self.load_cases: List[MidasLoadCase] = load_cases

    def get_midas_print_list(self) -> list:
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
        for lc in self.load_cases:
            if lc.anal == 'CB':
                factor *= lc.fact
            else:
                lc.fact *= factor
                effective_list.append(lc)
                factor = 1.0

        return effective_list
