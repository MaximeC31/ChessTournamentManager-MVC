from models.entities.match import Match
from models.entities.round import Round
from models.entities.player import Player
from models.entities.tournament import Tournament
from models.managers.base_manager import BaseManager
from views.tournament_view import TournamentView
from datetime import datetime
import random


class TournamentController:

    def __init__(self) -> None:
        self.view = TournamentView()
        self.tournament_manager: BaseManager = BaseManager(Tournament)
        self.player_manager: BaseManager = BaseManager(Player)

    def run(self) -> None:
        while True:
            choice = self.view.display_menu()
            match choice:
                case "1":
                    self.create_tournament()
                case "2":
                    self.list_tournaments()
                case "3":
                    # TODO: Implémenter le lancement/reprise d'un tournoi
                    pass
                case "0":
                    break
                case _:
                    self.view.display_invalid_choice()

    def input_match_result(self, match: Match) -> Player | None:
        if match.player_2 is None:
            return match.player_1

        choice = self.view.prompt_match_result(match.player_1, match.player_2)
        return match.set_result(choice)

    def create_first_round(self, players: list[Player]) -> Round:
        shuffled_players = list(players)
        random.shuffle(shuffled_players)

        matches = [
            Match(shuffled_players[i], shuffled_players[i + 1], 0.0, 0.0)
            for i in range(0, len(shuffled_players), 2)
        ]

        new_round = Round(name="Round 1", matches=matches, start_datetime=datetime.now())
        return new_round

    def create_tournament(self) -> None:
        players = self.player_manager.get_all()
        if len(players) < 2:
            self.view.display_message("Il faut au moins 2 joueurs pour créer un tournoi.")
            return

        while True:
            tournament_info = self.view.prompt_tournament_data()
            selected_players = self.view.select_players(players)

            raw_end_date = str(tournament_info["end_date"]).strip()
            final_end_date: str | None = raw_end_date if raw_end_date else None

            try:
                new_tournament = Tournament(
                    name=str(tournament_info["name"]),
                    venue=str(tournament_info["venue"]),
                    start_date=str(tournament_info["start_date"]),
                    end_date=final_end_date,
                    description=str(tournament_info["description"]),
                    current_round_number=int(tournament_info["current_round_number"]),
                    rounds=[],
                    players=selected_players,
                    number_of_rounds=int(tournament_info["rounds"]),
                )
                self.tournament_manager.save(new_tournament)
                self.view.display_message(f"Tournoi '{new_tournament.name}' créé avec succès !")
                break
            except ValueError as e:
                self.view.display_message(
                    f"Erreur de données : {e}. Veuillez recommencer la saisie."
                )

    def list_tournaments(self) -> None:
        tournament_list = self.tournament_manager.get_all()
        self.view.display_tournaments(tournament_list)
