from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Класс імені
class Name(Field):
    pass
  
# Класс телефону
class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.is_valid(value):
            raise ValueError('Error, the number must have 10 digits')

    def is_valid(self, value):
        return len(value) == 10 and self.value.isdigit()

# Класс додавання запису
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    #Додаэмо телефон
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
    #Видаляемо телефон
    def remove_phone(self, phone):
        for phone in self.phones:
            if phone == phone:
                self.phones.remove(phone)
                return self.phones
        raise ValueError('Invalid number')
    #редагуемо телефон
    def edit_phone(self, old_phone, edit_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = edit_phone
                return phone.value
        raise ValueError('Invalid number')
    #Шукаємо телефон
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Класс адресної книжки
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]
