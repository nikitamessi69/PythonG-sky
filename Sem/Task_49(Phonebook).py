# Задача 49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

 
def add_contact():
    with open('phonebook.txt', 'a') as data:
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"Фамилия:{last_name}, Имя:{first_name}, Отчество:{middle_name}, Телефон:{phone_number}\n")
        
          
def show_contacts():
    with open('phonebook.txt', 'r') as data:
        for line in data:
            print(line.strip())
            
            
def search_contacts():
    search_param = input("Введите характеристику для поиска записей (например, фамилию): ")
    with open('phonebook.txt', 'r') as data:
        for line in data:
            if search_param in line:
                print(line.strip())
                
                
def export_contacts():
    with open('phonebook.txt', 'r') as data:
        contacts = data.read()
    with open('phonebook_export.txt', 'w') as data:
        data.write(contacts)
        

def main():
    while True:
        print("Выберите действие:")
        print("1 - Добавить новую запись")
        print("2 - Посмотреть все записи")
        print("3 - Поиск записей по характеристике")
        print("4 - Экспорт записей в файл в формате _export.txt")
        print("5 - Выход")
        choice = input("Введите номер действия: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            export_contacts()
        elif choice == '5':
            break
        else:
            print("Некорректный выбор, повторите попытку")
            

if __name__ == '__main__':
    main()