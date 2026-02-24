from models.entities.player import Player
from models.entities.tournament import Tournament
from models.managers.base_manager import BaseManager
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self) -> None:
        self.view = TournamentView()
        self.tournament_manager: BaseManager = BaseManager(Tournament)
        self.player_manager: BaseManager = BaseManager(Player)
        self.resolve_tournament_players()

    def run(self) -> None:
        while True:
            choice = self.view.display_menu()

            match choice:
                case "1":
                    self.create_tournament()
                case "2":
                    self.list_tournaments()
                case "3":
                    # 1. Récupérer tous les tournois via le manager
                    # 2. Demander à la vue de sélectionner un tournoi (select_tournament)
                    # 3. Si un tournoi est sélectionné :
                    #    - Appeler self.play_tournament(tournoi_selectionné)
                    pass
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

    # def play_tournament(self, tournament):
    # Boucle principale : tant que le nombre de rounds max n'est pas atteint
    # A. Déterminer si on doit générer un nouveau round
    # B. Récupérer le round actuel (le dernier de la liste)
    # C. Saisir les résultats des matchs restants
    # D. Clôturer le round
    # E. Fin

    def delete_tournament(self) -> None:
        tournaments = self.tournament_manager.get_all()
        tournament_to_delete = self.view.select_tournament(tournaments)

        if not tournament_to_delete:
            self.view.display_deletion_cancelled()
            return

        self.tournament_manager.delete(tournament_to_delete)
        self.view.display_tournament_deleted(tournament_to_delete.name)

    def resolve_tournament_players(self) -> None:
        all_players = self.player_manager.get_all()

        for tournament in self.tournament_manager.get_all():
            matching_players: list[Player] = []

            for p_id in tournament.players:
                for p_full in all_players:
                    if p_full.national_id == p_id:
                        matching_players.append(p_full)
                        break

            tournament.players = matching_players
