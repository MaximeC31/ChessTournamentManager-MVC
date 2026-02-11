from datetime import datetime
from typing import Any

from models.entities.player import Player
from models.entities.round import Round


class Tournament:

    def __init__(
        self,
        name: str,
        venue: str,
        start_date: str | datetime,
        end_date: str | datetime | None,
        description: str,
        current_round_number: int,
        rounds: list[Any],
        players: list[Any],
        number_of_rounds: int,
    ) -> None:
        self.name = name
        self.venue = venue
        self.start_date = (
            datetime.fromisoformat(start_date) if isinstance(start_date, str) else start_date
        )
        self.end_date = datetime.fromisoformat(end_date) if isinstance(end_date, str) else end_date
        self.description = description
        self.current_round_number = current_round_number
        self.rounds = [r if isinstance(r, Round) else Round(**r) for r in rounds]
        self.players = [p if isinstance(p, Player) else Player(**p) for p in players]
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
