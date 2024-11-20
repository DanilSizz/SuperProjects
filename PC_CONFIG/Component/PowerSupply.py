import Component

class PowerSupply(Component.Component):

        def __init__(self,rating:str, power:int):
            self.rating = rating
            self.power = power
    