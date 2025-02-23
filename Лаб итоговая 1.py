class Student:
    """
    Базовый класс для студентов
    """

    def __init__(self, name: str, age: int, major: str) -> None:
        """
        Инициализация студента

        :param name: Имя
        :param age: Возраст
        :param major: Специальность
        """
        self._name = name  # Непубличный атрибут
        self._age = age  # Непубличный атрибут
        self._major = major  # Непубличный атрибут

    def __str__(self) -> str:
        """
        Возвращает строковое представление студента

        :return: Строка с информацией о студенте.
        """
        return f"Student(Name: {self._name}, Age: {self._age}, Major: {self._major})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление студента

        :return: Официальная строка с информацией о студенте
        """
        return f"Student(name='{self._name}', age={self._age}, major='{self._major}')"

    def study(self) -> str:
        """
        Процесс учебы студента

        :return: Сообщение о том, что студент учится
        """
        return f"{self._name} is studying."


class Undergraduate(Student):
    """
    Класс бакалавров
    """

    def __init__(self, name: str, age: int, major: str, year: int) -> None:
        """
        Инициализация бакалавра

        :param name: Имя
        :param age: Возраст
        :param major: Специальность
        :param year: Год обучения (1-4)
        """
        super().__init__(name, age, major)  # Вызывает конструктор базового класса
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление бакалавра

        :return: Строка с информацией о бакалавре
        """
        return f"{super().__str__()}, Year: {self.year}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление бакалавра

        :return: Официальная строка с информацией о бакалавре
        """
        return f"Undergraduate(name='{self._name}', age={self._age}, major='{self._major}', year={self.year})"

    def study(self) -> str:
        """
        Переопределяет метод: добавляет информацию, что бакалавр готовится к экзаменам

        :return: Сообщение о том, что бакалавр и готовится к экзаменам
        """
        return f"{self._name} is studying for exams in year {self.year}."


class Graduate(Student):
    """
    Класс магистр
    """

    def __init__(self, name: str, age: int, major: str, thesis_topic: str) -> None:
        """
        Инициализация магистра

        :param name: Имя
        :param age: Возраст
        :param major: Специальность
        :param thesis_topic: Тема дипломной работы
        """
        super().__init__(name, age, major)  # Вызов конструктора базового класса
        self._thesis_topic = thesis_topic  # Непубличный атрибут для инкапсуляции

    def __str__(self) -> str:
        """
        Возвращает строковое представление

        :return: Строка с информацией о магистре
        """
        return f"{super().__str__()}, Thesis Topic: {self._thesis_topic}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление магистра

        :return: Официальная строка с информацией о магистре
        """
        return f"Graduate(name='{self._name}', age={self._age}, major='{self._major}', thesis_topic='{self._thesis_topic}')"

    def study(self) -> str:
        """
        Переопределяет метод, добавляет информацию, что магистр работает над дипломом

        :return: Сообщение о том, что магистр учится и работает над дипломом
        """
        return f"{self._name} is working on the thesis titled '{self._thesis_topic}'."


if __name__ == "__main__":
    undergraduate = Undergraduate("Alice", 20, "Computer Science", 2)
    print(undergraduate)
    print(undergraduate.study())

    graduate = Graduate("Bob", 25, "Physics", "Quantum Mechanics")
    print(graduate)
    print(graduate.study())
