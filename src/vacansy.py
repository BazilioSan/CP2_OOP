
class Vacansy:
    """Класс описания вакансии"""

    title: str
    link: str
    salary: float
    area: str
    description: str
    requirements: str

    def __init__(self, title: str, link: str, salary: float, area: str, description: str, requirements: str):
        self.title = title
        self.link = link
        self.salary = salary
        self.area = area
        self.description = description
        self.requirements = requirements

    def __str__(self):
        title = f"Вакансия - {self.title}.format(self.title)"
        salary = f"Зарплата - {self.salary}.format(self.salary)"
        area = f"Местоположение - {self.area}.format(self.area)"
        link = f"Ссылка на вакансию - {self.link}.format(self.link)"
        return f"{title}, {salary}, {area}, {link}"


