from models.entities.player import Player


class PlayerView:

    def display_menu(self) -> str:
        print("=== GESTION DES JOUEURS ===")
        print("1. Ajouter un joueur")
        print("2. Lister les joueurs")
        print("3. Rechercher un joueur")
        print("4. Supprimer un joueur")
        print("0. Retour au menu principal")

        choice: str = input("Choisissez une option : ")
        return choice

    def prompt_player_info(self) -> dict[str, str]:
        player_info: dict[str, str] = {
            "last_name": input("Entrez le nom du joueur : "),
            "first_name": input("Entrez le prénom du joueur : "),
            "birth_date": input("Entrez la date de naissance du joueur (YYYY-MM-DD) : "),
            "national_id": input("Entrez l'identifiant national du joueur : "),
        }
        return player_info

    def display_players(self, players: list[Player]) -> None:
        for player in players:
            print(
                f"ID: {player.national_id} | {player.first_name} {player.last_name} {player.birth_date}"
            )

    def prompt_player_national_id(self) -> str:
        return input("Entrez l'identifiant national du joueur : ")

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, error: str) -> None:
        print(f"Erreur : {error}")
