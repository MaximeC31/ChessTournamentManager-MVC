from typing import Any
from datetime import datetime
from models.entities.player import Player
from models.entities.tournament import Tournament


class TournamentView:

    def display_menu(self) -> str:
        print("=== GESTION DES TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Lister les tournois")
        print("3. Lancer/Reprendre un tournoi")
        print("4. Supprimer un tournoi")
        print("0. Retour au menu principal")

        choice: str = input("Choisissez une option : ")
        return choice

    def prompt_tournament_data(self) -> dict[str, str | int]:
        print("Créer un nouveau tournoi :")

        input_data: dict[str, str | int] = {}

        input_data["name"] = input("Nom du tournoi : ")
        input_data["venue"] = input("Lieu du tournoi : ")
        input_data["description"] = input("Description du tournoi : ")

        while True:
            s_date = input("Date de début (YYYY-MM-DD) : ")
            try:
                datetime.strptime(s_date, "%Y-%m-%d")
                input_data["s_date"] = s_date
                break
            except ValueError:
                print("Format incorrect. Veuillez recommencer.")

        while True:
            e_date = input("Date de fin (YYYY-MM-DD, optionnel) : ")
            if not e_date:
                input_data["e_date"] = ""
                break
            try:
                datetime.strptime(e_date, "%Y-%m-%d")
                input_data["e_date"] = e_date
                break
            except ValueError:
                print("Format invalide. Laissez vide ou respectez YYYY-MM-DD.")

        rounds_input = input("Nombre de tours (défaut 4) : ")
        input_data["rounds"] = int(rounds_input) if rounds_input.isdigit() else 4
        input_data["current_round_number"] = 0

        return input_data

    def select_players(self, players: list[Player]) -> list[Player]:
        print("Liste des joueurs disponibles :")

        for index, player in enumerate(players, start=1):
            print(f"{index}. {player.first_name} {player.last_name}")

        while True:
            choice = input("Sélectionnez les joueurs (ex: 1,2,3... ou 'all') : ").strip()

            if choice.lower() == "all":
                return players

            try:
                selected_indices = [int(i.strip()) for i in choice.split(",")]
                selected_players = [players[i - 1] for i in selected_indices]
                return selected_players
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez entrer des indices valides ou 'all'.")

    def display_not_enough_players(self) -> None:
        print("Il faut au moins 2 joueurs pour créer un tournoi.")

    def display_tournament_created(self, name: str) -> None:
        print(f"Tournoi '{name}' créé avec succès !")

    def display_tournament_error(self, error: str) -> None:
        print(f"Erreur de données : {error}. Veuillez recommencer la saisie.")

    def display_tournaments(self, tournaments: list[Tournament]) -> None:
        if not tournaments:
            print("Aucun tournoi trouvé.")
            return

        print("Liste des tournois :")
        for t in tournaments:
            e_date = t.e_date.strftime("%Y-%m-%d") if t.e_date else "En cours"
            print(f"- {t.name} | Dates: {t.s_date.strftime('%Y-%m-%d')} - {e_date}")

    def select_tournament(self, tournaments: list[Tournament]) -> Tournament | None:
        if not tournaments:
            print("Aucun tournoi disponible.")
            return None

        print("Sélectionnez un tournoi :")
        for i, tournament in enumerate(tournaments, start=1):
            print(f"{i}. {tournament.name}")

        while True:
            choice = input("Entrez le numéro du tournoi (ou 0 pour annuler) : ").strip()

            if choice == "0":
                return None

            if not choice.isdigit():
                print("Entrée invalide. Veuillez entrer un numéro valide.")
                continue

            choice_index = int(choice) - 1
            if choice_index < 0 or choice_index >= len(tournaments):
                print("Numéro de tournoi invalide. Veuillez réessayer.")
                continue

            return tournaments[choice_index]

    def display_round_name(self, round_name: str) -> None:
        print(f"--- {round_name} ---")

    def prompt_match_result(self, p1: Player, p2: Player | None) -> str:
        p2_name = f"{p2.first_name} {p2.last_name}" if p2 else "BYE"
        print(f"{p1.first_name} {p1.last_name} VS {p2_name}")

        if p2 is None:
            return "1"

        while True:
            result = input(
                f"Entrez le résultat (1 victoire {p1.first_name} {p1.last_name}, "
                f"2 victoire {p2_name}, draw Match nul) : "
            )

            if result not in ["1", "2", "draw"]:
                print("Entrée invalide. Veuillez entrer 1, 2 ou draw.")
                continue

            return result

    def display_match_winner(self, winner: Player) -> None:
        print(f"Vainqueur {winner.first_name} {winner.last_name} !")

    def display_match_draw(self) -> None:
        print("Match nul !")

    def display_tournament_deleted(self, name: str) -> None:
        print(f"Tournoi '{name}' supprimé.")

    def display_deletion_cancelled(self) -> None:
        print("Suppression annulée.")

    def display_invalid_choice(self) -> None:
        print("Choix invalide, veuillez réessayer.")

    def display_ranking(self, players: list[Player], player_score_function: Any) -> None:
        print("\n=== CLASSEMENT ===")
        sorted_players = sorted(players, key=player_score_function, reverse=True)
        for i, player in enumerate(sorted_players, start=1):
            score = player_score_function(player)
            print(f"{i}. {player.first_name} {player.last_name} - {score} pts")
        print("==================\n")
