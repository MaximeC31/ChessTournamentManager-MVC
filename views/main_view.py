class MainView:
    GREY = "\033[90m"
    RESET = "\033[0m"

    def display_main_menu(self) -> str:
        print(f"{self.GREY}=== MENU PRINCIPAL ===")
        print("1 - Gérer les joueurs")
        print("2 - Gérer les tournois")
        print("3 - Gérer les rapports")
        print(f"0 - Quitter{self.RESET}")

        choice = input("Veuillez entrer votre choix : ")
        return choice

    def display_invalid_choice(self) -> None:
        print("Choix invalide, veuillez réessayer.")

    def display_exit_message(self) -> None:
        print("Échec et Mat, application terminée !")
