# hackaton_1
********Wisielec*******:
Program, będący implementacją gry "wisielec".
Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.


Słowa do odgadnięcia utrzymywane są słowniku word_list
Po wylosowaniu słowa do odgadnięcia, zastępuje je znakami "-"
Gra będzie dawała graczowi maksymalnie 10 prób na odgadnięcie słowa
Gra odpytuje gracza o litera które zawiera słowo (check_letter). W przypadku trafieni pojawia się informacja o trafieniu i zastępowane są znaki "-" odgadniętymi lietrami.
Po każdej wprowadzonej literce będzie możliwość odgadnięcia całego hasła (funkcja guess_word).
W przypadku odgadnięcia hasła, gra kończy się zwycięstwem gracza.
W przypadku błędnej próby odgadnięcia licznik prób zmniejsza się o 2 próby.
Gra kończy się w momencie gdy gracz przekroczy liczbę 10 prób lub nie odgadnie wszystkich liter w haśle.


*******Address book*******
Program do wprowadzania danych (imię i numer telefonu)
Program umożliwia:
Pokazania wszystkich adresów - print_address_book
Dodanie konatktu - add_person
Usunięcie kontaktu - remove_person
Wyszukanie kontaktu po imieniu - search_person


*******XO*********
Wczytanie graczy i przypisanie im X, O
Rozpoczecie rozgrywki pętla do wpowadzania danych do matrycy