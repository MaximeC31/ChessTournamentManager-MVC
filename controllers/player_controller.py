from models.entities.player import Player
from models.managers.base_manager import BaseManager
from views.player_view import PlayerView


class PlayerController:

    def __init__(self) -> None:
        self.view = PlayerView()
        self.manager = BaseManager(Player)

    def run(self) -> None:
        while True:
            choice: str = self.view.display_menu()

            match choice:
                case "1":
                    self.add_player()
                case "2":
                    self.list_players()
                case "3":
                    self.search_player()
                case "4":
                    self.delete_player()
                case "0":
                    break
                case _:
                    self.view.display_message("Choix invalide, veuillez réessayer.")

    def add_player(self) -> None:
        try:
            player: dict[str, str] = self.view.prompt_player_info()
            new_player = Player(**player)
            self.manager.save(new_player)
            self.view.display_message(
                f"Joueur {new_player.first_name} {new_player.last_name} ajouté avec succès !"
            )
        except ValueError as e:
            self.view.display_error(f"Erreur lors de l'ajout du joueur : {e}")

    def list_players(self) -> None:
        players: list[Player] = self.manager.get_all()

        if not players:
            self.view.display_message("Aucun joueur trouvé.")
            return

        self.view.display_players(players)

    def search_player(self) -> None:
        player_national_id: str = self.view.prompt_player_national_id()
        players: list[Player] = self.manager.get_all()

        target_player = None
        for player in players:
            if player.national_id == player_national_id:
                target_player = player
                break

        if target_player is None:
            self.view.display_message("Aucun joueur trouvé avec cet identifiant.")
            return

        self.view.display_players([target_player])

    def delete_player(self) -> None:
        player_id = self.view.prompt_player_national_id()
        players = self.manager.get_all()

        target_player = None
        for player in players:
            if player.national_id == player_id:
                target_player = player
                break

        if target_player is None:
            self.view.display_message("Erreur : Aucun joueur trouvé avec cet identifiant.")
            return

        self.manager.delete(target_player)
        self.view.display_message(
            f"Joueur {target_player.first_name} {target_player.last_name} supprimé avec succès !"
        )
