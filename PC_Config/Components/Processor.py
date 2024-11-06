import Component

class Processor(Component.Component):

    def __init__(self, freq: float, cores: int):
        self.freq = freq
        self.cores = cores

    
