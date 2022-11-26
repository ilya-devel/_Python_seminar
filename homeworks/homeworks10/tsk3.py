class Person:
    def __init__(self, name: str, fathername: str, surname: str, phones: dict):
        self.surname = surname
        self.name = name
        self.fathername = fathername
        self.phones = phones

    def get_phone(self, key='private'):
        return self.phones[key] if key in self.phones.keys() else None

    def get_name(self):
        return f'{self.surname} {self.name} {self.fathername}'

    def get_work_phone(self, key='work'):
        return self.phones[key] if key in self.phones.keys() else None

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.fathername}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, company: str, type_cmp: str, phones: dict, *args: Person):
        self.name = company
        self.type = type_cmp
        self.phones = phones
        self.employees = args

    def get_phone(self):
        if 'contact' in self.phones.keys():
            return self.phones['contact']
        else:
            for pers in self.employees:
                if 'work' in pers.phones.keys():
                    return pers.phones['work']
        return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.type}'


def send_sms(*args: Person or Company):
    for item in args:
        if item.get_phone():
            print(f'Отправлено СМС на номер {item.get_phone()} с текстом: {item.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {item.get_name()}')


if __name__ == '__main__':
    person1 = Person('Ivan', 'Ivanovich', 'Ivanov', {'private': 123, 'work': 456})
    person2 = Person('Ivan', 'Petrovich', 'Petrov', {'private': 789})
    person3 = Person('Ivan', 'Petrovich', 'Sidorov', {'work': 789})
    person4 = Person('John', 'Unknown', 'Doe', {})
    company1 = Company('Bell', 'OOO', {'contact': 111}, person3, person4)
    company2 = Company('Cell', 'AO', {'non_contact': 222}, person2, person3)
    company3 = Company('Dell', 'LTD', {'non_contact': 333}, person2, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)

    print()

    person1 = Person('Степан', 'Петрович', 'Джобсов', {'private': 555})
    person2 = Person('Боря', 'Иванович', 'Гейтсов', {'private': 777, 'work': 888})
    person3 = Person('Семен', 'Робертович', 'Возняцкий', {'work': 789})
    person4 = Person('Леонид', 'Арсенович', 'Торвальдсон', {})
    company1 = Company('Яблочный комбинат', 'ООО', {'contact': 111}, person1, person3)
    company2 = Company('ПластОкно', 'АО', {'non_contact': 222}, person2)
    company3 = Company('Пингвинья ферма', 'LTD', {'non_contact': 333},person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)
