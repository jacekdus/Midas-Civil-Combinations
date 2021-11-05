class NodeData:
    def __init__(self, name, factor=None, _type=None):
        self.name = name
        self.factor = factor
        self.type = _type  # ST/CB
        if factor:
            self.value = str(factor) + '*' + name
        else:
            self.value = name
