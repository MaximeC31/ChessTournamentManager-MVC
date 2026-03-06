# Modèles UML - Gestionnaire de Tournoi d'Échecs

```mermaid
classDiagram
    class Player {
        +str last_name
        +str first_name
        +str birth_date
        +str national_id
        +validate_birth_date(value) str
        +validate_national_id(value) str
        +to_dict() dict
    }

    class Round {
        +str name
        +datetime s_datetime
        +datetime e_datetime
        +list~Match~ matches
        +end_round(value)
        +e_datetime_display() str
        +to_dict() dict
    }

    class Match {
        +str player_1
        +str player_2
        +float score_1
        +float score_2
        +set_result(result) str
        +to_tuple() tuple
        +to_dict() dict
        +from_tuple(data) Match
    }

    class Tournament {
        +str name
        +str venue
        +datetime s_date
        +datetime e_date
        +int number_of_rounds
        +int current_round_number
        +list~Round~ rounds
        +list~Player~ players
        +str description
        +e_date_display() str
        +to_dict() dict
        +get_player_score(player) float
        +get_played_opponents(player) set
        +generate_next_round() Round
        +_shuffle_tied_players(sorted_players) list
    }

    Tournament "1" *-- "many" Round
    Tournament "1" *-- "many" Player
    Round "1" *-- "many" Match
```
