from App.CombinationTree.LoadCase import LoadCase


class LoadCombination(LoadCase):
    def __init__(self, name, load_cases, active='Active', description='', envelop=False):
        LoadCase.__init__(self, name, _type='CB')
        self.load_cases = load_cases  # Array of pairs [LoadCase, factor]
        self.envelop = envelop
        self.active = active
        self.description = description