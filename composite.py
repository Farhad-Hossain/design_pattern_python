class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Composite:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self

    @property
    def price(self):
        return sum([item.price for item in self.items])

if __name__ == '__main__':
    computer = Composite('Computer')
    memory = Composite('Memory')

    ram = Equipment('RAM', 100)
    cpu = Equipment('CPU', 200)
    hdd = Equipment('HDD', 300)

    memory.add(ram).add(cpu)
    computer.add(memory).add(hdd)

    print(computer.price) 
