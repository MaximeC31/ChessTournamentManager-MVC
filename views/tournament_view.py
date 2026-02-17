from models.entities.player import Player


class TournamentView:

    def display_menu(self) -> str:
        print("=== GESTION DES TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Lister les tournois")
        print("3. Lancer/Reprendre un tournoi")
        print("0. Retour au menu principal")

        choice: str = input("Choisissez une option : ")
        return choice

    def prompt_match_result(self, p1: Player, p2: Player) -> str:
        print(f"{p1.first_name} {p1.last_name} VS {p2.first_name} {p2.last_name}")
        while True:
            result = input("Entrez le résultat (1 victoire J1, 2 victoire J2, draw Match nul) : ")

            if result not in ["1", "2", "draw"]:
                print("Entrée invalide. Veuillez entrer 1, 2 ou draw.")
                continue

            return result

    def display_message(self, message: str) -> None:
        print(message)
