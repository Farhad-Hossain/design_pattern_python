from dataclasses import dataclass

@dataclass
class DisplayDataType:
    index: float
    data: str

class DisplayData:
    def __init__(self, display_data: DisplayDataType):
        self.display_data = display_data
    
    def show_data(self):
        print(f"Index: {self.display_data.position}, Data: {self.display_data.amount}")

@dataclass
class DatabaseDataType:
    position: int
    amount: str

class StoreDatabaseData:
    def __init__(self, database_data: DatabaseDataType):
        self.database_data = database_data

    def store_data(self):
        print(f"Position: {self.database_data.position}, Amount: {self.database_data.amount}")


class DisplayDataAdapter(StoreDatabaseData, DisplayData):
    def __init__(self, data):
        self.data = data

    def store_data(self):
        print('Call out code but using 3rd party library')
        for item in self.data:
            ddt = DatabaseDataType(float(item.position), str(item.amount))
            self.display_data = ddt
            self.show_data()

def generate_data():
    data = []
    data.append(DatabaseDataType(1, "Data 1"))
    data.append(DatabaseDataType(2, "Data 2"))
    data.append(DatabaseDataType(3, "Data 3"))
    data.append(DatabaseDataType(4, "Data 4"))
    return data

if __name__ == "__main__":
    adapter = DisplayDataAdapter(generate_data())
    adapter.store_data()




