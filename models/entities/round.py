from datetime import datetime
from typing import Any
from models.entities.match import Match


class Round:

    def __init__(
        self,
        name: str,
        matches: list[Any],
        s_datetime: str | datetime,
        e_datetime: str | datetime | None = None,
    ) -> None:
        self.name = name
        self.matches: list[Any] = [
            m if isinstance(m, Match) else Match.from_tuple(m) for m in matches
        ]
        self.s_datetime = (
            datetime.fromisoformat(s_datetime) if isinstance(s_datetime, str) else s_datetime
        )
        self.e_datetime = (
            datetime.fromisoformat(e_datetime) if isinstance(e_datetime, str) else e_datetime
        )

    def end_round(self, value: datetime) -> None:
        self.e_datetime = value

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "matches": [match.to_tuple() for match in self.matches],
            "s_datetime": self.s_datetime.isoformat(),
            "e_datetime": self.e_datetime.isoformat() if self.e_datetime else None,
        }
