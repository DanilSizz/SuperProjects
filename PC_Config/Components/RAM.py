import Component

class RAM(Component.Component):

    def __init__(self, freq: float, value: int):
        self.freq = freq
        self.value = value

    