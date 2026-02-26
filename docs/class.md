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
        +list matches
        +end_round(value)
        +to_dict() dict
    }

    class Match {
        +Player player_1
        +Player player_2
        +float score_1
        +float score_2
        +set_result(result) Player
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
        +list rounds
        +list players
        +str description
        +to_dict() dict
        +get_player_score(player) float
        +get_played_opponents(player) set
        +generate_next_round() Round
    }

    Tournament "1" *-- "many" Round
    Tournament "1" *-- "many" Player
    Round "1" *-- "many" Match
    Match "1" o-- "2" Player
```
