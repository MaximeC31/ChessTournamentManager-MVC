from datetime import datetime
from typing import TypedDict


class RoundData(TypedDict):
    name: str
    start_datetime: str
    end_datetime: str | None


class Round:

    def __init__(
        self,
        name: str,
        start_datetime: datetime,
        end_datetime: datetime | None,
    ) -> None:
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def end_round(self, value: datetime) -> None:
        self.end_datetime = value

    def to_dict(self) -> RoundData:
        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat() if self.end_datetime else None,
        }

    @classmethod
    def from_dict(cls, data: RoundData) -> "Round":
        start_str = data["start_datetime"]
        end_str = data.get("end_datetime")

        return cls(
            name=data["name"],
            start_datetime=datetime.fromisoformat(start_str),
            end_datetime=datetime.fromisoformat(end_str) if end_str else None,
        )
