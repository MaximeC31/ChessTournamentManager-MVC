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
            "first_name": input("Entrez le prénom du joueur : "),
            "last_name": input("Entrez le nom du joueur : "),
            "birth_date": input("Entrez la date de naissance du joueur (YYYY-MM-DD) : "),
            "national_id": input("Entrez l'identifiant national du joueur : "),
        }
        return player_info

    def display_player_added(self, player: Player) -> None:
        print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès !")

    def display_player_add_error(self, error: Exception) -> None:
        print(f"Erreur lors de l'ajout du joueur : {error}")

    def prompt_player_national_id(self) -> str:
        return input("Entrez l'identifiant national du joueur : ")

    def display_players(self, players: list[Player]) -> None:
        for p in players:
            print(f"ID: {p.national_id} | {p.first_name} {p.last_name} - {p.birth_date}")

    def display_no_players_found(self) -> None:
        print("Aucun joueur trouvé.")

    def display_player_not_found(self) -> None:
        print("Erreur : Aucun joueur trouvé avec cet identifiant.")

    def display_player_updated(self, player: Player) -> None:
        print(f"Joueur {player.first_name} {player.last_name} mis à jour avec succès !")

    def display_player_deleted(self, player: Player) -> None:
        print(f"Joueur {player.first_name} {player.last_name} supprimé avec succès !")

    def display_invalid_choice(self) -> None:
        print("Choix invalide, veuillez réessayer.")
