from functools import total_ordering


# @total_ordering
class Vacansy:
    """Класс описания вакансии"""

    title: str
    link: str
    salary: float
    area: str
    description: str
    requirement: str

    def __init__(self, title: str, link: str, salary: float, area: str, description: str, requirement: str):
        self.title = title
        self.link = link
        self.salary = salary
        self.area = area
        self.description = description
        self.requirements = requirement

    def __str__(self):
        title = f"Вакансия - {self.title}.format(self.title)"
        salary = f"Зарплата - {self.salary}.format(self.salary)"
        area = f"Местоположение - {self.area}.format(self.area)"
        link = f"Ссылка на вакансию - {self.link}.format(self.link)"
        return f"{title}, {salary}, {area}, {link}"

    def vac_full(self):
        title = f"Вакансия - {self.title}"
        salary = f"зарплата - {self.salary}"
        area = f"местоположение - {self.area}"
        description = f"описание - {self.description}"
        requirement = f"требования - {self.requirement}"
        link = f"ссылка - {self.link}"
        return f"{title}, {salary}, {area}, {description}, {requirement}, {link}"

        def __eq__(self, other):
            if isinstance(other, Vacansy):
                return self.salary == other.salary
            else:
                return NotImplemented

        def __lt__(self, other):
            if isinstance(other, Vacansy):
                return self.salary < other.salary
            else:
                return NotImplemented

        def __ge__(self, other):
            if isinstance(other, Vacansy):
                return self.salary >= other.salary
            else:
                return NotImplemented


if __name__ == "__main__":
    vac_1 = Vacansy("Продавец", "link.ru", "Продажа томатов.", "Без опыта работы.", "Москва", 30000)
    print(vac_1.description)
    print(vac_1.requirement)
    print(vac_1)
