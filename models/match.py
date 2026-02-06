from models.player import Player
from typing import Any


class Match:

    def __init__(self, player_1: Player, player_2: Player, score_1: float, score_2: float) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def set_result(self, result: str) -> None:
        match result:
            case "1":
                self.score_1 = 1.0
                self.score_2 = 0.0
            case "2":
                self.score_1 = 0.0
                self.score_2 = 1.0
            case "draw":
                self.score_1 = 0.5
                self.score_2 = 0.5
            case _:
                raise ValueError("Résultat invalide. Utilisez '1', '2' ou 'draw'.")

    def to_tuple(self) -> tuple[list[Player | float], list[Player | float]]:
        return ([self.player_1, self.score_1], [self.player_2, self.score_2])

    def to_dict(self) -> Any:
        return {
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict(),
            "score_1": self.score_1,
            "score_2": self.score_2,
        }

    @classmethod
    def from_dict(cls, data: Any) -> "Match":
        return cls(
            player_1=Player.from_dict(data["player_1"]),
            player_2=Player.from_dict(data["player_2"]),
            score_1=float(data["score_1"]),
            score_2=float(data["score_2"]),
        )
