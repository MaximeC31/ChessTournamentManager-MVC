from models.entities.player import Player
from models.entities.tournament import Tournament
from models.managers.base_manager import BaseManager
from views.report_view import ReportView


class ReportController:

    def __init__(self) -> None:
        self.view = ReportView()
        self.player_manager: BaseManager = BaseManager(Player)
        self.tournament_manager: BaseManager = BaseManager(Tournament)

    def run(self) -> None:
        while True:
            choice = self.view.display_menu()

            match choice:
                case "1":
                    self.show_all_players_alpha()
                case "2":
                    self.show_all_tournaments()
                case "3":
                    self.show_tournament_details()
                case "4":
                    self.show_tournament_players_alpha()
                case "5":
                    self.show_tournament_rounds_matches()
                case "0":
                    break
                case _:
                    self.view.display_invalid_choice()

    def show_all_players_alpha(self) -> None:
        players = self.player_manager.get_all()
        sorted_players = sorted(players, key=lambda p: p.last_name.lower())
        self.view.display_players_sorted(sorted_players)

        if sorted_players:
            html_content = self.view.generate_players_html(sorted_players)
            self.view.export_to_file("joueurs", html_content)

    def show_all_tournaments(self) -> None:
        tournaments = self.tournament_manager.get_all()
        self.view.display_tournaments_list(tournaments)

        if tournaments:
            html_content = self.view.generate_tournaments_html(tournaments)
            self.view.export_to_file("tournois", html_content)

    def show_tournament_details(self) -> None:
        tournaments = self.tournament_manager.get_all()
        tournament = self.view.select_tournament(tournaments)

        if tournament:
            self.view.display_tournament_details(tournament)
            html_content = self.view.generate_tournament_details_html(tournament)
            self.view.export_to_file(f"tournoi_{tournament.name}", html_content)

    def show_tournament_players_alpha(self) -> None:
        tournaments = self.tournament_manager.get_all()
        tournament = self.view.select_tournament(tournaments)

        if tournament:
            sorted_players = sorted(tournament.players, key=lambda p: p.last_name.lower())
            self.view.display_tournament_players(tournament, sorted_players)

            if sorted_players:
                html_content = self.view.generate_tournament_players_html(
                    tournament, sorted_players
                )
                self.view.export_to_file(f"joueurs_{tournament.name}", html_content)

    def show_tournament_rounds_matches(self) -> None:
        tournaments = self.tournament_manager.get_all()
        tournament = self.view.select_tournament(tournaments)

        if tournament:
            id_map = {p.national_id: p for p in tournament.players}
            self.view.display_rounds_matches(tournament, id_map)
            html_content = self.view.generate_rounds_matches_html(tournament, id_map)
            self.view.export_to_file(f"tours_{tournament.name}", html_content)
