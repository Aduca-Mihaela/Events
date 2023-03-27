from datetime import datetime

from Domain.Evenimente import Evenimente


class EvenimentValidator:
    def valideaza (self, evenimet: Evenimente):
        try:
            datetime.strptime(evenimet.getData(), '%d.%m.%Y')
            datetime.strptime(evenimet.getTimp(), '%H:%M')
        except ValueError:
            raise ValueError("Formatul datei trebuie sa fie : DD.MM.YYYY")
