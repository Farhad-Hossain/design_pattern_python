from dataclasses import dataclass

@dataclass
class Memento:
    state: str

class Originator:
    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)
    
    def restore_memento(self, memento: Memento):
        self.state = memento.state

class Caretaker:
    memento_list = []

    def save_state(self, state: Memento):
        self.memento_list.append(state)

    def restore(self, index: int):
        return self.memento_list[index]


if __name__ == '__main__':
    originator = Originator('Initial State')

    caretaker = Caretaker()

    caretaker.save_state(originator.create_memento())
    print(f'Current state is {originator.state}')

    originator.state = 'State 1'
    caretaker.save_state(originator.create_memento())
    print(f'Current state is {originator.state}')

    originator.state = 'State 2'
    caretaker.save_state(originator.create_memento())
    print(f'Current state is {originator.state}')

    originator.state = 'State 3'
    caretaker.save_state(originator.create_memento())
    print(f'Current state is {originator.state}')


    originator.restore_memento(caretaker.restore(1))



