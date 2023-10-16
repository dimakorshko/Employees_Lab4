import csv
import random
from faker import Faker
from faker.providers import BaseProvider
import calendar

class CustomDateProvider(BaseProvider):
    def birthdate_in_range(self):
        start_year = 1938
        end_year = 2008
        birth_year = random.randint(start_year, end_year)
        birth_month = random.randint(1, 12)
        max_day = calendar.monthrange(birth_year, birth_month)[1]
        birth_day = random.randint(1, max_day)
        return f"{birth_year}-{birth_month:02d}-{birth_day:02d}"


fake = Faker("uk_UA")
fake.add_provider(CustomDateProvider)

ukrainian_male_patronymics = ["Андрійович","Борисович","Васильович","Вікторович","Володимирович","Геннадійович","Григорійович","Давидович","Данилович",
    "Денисович","Євгенович","Захарович","Зеновійович","Ігорович","Іванович","Кирилович","Костянтинович","Леонідович","Максимович","Мар'янович","Марківич",
    "Михайлович","Назарович","Олегович","Олександрович","Олексійович","Остапович","Павлович","Петрович","Романович","Сергійович","Станіславович","Тарасович",
    "Тимофійович","Федорович","Юрійович","Ярославович"]

ukrainian_female_patronymics = ["Андріївна","Борисівна","Василівна","Вікторівна","Володимирівна","Геннадіївна","Григоріївна","Давидівна","Данилівна",
    "Денисівна","Євгенівна","Захарівна","Зеновіївна","Ігорівна","Іванівна","Кирилівна","Костянтинівна","Леонідівна","Максимівна","Мар'янівна","Марківна",
    "Михайлівна","Назарівна","Олегівна","Олександрівна","Олексіївна","Остапівна","Павлівна","Петрівна","Романівна","Сергіївна","Станіславівна","Тарасівна",
    "Тимофіївна","Федорівна","Юріївна", "Ярославівна"]

employee_position = ["Менеджер з продажу","Фінансовий аналітик","Системний адміністратор","Менеджер з маркетингу","HR-менеджер",
    "Бухгалтер","Програміст","Дизайнер","Асистент керівника","Копірайтер","Менеджер з продукту","Аналітик даних","Кадровий менеджер",
    "Менеджер з закупівель","Офіс-менеджер","Тестувальник","Інженер з якості","Архітектор","PR-менеджер","Аудитор"]

with open('Employees.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Прізвище', "Ім'я", 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

    for i in range(2000):
        tmp_gender = random.choices(["male", "female"], weights=[0.6, 0.4])[0]
        if tmp_gender == "male":
            tmp_name = fake.first_name_male()
            tmp_surname = fake.last_name_male()
            tmp_patronymics = random.choice(ukrainian_male_patronymics)
        else:
            tmp_name = fake.first_name_female()
            tmp_surname = fake.last_name_male()
            tmp_patronymics = random.choice(ukrainian_female_patronymics)
        csvwriter.writerow([tmp_surname, tmp_name, tmp_patronymics, tmp_gender, fake.birthdate_in_range(), random.choice(employee_position), fake.city(), fake.address(), fake.phone_number(), fake.email()])