from datetime import datetime
from typing import Any
from models.entities.match import Match


class Round:

    def __init__(
        self,
        name: str,
        matches: list[Match],
        start_datetime: datetime,
        end_datetime: datetime | None = None,
    ) -> None:
        self.name = name
        self.matches = matches
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def end_round(self, value: datetime) -> None:
        self.end_datetime = value

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "matches": [match.to_tuple() for match in self.matches],
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat() if self.end_datetime else None,
        }

    @classmethod
    def from_dict(cls, data: Any) -> "Round":
        return cls(
            name=data["name"],
            matches=[Match.from_tuple(match_data) for match_data in data["matches"]],
            start_datetime=datetime.fromisoformat(data["start_datetime"]),
            end_datetime=(
                datetime.fromisoformat(data["end_datetime"]) if data["end_datetime"] else None
            ),
        )
