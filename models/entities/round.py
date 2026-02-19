from datetime import datetime
from typing import Any
from models.entities.match import Match


class Round:

    def __init__(
        self,
        name: str,
        matches: list[Any],
        start_datetime: str | datetime,
        end_datetime: str | datetime | None = None,
    ) -> None:
        self.name = name
        self.matches: list[Any] = [
            m if isinstance(m, Match) else Match.from_tuple(m) for m in matches
        ]
        self.start_datetime = (
            datetime.fromisoformat(start_datetime)
            if isinstance(start_datetime, str)
            else start_datetime
        )
        self.end_datetime = (
            datetime.fromisoformat(end_datetime) if isinstance(end_datetime, str) else end_datetime
        )

    def end_round(self, value: datetime) -> None:
        self.end_datetime = value

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "matches": [match.to_tuple() for match in self.matches],
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat() if self.end_datetime else None,
        }
