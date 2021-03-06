from App.CombinationTree.LoadCase import LoadCase
from App.CombinationTree.LoadCombination import LoadCombination
from App.Config import Config


class Validator:
    def __init__(self):
        self.messages = []

    def validate_comb(self, main_comb: LoadCombination):
        self._next(main_comb)
        print('Validation complete. Data correct.')

    def _next(self, comb: LoadCombination):
        for lc_f in comb.load_cases:
            if not self._is_lc_f_correct(lc_f, comb.name):
                print(*self.messages)
                exit()

            if lc_f[0].__class__.__name__ == 'LoadCombination':
                self._next(lc_f[0])

    def _is_lc_f_correct(self, lc_f, comb_name):
        if not (isinstance(lc_f, list)):
            self.messages.append(
                'Load case not provided as list. Load case not wrapped in []. \nCheck: ' + comb_name)
            return False

        if not (len(lc_f) == 2):
            self.messages.append(
                'Load case in load combination not provided with 2 values: LoadCase and Factor. \nCheck: ' + comb_name)
            return False

        if not (isinstance(lc_f[0], LoadCase) or isinstance(lc_f[0], LoadCombination)):
            self.messages.append('Load case not of type LoadCase or LoadCombination. \nCheck: ' + comb_name)
            return False

        if not (isinstance(lc_f[1], int) or isinstance(lc_f[1], float)):
            self.messages.append('Factor not float/int. \nCheck: ' + comb_name)
            return False

        return True
