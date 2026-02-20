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

    def prompt_match_result(self, p1: Player, p2: Player | None) -> str:
        p2_name = f"{p2.first_name} {p2.last_name}" if p2 else "BYE"
        print(f"{p1.first_name} {p1.last_name} VS {p2_name}")

        if p2 is None:
            return "1"

        while True:
            result = input(
                f"Entrez le résultat (1 victoire {p1.first_name} {p1.last_name}, 2 victoire {p2_name}, draw Match nul) : "
            )

            if result not in ["1", "2", "draw"]:
                print("Entrée invalide. Veuillez entrer 1, 2 ou draw.")
                continue

            return result

    def display_invalid_choice(self) -> None:
        print("Choix invalide, veuillez réessayer.")

    def display_round_name(self, round_name: str) -> None:
        print(f"--- {round_name} ---")

    def display_match_winner(self, winner: Player) -> None:
        print(f"Vainqueur {winner.first_name} {winner.last_name} !")

    def display_match_draw(self) -> None:
        print("Match nul !")

    def display_message(self, message: str) -> None:
        print(message)
