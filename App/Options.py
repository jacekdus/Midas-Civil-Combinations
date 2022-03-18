class Options:
    def __init__(self, kind='GEN', active='ACTIVE', i_serv_type=0,
                 indirect_kind='GEN', indirect_active='ACTIVE', indirect_i_serv_type=0, create_indirect_combs=True):
        self.kind = kind
        self.active = active
        self.i_serv_type = i_serv_type
        self.indirect_kind = indirect_kind
        self.indirect_active = indirect_active
        self.indirect_i_serv_type = indirect_i_serv_type
        self.create_indirect_combs = create_indirect_combs
