import Component

class Case(Component.Component):
    
    def __init__(self,form:str, long:int):
        self.form = form
        self.long = long