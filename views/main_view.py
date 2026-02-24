class MainView:

    def display_main_menu(self) -> str:
        print(f"=== MENU PRINCIPAL ===")
        print("1 - Gérer les joueurs")
        print("2 - Gérer les tournois")
        print("3 - Gérer les rapports")
        print(f"0 - Quitter l'application")

        choice = input("Veuillez entrer votre choix : ")
        return choice

    def display_exit_message(self) -> None:
        print("Échec et Mat, application terminée !")

    def display_invalid_choice(self) -> None:
        print("Choix invalide, veuillez réessayer.")
