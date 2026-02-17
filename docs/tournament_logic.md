classDiagram
    class Tournament {
        +String name
        +String venue
        +DateTime start_date
        +DateTime end_date
        +String description
        +int current_round_number
        +List rounds
        +List players
        +int number_of_rounds
        +to_dict()
    }
    class Round {
        +String name
        +List matches
        +DateTime start_datetime
        +DateTime end_datetime
        +end_round(DateTime)
        +to_dict()
    }
    class Match {
        +Player player_1
        +Player player_2
        +float score_1
        +float score_2
        +set_result(String)
        +to_tuple()
        +to_dict()
        +from_tuple(data)
    }
    class Player {
        +String last_name
        +String first_name
        +String birth_date
        +String national_id
        +to_dict()
    }
    class BaseManager {
        +model_class
        +String file_path
        +List data
        +save(instance)
        +get_all()
        +delete(instance)
    }
    class TournamentController {
        +TournamentView view
        +BaseManager tournament_manager
        +BaseManager player_manager
        +run()
        +create_tournament()
        +play_tournament()
        +generate_rounds()
    }
    class TournamentView {
        +display_menu()
        +prompt_tournament_info()
        +display_tournaments(list)
        +display_round(round)
    }

    Tournament "1" *-- "*" Round
    Round "1" *-- "*" Match
    Match "1" o-- "2" Player
    TournamentController --> TournamentView
    TournamentController --> BaseManager
    TournamentController ..> Tournament
