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
                    self.view.display_invalid_choice()

    def add_player(self) -> None:
        try:
            player_data: dict[str, str] = self.view.prompt_player_info()
            new_player = Player(**player_data)
            self.manager.save(new_player)
            self.view.display_player_added(new_player)
        except ValueError as e:
            self.view.display_player_add_error(e)

    def list_players(self) -> None:
        players: list[Player] = self.manager.get_all()

        if not players:
            self.view.display_no_players_found()
            return

        self.view.display_players(players)

    def search_player(self) -> None:
        target_player = self._find_player_by_id()

        if target_player:
            self.view.display_players([target_player])

    def delete_player(self) -> None:
        target_player = self._find_player_by_id()

        if target_player:
            self.manager.delete(target_player)
            self.view.display_player_deleted(target_player)

    def _find_player_by_id(self) -> Player | None:
        player_id = self.view.prompt_player_national_id()
        players = self.manager.get_all()

        for player in players:
            if player.national_id == player_id:
                return player

        self.view.display_player_not_found()
        return None
