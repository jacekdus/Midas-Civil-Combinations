# Midas-Civil-Combinations

## Jak uruchomić 

Przed przystapieniem do uruchomienia aplikacji, upewnij sie, że masz zainstalowaną najnowszą wersję [Pythona](https://www.python.org/downloads/)

**BARDZO WAŻNE!!!** Podczas instalacji upewnij się żeby zaznaczyć opcję 
> Add python to environment variables

Jeżeli z programu korzystasz pierwszy raz musisz zainstalować bibliotekę [treelib](https://treelib.readthedocs.io/en/latest/). Zainstalujesz ją wpisując w wierszu polecenia następującą komendę i wciskając enter:

`pip install treelib`

Jeżeli wyskoczy błąd, prawdopodobnie podczas instalacji Pythona nie została zaznaczona opcja **Add python to environment variables**. W takim wypadku należy uruchomić instalatora Pythona jeszcze raz, w okienku wyboru wybrać ścieżkę Modify, kliknąć Next, a następnie zaznaczyć **Add python to environment variables**, po zakończeniu instalacji powyższa komenda powinna już działać.

Instrukcja dodawania danych wejsciowych do aplikacji znajduje sie w pliku `Input.py`

Aby uruchomic aplikacje uruchom wiersz polecenia w folderze aplikacji, w którym znajduje się plik `Main.py`, 
po czym wpisz następującą komendę:

`py Main.py`

Przykład w powershell:

`PS C:\Users\user\Desktop\Programy\Combinations> py Main.py`

## Rezultat

Jeżeli aplikacja pomyślnie zakończyła swoje działanie, to w folderze z plikiem `Main.py`, powinny zostać utworzone pliki:
- `mct_command.txt` - plik tekstowy z przygotowaną komendą do bezpośredniego wklejenia do programu Midas Civil 
w opcji MCT Command Shell.
- `log.txt` - plik tekstowy zawierający raport z tworzenia kombinacji.
