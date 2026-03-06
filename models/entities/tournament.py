from datetime import datetime
from typing import Any
import random

from models.entities.player import Player
from models.entities.round import Round
from models.entities.match import Match
from models.managers.base_manager import BaseManager


class Tournament:

    def __init__(
        self,
        name: str,
        venue: str,
        s_date: str | datetime,
        e_date: str | datetime | None,
        description: str,
        current_round_number: int,
        rounds: list[Any],
        players: list[Any],
        number_of_rounds: int = 4,
    ) -> None:
        self.player_manager = BaseManager(Player)
        self.name = name
        self.venue = venue
        self.s_date = (
            datetime.fromisoformat(s_date)
            if isinstance(s_date, str)
            else s_date
        )
        self.e_date = (
            datetime.fromisoformat(e_date)
            if isinstance(e_date, str)
            else e_date
        )
        self.description = description
        self.current_round_number = current_round_number
        self.rounds: list[Round] = [
            r if isinstance(r, Round) else Round(**r) for r in rounds
        ]
        self.players = [
            p if isinstance(p, Player) else self.player_manager.get_by_id(p)
            for p in players
        ]
        self.number_of_rounds = number_of_rounds

    @property
    def e_date_display(self) -> str:
        return self.e_date.strftime("%Y-%m-%d") if self.e_date else "En cours"

    def to_dict(self) -> Any:
        return {
            "name": self.name,
            "venue": self.venue,
            "s_date": self.s_date.isoformat(),
            "e_date": self.e_date.isoformat() if self.e_date else None,
            "description": self.description,
            "current_round_number": self.current_round_number,
            "rounds": [round.to_dict() for round in self.rounds],
            "players": [p.national_id for p in self.players],
            "number_of_rounds": self.number_of_rounds,
        }

    def get_player_score(self, player: Player) -> float:
        score = 0.0

        for round in self.rounds:
            for match in round.matches:
                if match.player_1 == player.national_id:
                    score += match.score_1
                if match.player_2 and match.player_2 == player.national_id:
                    score += match.score_2

        return score

    def get_played_opponents(self, player: Player) -> set[str]:
        opponents: set[str] = set()

        for round in self.rounds:
            for match in round.matches:
                if match.player_2:
                    if player.national_id == match.player_1:
                        opponents.add(match.player_2)
                    elif player.national_id == match.player_2:
                        opponents.add(match.player_1)

        return opponents

    def generate_next_round(self) -> Round:
        sorted_players = sorted(
            self.players, key=self.get_player_score, reverse=True
        )

        if not self.rounds:
            random.shuffle(sorted_players)
        else:
            sorted_players = self._shuffle_tied_players(sorted_players)

        matches: list[Match] = []

        if len(sorted_players) % 2 == 1:
            bye_player = sorted_players.pop()
            matches.append(
                Match(
                    player_1=bye_player.national_id,
                    player_2=None,
                    score_1=1.0,
                    score_2=0.0,
                )
            )

        while sorted_players:
            p1 = sorted_players.pop(0)
            opponents_p1 = self.get_played_opponents(p1)

            p2 = None
            for index, candidate in enumerate(sorted_players):
                if candidate.national_id not in opponents_p1:
                    p2 = sorted_players.pop(index)
                    break

            if not p2 and sorted_players:
                p2 = sorted_players.pop(0)

            matches.append(
                Match(
                    player_1=p1.national_id,
                    player_2=p2.national_id if p2 else None,
                    score_1=0.0,
                    score_2=0.0,
                )
            )

        return Round(
            name=f"Round {self.current_round_number + 1}",
            matches=matches,
            s_datetime=datetime.now(),
        )

    def _shuffle_tied_players(
        self, sorted_players: list[Player]
    ) -> list[Player]:
        result: list[Player] = []
        group: list[Player] = []
        current_score: float | None = None

        for player in sorted_players:
            score = self.get_player_score(player)
            if score != current_score:
                random.shuffle(group)
                result.extend(group)
                group = [player]
                current_score = score
            else:
                group.append(player)

        random.shuffle(group)
        result.extend(group)
        return result
