from typing import Any


class MainController:

    def __init__(self) -> None:
        self.view: Any = None  # À implémenter : Initialiser la vue principale

    def run(self) -> None:
        while True:
            choice: str = self.view.method()  # À implémenter : Récupérer le choix de l'utilisateur

            match choice:
                case "1":
                    self.handle_players_menu()
                case "2":
                    self.handle_tournaments_menu()
                case "3":
                    self.handle_reports_menu()
                case "0":
                    self.exit_application()
                    break
                case _:
                    pass  # À implémenter : Gérer les choix invalides

    def handle_players_menu(self) -> None:
        pass  # À implémenter : Gérer le menu des joueurs

    def handle_tournaments_menu(self) -> None:
        pass  # À implémenter : Gérer le menu des tournois

    def handle_reports_menu(self) -> None:
        pass  # À implémenter : Gérer le menu des rapports

    def exit_application(self) -> None:
        pass  # À implémenter : Gérer la fermeture de l'application
