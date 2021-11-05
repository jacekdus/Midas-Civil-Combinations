class MidasLoadCase:
    def __init__(self, anal, lcname, fact):
        self.anal = anal        # ST/CB
        self.lcname = lcname    # Load case name
        self.fact = fact        # Factor

    def get_properties_as_mct_command_list(self):
        return [self.anal, self.lcname, self.fact]
