from models.managers.base_manager import BaseManager
from models.entities.player import Player


class PlayerManager(BaseManager):

    def __init__(self, file_path: str = "data/players.json") -> None:
        super().__init__(file_path, Player)
