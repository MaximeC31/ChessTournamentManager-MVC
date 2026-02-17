from models.entities.match import Match
from views.tournament_view import TournamentView


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
                case "0":
                    break
                case _:
                    self.view.display_message("Choix invalide, veuillez réessayer.")

    def input_match_result(self, match: Match) -> None:
        choice = self.view.prompt_match_result(match.player_1, match.player_2)
        match.set_result(choice)
