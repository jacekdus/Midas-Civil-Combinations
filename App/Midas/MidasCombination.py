from App.Midas.MidasLoadCaseCollection import MidasLoadCaseCollection


class MidasCombination:
    def __init__(self, name, midas_load_case_collection: MidasLoadCaseCollection,
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
        self.load_case_collection: MidasLoadCaseCollection = midas_load_case_collection

    def print_mct_command_midas_combination(self):
        print("   NAME={}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.name, self.kind, self.active, self.b_es,
                                                                  self.i_type, self.desc, self.i_serv_type,
                                                                  self.n_lcomtype, self.n_seistype))
        print(end='        ')
        print(*self.load_case_collection.get_midas_print_list(), sep=', ')
