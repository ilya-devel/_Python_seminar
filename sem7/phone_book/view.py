import operation_file


def menu():
    print('''
    1. Show contacts
    2. Find contact
    3. Add contact
    4. Import contact
    5. Export contact
    ''')
    return input('Choice operation: ')


def show_contact():
    operation_file.show_contacts()


def find_contact():
    operation_file.find_contact()
    print('Search complete\n')


def add_contact():
    operation_file.add_person(operation_file.get_info())
    print('Added contact\n')


def import_contacts():
    operation_file.import_contacts()
    print('Import completed\n')


def export_contact():
    operation_file.export_contact()
    print('Export completed')
