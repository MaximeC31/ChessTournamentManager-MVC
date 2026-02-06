from datetime import datetime
from typing import TypedDict
from models.match import Match


class RoundData(TypedDict):
    name: str
    start_datetime: str
    end_datetime: str | None
    matches: list[Match]


class Round:

    def __init__(
        self,
        name: str,
        start_datetime: datetime,
        matches: list[Match],
        end_datetime: datetime | None = None,
    ) -> None:
        self.name = name
        self.start_datetime = start_datetime
        self.matches = matches
        self.end_datetime = end_datetime

    def end_round(self, value: datetime) -> None:
        self.end_datetime = value

    def to_dict(self) -> RoundData:
        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat() if self.end_datetime else None,
            "matches": [match.to_dict() for match in self.matches],
        }

    @classmethod
    def from_dict(cls, data: RoundData) -> "Round":
        return cls(
            name=data["name"],
            start_datetime=datetime.fromisoformat(data["start_datetime"]),
            matches=[Match.from_dict(match_data) for match_data in data["matches"]],
            end_datetime=(
                datetime.fromisoformat(data["end_datetime"]) if data["end_datetime"] else None
            ),
        )
