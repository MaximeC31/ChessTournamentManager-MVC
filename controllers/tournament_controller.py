from models.entities.match import Match
from models.entities.round import Round
from models.entities.player import Player
from views.tournament_view import TournamentView
from datetime import datetime
import random


class TournamentController:

    def __init__(self) -> None:
        self.view = TournamentView()

    def run(self) -> None:
        while True:
            choice = self.view.display_menu()
            match choice:
                case "1":
                    # TODO: Implémenter la création de tournoi
                    pass
                case "2":
                    # TODO: Implémenter la liste des tournois
                    pass
                case "3":
                    # TODO: Implémenter le lancement/reprise d'un tournoi
                    pass
                case "4":
                    from models.managers.base_manager import BaseManager

                    players = BaseManager(Player).get_all()

                    new_round = self.create_first_round(players)
                    self.view.display_message(new_round.name)

                    for match in new_round.matches:
                        winner = self.input_match_result(match)

                        if winner is None:
                            self.view.display_message("Match nul !")
                            continue

                        self.view.display_message(
                            f"Vainqueur {winner.first_name} {winner.last_name} !"
                        )
                case "0":
                    break
                case _:
                    self.view.display_message("Choix invalide, veuillez réessayer.")

    def create_first_round(self, players: list[Player]) -> Round:
        shuffled_players = list(players)
        random.shuffle(shuffled_players)

        matches = [
            Match(shuffled_players[i], shuffled_players[i + 1], 0.0, 0.0)
            for i in range(0, len(shuffled_players), 2)
        ]

        new_round = Round(name="Round 1", matches=matches, start_datetime=datetime.now())
        return new_round

    def input_match_result(self, match: Match) -> Player | None:
        choice = self.view.prompt_match_result(match.player_1, match.player_2)
        return match.set_result(choice)
