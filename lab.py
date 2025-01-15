from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param make: Производитель транспортного средства (например, 'Toyota').
        :param model: Модель транспортного средства (например, 'Corolla').
        :param year: Год выпуска транспортного средства (например, 2020).
        :raises ValueError: Если год выпуска меньше 1886 (первый автомобиль).
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886.")

        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """Запустить двигатель транспортного средства."""
        ...

    @abstractmethod
    def stop_engine(self) -> None:
        """Остановить двигатель транспортного средства."""
        ...


class Book(ABC):
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.
        :raises ValueError: Если количество страниц меньше 1.
        """
        if pages < 1:
            raise ValueError("Количество страниц должно быть положительным.")

        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self) -> str:
        """Читать книгу и вернуть текст текущей страницы."""
        ...

    @abstractmethod
    def bookmark(self, page: int) -> None:
        """
        Установить закладку на странице.

        :param page: Номер страницы для закладки.
        :raises ValueError: Если номер страницы выходит за пределы книги.
        """
        ...


class Computer(ABC):
    def __init__(self, brand: str, ram: int, storage: int):
        """
        Инициализация компьютера.

        :param brand: Бренд компьютера (например, 'Dell').
        :param ram: Объем оперативной памяти в гигабайтах.
        :param storage: Объем хранилища в гигабайтах.
        :raises ValueError: Если объем RAM или хранилища меньше 1.
        """
        if ram < 1 or storage < 1:
            raise ValueError("Объем RAM и хранилища должен быть положительным.")

        self.brand = brand
        self.ram = ram
        self.storage = storage

    @abstractmethod
    def power_on(self) -> None:
        """Включить компьютер."""
        ...

    @abstractmethod
    def power_off(self) -> None:
        """Выключить компьютер."""
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass



