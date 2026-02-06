class Player:

    def __init__(self, last_name: str, first_name: str, birth_date: str, national_id: str) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = self.validate_national_id(national_id)

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

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "Player":
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            birth_date=data["birth_date"],
            national_id=data["national_id"],
        )
