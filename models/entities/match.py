from models.entities.player import Player
from typing import Any


class Match:

    def __init__(
        self, player_1: Player, player_2: Player | None, score_1: float, score_2: float
    ) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

        if player_2 is None:
            self.score_1 = 1.0
            self.score_2 = 0.0

    def set_result(self, result: str) -> Player | None:
        if self.player_2 is None:
            self.score_1 = 1.0
            self.score_2 = 0.0
            return self.player_1

        match result:
            case "1":
                self.score_1 = 1.0
                self.score_2 = 0.0
                return self.player_1
            case "2":
                self.score_1 = 0.0
                self.score_2 = 1.0
                return self.player_2
            case "draw":
                self.score_1 = 0.5
                self.score_2 = 0.5
                return None
            case _:
                raise ValueError("Résultat invalide. Utilisez '1', '2' ou 'draw'.")

    def to_tuple(self) -> tuple[list[Any], list[Any]]:
        p1_data: list[Any] = [self.player_1.to_dict(), self.score_1]
        p2_data: list[Any] = [self.player_2.to_dict() if self.player_2 else None, self.score_2]
        return (p1_data, p2_data)

    def to_dict(self) -> dict[str, Any]:
        return {
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict() if self.player_2 else None,
            "score_1": self.score_1,
            "score_2": self.score_2,
        }

    @classmethod
    def from_tuple(cls, data: Any) -> "Match":
        player_1_data, score_1 = data[0]
        player_2_data, score_2 = data[1]

        return cls(
            player_1=Player(**player_1_data),
            player_2=Player(**player_2_data) if player_2_data else None,
            score_1=float(score_1),
            score_2=float(score_2),
        )
