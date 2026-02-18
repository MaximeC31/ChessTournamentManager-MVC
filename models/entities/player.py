from datetime import datetime


class Player:

    def __init__(self, last_name: str, first_name: str, birth_date: str, national_id: str) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = self.validate_birth_date(birth_date)
        self.national_id = self.validate_national_id(national_id)

    def validate_birth_date(self, value: str) -> str:
        value_splitted = value.split("-")

        if len(value_splitted) != 3:
            raise ValueError(f"Date de naissance invalide : format YYYY-MM-DD requis.")
        try:
            year, month, day = map(int, value_splitted)
            birth_date = datetime(year, month, day)
        except ValueError:
            raise ValueError(f"Date de naissance invalide : date incorrecte.")

        today = datetime.now()
        eighteen_years_ago = datetime(today.year - 18, today.month, today.day)
        if not (year > 1900 and birth_date <= eighteen_years_ago):
            raise ValueError(f"Date de naissance invalide : le joueur doit être majeur")

        return value

    def validate_national_id(self, value: str) -> str:
        if not len(value) == 7:
            raise ValueError(f"Identifiant {value} invalide : longueur de 7 caractères requise.")

        if not value[:2].isalpha() or not value[:2].isupper():
            raise ValueError(f"Identifiant {value} invalide : les 2 premiers caractères invalides.")

        if not value[2:].isdigit():
            raise ValueError(f"Identifiant {value} invalide : les 5 derniers caractères invalides.")

        return value

    def to_dict(self) -> dict[str, str]:
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
        }
