from models.entities.player import Player
from models.entities.tournament import Tournament
from models.managers.base_manager import BaseManager
from views.tournament_view import TournamentView
from datetime import datetime


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
                    selected = self.view.select_tournament(self.tournament_manager.get_all())
                    if selected:
                        self.play_tournament(selected)
                case "4":
                    self.delete_tournament()
                case "0":
                    break
                case _:
                    self.view.display_invalid_choice()

    def create_tournament(self) -> None:
        players = self.player_manager.get_all()

        if len(players) < 2:
            self.view.display_not_enough_players()
            return

        while True:
            tournament_info = self.view.prompt_tournament_data()
            selected_players = self.view.select_players(players)

            raw_e_date = str(tournament_info["e_date"]).strip()
            final_e_date: str | None = raw_e_date if raw_e_date else None

            try:
                new_tournament = Tournament(
                    name=str(tournament_info["name"]),
                    venue=str(tournament_info["venue"]),
                    s_date=str(tournament_info["s_date"]),
                    e_date=final_e_date,
                    description=str(tournament_info["description"]),
                    current_round_number=int(tournament_info["current_round_number"]),
                    rounds=[],
                    players=selected_players,
                    number_of_rounds=int(tournament_info["rounds"]),
                )
                self.tournament_manager.save(new_tournament)
                self.view.display_tournament_created(new_tournament.name)
                break
            except ValueError as e:
                self.view.display_tournament_error(str(e))

    def list_tournaments(self) -> None:
        tournament_list = self.tournament_manager.get_all()
        self.view.display_tournaments(tournament_list)

    def play_tournament(self, tournament: Tournament) -> None:
        if tournament.current_round_number >= tournament.number_of_rounds:
            self.view.display_ranking(tournament.players, tournament.get_player_score)
            return

        while tournament.current_round_number < tournament.number_of_rounds:
            last_round = tournament.rounds[-1] if tournament.rounds else None

            if not last_round or last_round.e_datetime:
                current_round = tournament.generate_next_round()
                tournament.rounds.append(current_round)
                tournament.current_round_number += 1
                self.tournament_manager.save(tournament)
            else:
                current_round = last_round

            self.view.display_round_name(current_round.name)

            for match in current_round.matches:
                if not match.player_2 or (match.score_1 != 0 or match.score_2 != 0):
                    continue

                p1 = self.get_player_by_id(tournament, match.player_1)
                p2 = self.get_player_by_id(tournament, match.player_2)
                result = self.view.prompt_match_result(p1, p2)
                match.set_result(result)
                self.tournament_manager.save(tournament)

            current_round.end_round(datetime.now())
            self.tournament_manager.save(tournament)

        if not tournament.e_date:
            tournament.e_date = datetime.now()
            self.tournament_manager.save(tournament)

        self.view.display_ranking(tournament.players, tournament.get_player_score)

    def delete_tournament(self) -> None:
        tournaments = self.tournament_manager.get_all()
        tournament_to_delete = self.view.select_tournament(tournaments)

        if not tournament_to_delete:
            self.view.display_deletion_cancelled()
            return

        self.tournament_manager.delete(tournament_to_delete)
        self.view.display_tournament_deleted(tournament_to_delete.name)

    def get_player_by_id(self, tournament: Tournament, national_id: str) -> Player:
        for player in tournament.players:
            if player.national_id == national_id:
                return player
        raise ValueError(f"Joueur {national_id} introuvable dans le tournoi.")
