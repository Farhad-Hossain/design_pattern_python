from dataclasses import dataclass

class ComplexSystemStore:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cache = {}
        print(f'Reading data from file')
    
    def store(self, key, value):
        self.cache[key] = value

    def read(self, key):
        return self.cache[key]

    def commit(self):
        print(f"Storing cached data to the file")

@dataclass
class User:
    login: str

class UserRepository:
    def __init__(self):
        self.system_preferences = ComplexSystemStore('hello/bangladesh')

    def store(self, user: User):
        self.system_preferences.store("USER_KEY", user.login)
        self.system_preferences.commit()
    
    def find_first(self):
        return User(self.system_preferences.read('USER_KEY'))

if __name__ == '__main__':
    user_repo = UserRepository()
    user = User("John")

    user_repo.store(user)
    retrived_user = user_repo.find_first()
    print(retrived_user.login)
