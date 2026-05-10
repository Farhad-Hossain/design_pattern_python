from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        print(f'Image loading ....')

    def display(self):
        print(f"Real image : displaying... {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
    
    def display(self):
        print(f"Proxy Image ...")
        if not self.real_image:
            print("From DIsk ...")
            self.real_image = RealImage(self.filename)

        else:
            print('Form the cache')

        self.real_image.display()

if __name__ == '__main__':
    image = ProxyImage('test.jpg')
    image.display()
    image.display()

