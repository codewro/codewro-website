# Strona CodeWro

To jest repozytorium kodu strony http://codewro.pl/

## Jak pomóc przy rozwoju strony?

1. Ściągnij projekt na swój komputer.

    `git clone git@github.com:codewro/codewro-website.git`

2. Wejdź do nowoutworzonego folderu

    `cd codewro-website`

3. Stwórz virtualenv o nazwie np. "myvenv" i je aktywuj

    `python3 -m venv myvenv`
    
    Na linuxie i na macu:

        `source myvenv/bin/activate`

    Na windowsie:
    
        `myvenv\Scripts\activate`
    
4. Wpisz komendę

    `pip install -r requirements.txt`
    
5. Wpisz komendę 

    `python manage.py migrate`

6. Wpisz komendę

    `python manage.py runserver`
    
