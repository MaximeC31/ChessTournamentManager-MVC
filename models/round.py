from datetime import datetime
from typing import TypedDict


class RoundData(TypedDict):
    """Schema for Round dictionary representation."""
    name: str
    start_datetime: str
    end_datetime: str | None


class Round:
    """Represents a tournament round."""

    def __init__(
        self,
        name: str,
        start_datetime: datetime | None = None,
        end_datetime: datetime | None = None,
    ) -> None:
        """
        Initialize a Round instance.
        If start_datetime is not provided, it defaults to the current time.
        """
        self.name = name
        self.start_datetime = start_datetime or datetime.now()
        self.end_datetime = end_datetime

    def end_round(self) -> None:
        """Mark the round as finished by setting the end datetime."""
        self.end_datetime = datetime.now()

    def to_dict(self) -> RoundData:
        """Serialize the Round instance to a dictionary."""
        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat() if self.end_datetime else None,
        }

    @classmethod
    def from_dict(cls, data: RoundData) -> "Round":
        """Create a Round instance from a dictionary representation."""
        start_str = data["start_datetime"]
        end_str = data.get("end_datetime")

        return cls(
            name=data["name"],
            start_datetime=datetime.fromisoformat(start_str),
            end_datetime=datetime.fromisoformat(end_str) if end_str else None,
        )
