class product:
    def __init__(self, name, amount, type):
        self.name = name
        self.amount = int(amount)
        if type:
            self.type = "detaļa"
        else:
            self.type = "programma"
            
    def add(self, amount):
        self.amount += int(amount)

    def val(self):
        return [self.name, str(self.amount), self.type]
    
    def typ(self):
        return self.type
