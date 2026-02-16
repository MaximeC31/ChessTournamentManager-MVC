import sys
from views.main_view import MainView
from controllers.player_controller import PlayerController


class MainController:

    def __init__(self) -> None:
        self.view = MainView()

    def run(self) -> None:
        while True:
            choice: str = self.view.display_main_menu()

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
                    self.view.display_message("Choix invalide, veuillez réessayer.")

    def handle_players_menu(self) -> None:
        player_controller = PlayerController()
        player_controller.run()

    def handle_tournaments_menu(self) -> None:
        self.view.display_message("Gérer les tournois")
        pass  # À implémenter : Gérer le menu des tournois

    def handle_reports_menu(self) -> None:
        self.view.display_message("Gérer les rapports")
        pass  # À implémenter : Gérer le menu des rapports

    def exit_application(self) -> None:
        self.view.display_message("Échec et Mat, application terminée !")
        sys.exit(0)
        pass  # À implémenter : Effectuer les opérations de nettoyage avant de quitter
