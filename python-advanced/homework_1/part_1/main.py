from abc import ABC, abstractmethod
from typing import Union

class Animal(ABC):

    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound
        
    @abstractmethod
    def makesound(self) -> None:
        pass

class Cat(Animal):

    color: Union[str, None] = None

    def makesound(self) -> None:
        print("cat \"" + self.name + "\"" + (", цвета \"" + self.color + "\"," if self.color else "") + " make sound \"" + self.sound + "\"")

class Dog(Animal):

    color: Union[str, None] = None

    def makesound(self) -> None:
        print("dog \"" + self.name + "\"" + (", цвета \"" + self.color + "\"," if self.color else "") + " make bark sound \"" + self.sound + "\"")


if __name__ == "__main__":
    cat: Cat = Cat("Британский", "мяу")
    cat.color = "темно-синий"
    cat.makesound()

    dog: Dog = Dog("Собака", "гав")
    dog.makesound()

    # Тестирование
    assert issubclass(Cat, Animal)
    assert issubclass(Dog, Animal)


