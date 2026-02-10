from datetime import datetime
from typing import Any

from models.entities.player import Player
from models.entities.round import Round


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
        number_of_rounds: int,
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

    def to_dict(self) -> Any:
        return {
            "name": self.name,
            "venue": self.venue,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "description": self.description,
            "current_round_number": self.current_round_number,
            "rounds": [round.to_dict() for round in self.rounds],
            "players": [player.to_dict() for player in self.players],
            "number_of_rounds": self.number_of_rounds,
        }

    @classmethod
    def from_dict(cls, data: Any) -> "Tournament":
        return cls(
            name=data["name"],
            venue=data["venue"],
            start_date=datetime.fromisoformat(data["start_date"]),
            end_date=datetime.fromisoformat(data["end_date"]) if data["end_date"] else None,
            description=data["description"],
            current_round_number=data["current_round_number"],
            rounds=[Round.from_dict(r) for r in data["rounds"]],
            players=[Player.from_dict(p) for p in data["players"]],
            number_of_rounds=data["number_of_rounds"],
        )
