import os
from models.entities.player import Player
from models.entities.tournament import Tournament


class ReportView:

    def display_menu(self) -> str:
        print("=== RAPPORTS ===")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Nom et dates d'un tournoi donné")
        print("4. Liste des joueurs du tournoi par ordre alphabétique")
        print("5. Liste de tous les tours du tournoi et matchs")
        print("0. Retour au menu principal")

        choice: str = input("Choisissez une option : ")
        return choice

    def display_players_sorted(self, players: list[Player]) -> None:
        if not players:
            self.display_no_players()
            return

        print("=== LISTE DES JOUEURS (ORDRE ALPHABÉTIQUE) ===")
        for player in players:
            print(
                f"ID: {player.national_id} | {player.first_name} {player.last_name} - {player.birth_date}"
            )

    def display_tournaments_list(self, tournaments: list[Tournament]) -> None:
        if not tournaments:
            print("Aucun tournoi trouvé.")
            return

        print("=== LISTE DES TOURNOIS ===")
        for t in tournaments:
            print(
                f"- {t.name} | Lieu: {t.venue} | Dates: {t.s_date.strftime('%Y-%m-%d')} - {t.e_date_display}"
            )

    def display_tournament_details(self, tournament: Tournament) -> None:
        print("=== DÉTAILS DU TOURNOI ===")
        print(f"Nom: {tournament.name}")
        print(f"Lieu: {tournament.venue}")
        print(f"Dates: {tournament.s_date.strftime('%Y-%m-%d')} - {tournament.e_date_display}")
        print(f"Description: {tournament.description}")
        print(f"Tours: {tournament.current_round_number}/{tournament.number_of_rounds}")

    def display_tournament_players(self, tournament: Tournament, players: list[Player]) -> None:
        if not players:
            self.display_no_players()
            return

        print(f"=== JOUEURS DU TOURNOI: {tournament.name} ===")
        for player in players:
            print(f"- {player.first_name} {player.last_name} ({player.national_id})")

    def display_rounds_matches(self, tournament: Tournament, id_map: dict[str, Player]) -> None:
        print(f"=== TOURS ET MATCHS: {tournament.name} ===")

        if not tournament.rounds:
            print("Aucun tour joué pour le moment.")

            return

        for round in tournament.rounds:
            print(f"--- {round.name} ---")
            print(f"Début: {round.s_datetime.strftime('%Y-%m-%d %H:%M')}")
            print(f"Fin: {round.e_datetime_display}")
            print("Matchs:")

            for match in round.matches:
                p1 = id_map.get(match.player_1)
                p1_name = f"{p1.first_name} {p1.last_name}" if p1 else match.player_1
                if match.player_2:
                    p2 = id_map.get(match.player_2)
                    p2_name = f"{p2.first_name} {p2.last_name}" if p2 else match.player_2
                else:
                    p2_name = "BYE"
                print(f"  {p1_name} ({match.score_1}) vs {p2_name} ({match.score_2})")

    def generate_players_html(self, players: list[Player]) -> str:
        html = "<h1>Liste des joueurs (ordre alphabétique)</h1>"
        html += "<ul>"
        for player in players:
            html += f"<li>ID: {player.national_id} | {player.first_name} {player.last_name} - {player.birth_date}</li>"
        html += "</ul>"
        return self._wrap_html(html)

    def generate_tournaments_html(self, tournaments: list[Tournament]) -> str:
        html = "<h1>Liste des tournois</h1>"
        html += "<ul>"
        for t in tournaments:
            html += f"<li>{t.name} | Lieu: {t.venue} | Dates: {t.s_date.strftime('%Y-%m-%d')} - {t.e_date_display}</li>"
        html += "</ul>"
        return self._wrap_html(html)

    def generate_tournament_details_html(self, tournament: Tournament) -> str:
        html = f"<h1>{tournament.name}</h1>"
        html += f"<p><strong>Lieu:</strong> {tournament.venue}</p>"
        html += f"<p><strong>Dates:</strong> {tournament.s_date.strftime('%Y-%m-%d')} - {tournament.e_date_display}</p>"
        html += f"<p><strong>Description:</strong> {tournament.description}</p>"
        html += f"<p><strong>Tours:</strong> {tournament.current_round_number}/{tournament.number_of_rounds}</p>"
        return self._wrap_html(html)

    def generate_tournament_players_html(
        self, tournament: Tournament, players: list[Player]
    ) -> str:
        html = f"<h1>Joueurs du tournoi: {tournament.name}</h1>"
        html += "<ul>"
        for player in players:
            html += f"<li>{player.first_name} {player.last_name} ({player.national_id})</li>"
        html += "</ul>"
        return self._wrap_html(html)

    def generate_rounds_matches_html(
        self, tournament: Tournament, id_map: dict[str, Player]
    ) -> str:
        html = f"<h1>Tours et matchs: {tournament.name}</h1>"

        if not tournament.rounds:
            html += "<p>Aucun tour joué pour le moment.</p>"
            return self._wrap_html(html)

        for round in tournament.rounds:
            html += f"<h2>{round.name}</h2>"
            html += f"<p><strong>Début:</strong> {round.s_datetime.strftime('%Y-%m-%d %H:%M')}</p>"
            html += f"<p><strong>Fin:</strong> {round.e_datetime_display}</p>"
            html += "<h3>Matchs</h3><ul>"

            for match in round.matches:
                p1 = id_map.get(match.player_1)
                p1_name = f"{p1.first_name} {p1.last_name}" if p1 else match.player_1
                if match.player_2:
                    p2 = id_map.get(match.player_2)
                    p2_name = f"{p2.first_name} {p2.last_name}" if p2 else match.player_2
                else:
                    p2_name = "BYE"
                html += f"<li>{p1_name} ({match.score_1}) vs {p2_name} ({match.score_2})</li>"

            html += "</ul>"

        return self._wrap_html(html)

    def select_tournament(self, tournaments: list[Tournament]) -> Tournament | None:
        if not tournaments:
            print("Aucun tournoi trouvé.")
            return None

        print("Sélectionnez un tournoi :")
        for i, tournament in enumerate(tournaments, start=1):
            print(f"{i}. {tournament.name}")

        while True:
            choice = input("Entrez le numéro du tournoi (ou 0 pour annuler) : ").strip()

            if choice == "0":
                return None

            if not choice.isdigit():
                print("Entrée invalide. Veuillez entrer un numéro valide.")
                continue

            choice_index = int(choice) - 1
            if choice_index < 0 or choice_index >= len(tournaments):
                print("Numéro de tournoi invalide. Veuillez réessayer.")
                continue

            return tournaments[choice_index]

    def display_no_players(self) -> None:
        print("Aucun joueur trouvé.")

    def display_invalid_choice(self) -> None:
        print("Choix invalide, veuillez réessayer.")

    def _wrap_html(self, content: str) -> str:
        return f"<!DOCTYPE html><html><body>{content}</body></html>"

    def export_to_file(self, filename: str, content: str) -> None:
        os.makedirs("reports", exist_ok=True)
        filepath = f"reports/{filename}.html"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        self.display_export_success(filepath)

    def display_export_success(self, filepath: str) -> None:
        print(f"Rapport exporté : {filepath}")
