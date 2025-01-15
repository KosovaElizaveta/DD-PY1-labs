class CuteCat:
    def __init__(self, name: str, age: int):
        """
        Инициализация объекта CuteCat.

        :param name: Имя кота (строка).
        :param age: Возраст кота в годах (целое число). Должен быть положительным числом.

        :raises ValueError: Если age не положительное число.
        """
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")

        self.name = name
        self.age = age

    def meow(self) -> str:
        """
        Кот издает звук "мяу".

        :return: Звук, который издает кот (строка).

        >>> cat = CuteCat("Мурка", 2)
        >>> cat.meow()
        'Мяу!'
        """
        return "Мяу!"

    def celebrate_birthday(self) -> None:
        """
        Увеличивает возраст кота на 1 год.

        >>> cat = CuteCat("Мурка", 2)
        >>> cat.celebrate_birthday()
        >>> cat.age
        3
        """
        self.age += 1


class SweetFlower:
    def __init__(self, species: str, color: str):
        """
        Инициализация объекта SweetFlower.

        :param species: Вид цветка (строка).
        :param color: Цвет цветка (строка).

        :raises ValueError: Если species или color пустые строки.
        """
        if not species or not color:
            raise ValueError("Вид и цвет цветка не могут быть пустыми строками.")

        self.species = species
        self.color = color

    def bloom(self) -> str:
        """
        Цветок распускается.

        :return: Сообщение о том, что цветок распустился (строка).

        >>> flower = SweetFlower("Роза", "Красный")
        >>> flower.bloom()
        'Роза распустилась!'
        """
        return f"{self.species} распустилась!"

    def wilt(self) -> str:
        """
        Цветок увядает.

        :return: Сообщение о том, что цветок увял (строка).

        >>> flower = SweetFlower("Роза", "Красный")
        >>> flower.wilt()
        'Роза увяла.'
        """
        return f"{self.species} увяла."


class CozyBook:
    def __init__(self, title: str, author: str):
        """
        Инициализация объекта CozyBook.

        :param title: Название книги (строка).
        :param author: Автор книги (строка).

        :raises ValueError: Если title или author пустые строки.
        """
        if not title or not author:
            raise ValueError("Название и автор книги не могут быть пустыми строками.")

        self.title = title
        self.author = author

    def read(self) -> str:
        """
        Чтение книги.

        :return: Сообщение о том, что книга читается (строка).

        >>> book = CozyBook("Гарри Поттер", "Джоан Роулинг")
        >>> book.read()
        'Вы читаете Гарри Поттер.'
        """
        return f"Вы читаете {self.title}."

    def summarize(self) -> str:
        """
        Получение краткого содержания книги.

        :return: Сообщение с кратким содержанием (строка).

        >>> book = CozyBook("Гарри Поттер", "Джоан Роулинг")
        >>> book.summarize()
        'Гарри Поттер - это история о юном волшебнике.'
        """
        return f"{self.title} - это история о юном волшебнике."


if __name__ == "__main__":
    import doctest

    doctest.testmod()



