address_book = [{"name": "john", "phone": "401"}, {"name": "bob", "phone": "501"}]


def print_address_book():
    for person in address_book:
        print_person = ''
        for element in person:
            print_person = print_person + element + ": " + person[element] + ", "
        print(print_person)


def add_person():
    person = {}
    while person != '':
        person_name = input("Podaj imię: ").lower()
        if check_person_by_name(person_name) is None:
            person['name'] = person_name
            person['phone'] = input("Podaj telefon: ")
            return person
        else:
            print('Kontakt o takim imieniu już istnieje')

def remove_person():
    result = 'x'
    while result is not None:
        rem_person = input('Podaj imię do usunięcia: ').lower()
        if check_person_by_name(rem_person) is None:
            print("Nie ma takiej osoby w Twojej książce")
            result = ''
        else:
            return check_person_by_name(rem_person)


def check_person_by_name(name):
    person = ''
    for person in address_book:
        if person['name'] == name:
            person = person
            break
        else:
            person = None
    if person is None:
        return None
    else:
        return person

def search_person():
    name = input("Podaj imię do wyszukania: ").lower()
    person = check_person_by_name(name)
    if person is None:
        print("Nie ma takiej osoby")
    else:
        print_person = ""
        for element in person:
            print_person = print_person + element + ": " + person[element] + ", "
        print(print_person)

def main():
    user_choice = ''
    while user_choice != 'K':
        user_choice = input("""Menu:
                    Wszystkie wpisy - W
                    Nowy wpis - N
                    Usuń wpis - U
                    Szukaj - S
                    Koniec - K:
                    """).upper()
        #    user_choice = 'U'
        if user_choice == 'W':
            print_address_book()
        elif user_choice == 'N':
            address_book.append(add_person())
            print("Osoba dodana")
        elif user_choice == 'U':
            address_book.remove(remove_person())
            print("Osoba została usunięta")
        elif user_choice == 'S':
            search_person()
        elif user_choice == 'K':
            print('Pa!')
        else:
            print("Wartość z poza listy")


main()
