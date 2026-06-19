import json
import os

FILE_NAME = 'contacts.json'

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_contacts(contacts):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def add_contact():
    print("\n--- Добавление контакта ---")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    email = input("Введите email: ")
    
    contacts = load_contacts()
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(new_contact)
    save_contacts(contacts)
    print("Контакт добавлен!")

def show_all():
    contacts = load_contacts()
    print("\n=== Все контакты ===")
    if not contacts:
        print("Контакты отсутствуют.")
        return
        
    for contact in contacts:
        name = contact.get("name", "")
        phone = contact.get("phone", "")
        email = contact.get("email", "")
        print(f"Имя: {name} | Телефон: {phone} | Email: {email}")

def search_contact():
    print("\n--- Поиск контакта ---")
    search_name = input("Введите имя для поиска: ").lower()
    
    contacts = load_contacts()
    found_contacts = []
    
    for contact in contacts:
        if search_name in contact.get("name", "").lower():
            found_contacts.append(contact)
            
    if not found_contacts:
        print("Контакты не найдены.")
        return
        
    print("\nНайденные контакты:")
    for contact in found_contacts:
        name = contact.get("name", "")
        phone = contact.get("phone", "")
        email = contact.get("email", "")
        print(f"Имя: {name} | Телефон: {phone} | Email: {email}")

def show_menu():
    while True:
        print("\n=== Телефонная книга ===")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Поиск по имени")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            show_all()
        elif choice == '3':
            search_contact()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == '__main__':
    show_menu()