from models.managers.base_manager import BaseManager
from models.entities.tournament import Tournament


class TournamentManager(BaseManager):

    def __init__(self, file_path: str = "data/tournaments.json") -> None:
        super().__init__(file_path, Tournament)
