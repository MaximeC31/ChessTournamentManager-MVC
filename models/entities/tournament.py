from datetime import datetime
from typing import Any
import random

from models.entities.player import Player
from models.entities.round import Round
from models.entities.match import Match


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
        number_of_rounds: int = 4,
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

    def get_player_score(self, player: Player) -> float:
        score = 0.0

        for round in self.rounds:
            for match in round.matches:
                if match.player_1 == player:
                    score += match.score_1
                if match.player_2 == player:
                    score += match.score_2

        return score

    def get_played_opponents(self, player: Player) -> set[str]:
        opponents: set[str] = set()

        for round_obj in self.rounds:
            for match in round_obj.matches:
                if match.player_1.national_id == player.national_id and match.player_2:
                    opponents.add(match.player_2.national_id)

                if match.player_2 and match.player_2.national_id == player.national_id:
                    opponents.add(match.player_1.national_id)

        return opponents

    def generate_next_round(self) -> Round:
        sorted_players = sorted(self.players, key=self.get_player_score, reverse=True)

        if not self.rounds:
            random.shuffle(sorted_players)

        matches: list[Match] = []

        if len(sorted_players) % 2 == 1:
            bye_player = sorted_players.pop()
            matches.append(Match(player_1=bye_player, player_2=None, score_1=1.0, score_2=0.0))

        while sorted_players:
            p1 = sorted_players.pop(0)
            opponents_p1 = self.get_played_opponents(p1)

            p2_match = None
            for i, candidate in enumerate(sorted_players):
                if candidate.national_id not in opponents_p1:
                    p2_match = sorted_players.pop(i)
                    break

            if not p2_match and sorted_players:
                p2_match = sorted_players.pop(0)

            if p2_match:
                matches.append(Match(player_1=p1, player_2=p2_match, score_1=0.0, score_2=0.0))

        return Round(
            name=f"Round {self.current_round_number + 1}",
            matches=matches,
            start_datetime=datetime.now(),
        )
