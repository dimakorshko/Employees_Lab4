import pandas
from datetime import datetime

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

try:
    excel_file = 'Excel_file.xlsx'
    csv_file = 'Employees.csv'
    data = pandas.read_csv(csv_file)

    selected_data = data[['Прізвище', "Ім'я", "По батькові" ,'Дата народження']]
    selected_data = selected_data.assign(Вік=selected_data['Дата народження'].apply(lambda x: calculate_age(x)))
    data_18 = selected_data[selected_data['Вік'] < 18]
    data_18_45 = selected_data[(selected_data['Вік'] < 45) & (selected_data['Вік'] > 18)]
    data_45_70 = selected_data[(selected_data['Вік'] < 70) & (selected_data['Вік'] > 45)]
    data_70 = selected_data[selected_data['Вік'] > 70]

    with pandas.ExcelWriter(excel_file) as writer:
        data.to_excel(writer, sheet_name="all", index=False)
        data_18.to_excel(writer, sheet_name="younger_18", index=False)
        data_18_45.to_excel(writer, sheet_name="18_45", index=False)
        data_45_70.to_excel(writer, sheet_name="45_70", index=False)
        data_70.to_excel(writer, sheet_name="older_70", index=False)
    print("OK")

except FileNotFoundError:
    print("Помилка: файл CSV не знайдено.")
except Exception as e:
    print(f"Помилка: {e}. Неможливо створити XLSX файл.")