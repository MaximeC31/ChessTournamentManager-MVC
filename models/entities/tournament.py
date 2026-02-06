from datetime import datetime
from typing import TypedDict, Any

from models.entities.player import Player
from models.entities.round import Round


class TournamentData(TypedDict):
    name: str
    venue: str
    start_date: str
    end_date: str | None
    description: str
    number_of_rounds: int
    current_round_number: int
    rounds: list[Any]
    players: list[Any]


class Tournament:

    def __init__(
        self,
        name: str,
        venue: str,
        start_date: datetime,
        end_date: datetime | None,
        description: str,
        current_round_number: int,
        rounds: list[Round],
        players: list[Player],
        number_of_rounds: int = 4,
    ) -> None:
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.current_round_number = current_round_number
        self.rounds = rounds
        self.players = players
        self.number_of_rounds = number_of_rounds

    def to_dict(self) -> TournamentData:
        return {
            "name": self.name,
            "venue": self.venue,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "current_round_number": self.current_round_number,
            "rounds": [r.to_dict() for r in self.rounds],
            "players": [p.to_dict() for p in self.players],
        }

    @classmethod
    def from_dict(cls, data: TournamentData) -> "Tournament":
        end_date_str = data["end_date"]

        return cls(
            name=data["name"],
            venue=data["venue"],
            start_date=datetime.fromisoformat(data["start_date"]),
            end_date=datetime.fromisoformat(end_date_str) if end_date_str else None,
            description=data["description"],
            current_round_number=data["current_round_number"],
            rounds=[Round.from_dict(r) for r in data["rounds"]],
            players=[Player.from_dict(p) for p in data["players"]],
            number_of_rounds=data["number_of_rounds"],
        )
