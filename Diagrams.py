import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas
from datetime import datetime


def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def age_category(age):
    if age < 18:
        return 'Менше 18'
    elif 18 <= age < 45:
        return '18-45'
    elif 45 <= age < 70:
        return '45-70'
    else:
        return 'Старше 70'

csv_file = 'Employees.csv'

try:
    data = pandas.read_csv(csv_file)
except FileNotFoundError:
    print("Помилка: Файл CSV не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка: {e}. Неможливо відкрити файл CSV.")
    exit(1)

# Побудова діаграми по статі
gender_counts = data['Стать'].value_counts()
print("Кількості співробітників чоловічої та жіночої статі:")
print(gender_counts)
gender_counts.plot(kind='bar', title='Розподіл по статі')
plt.xlabel('Стать')
plt.ylabel('Кількість')
plt.show()

# Побудова діаграми за віковими категоріями
data['Вікова категорія'] = data['Дата народження'].apply(lambda x: age_category(calculate_age(x)))
age_category_counts = data['Вікова категорія'].value_counts()
print("\nКількість працівників у кожній віковій категорії:")
print(age_category_counts)
age_category_counts.plot(kind='bar', title='Розподіл за віковими категоріями')
plt.xlabel('Вікова категорія')
plt.ylabel('Кількість')
plt.show()

# Побудова діаграми для кількості співробітників чоловічої та жіночої статі у кожній віковій категорії
gender_age_category_counts = data.groupby(['Стать', 'Вікова категорія']).size().unstack(fill_value=0)
print("\nКількість працівників чоловічої та жіночої статі у кожній віковій категорії:")
print(gender_age_category_counts)
gender_age_category_counts.plot(kind='bar', title='Розподіл за статтю та віковими категоріями')
plt.xlabel('Вікова категорія')
plt.ylabel('Кількість')
plt.show()