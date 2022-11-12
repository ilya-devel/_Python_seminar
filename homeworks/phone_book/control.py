import view


def app():
    while True:
        choice = view.menu()
        if choice == '1':
            view.show_contact()
        elif choice == '2':
            view.find_contact()
        elif choice == '3':
            view.add_contact()
        elif choice == '4':
            view.import_contacts()
        elif choice == '5':
            view.export_contact()
        else:
            print('Invalue number of operation')
        ans = input('Do you want to continue?: Y/n')
        if ans.lower() != 'y':
            break
