class ControlTower:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print('Initializing Control Tower')
        return cls._instance

tower1 = ControlTower()
tower2 = ControlTower()

print(tower1 is tower2)