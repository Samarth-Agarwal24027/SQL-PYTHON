"""
========================================
CRICKETWORLD DATABASE APPLICATION
========================================

AUTHOR:
- Samarth Agarwal

PURPOSE:
This application allows users to manage cricket data including teams and players.
Users can add, view, search, update, and delete player records stored in a SQLite database.


----------------------------------------
USERS (TARGET AUDIENCE)
----------------------------------------

This application may be used by:

- Cricket fans who want to compare players and teams
- Coaches who want to track player performance data
- Students learning about databases and Python
- Sports analysts who want a simple way to store and retrieve cricket statistics


----------------------------------------
REQUIREMENTS & SPECIFICATIONS
----------------------------------------

FUNCTIONAL REQUIREMENTS:
- User must be able to add player records
- User must be able to view all player records
- User must be able to search players by team
- User must be able to update player details
- User must be able to delete player records

NON-FUNCTIONAL REQUIREMENTS:
- Program must run in Python using VS Code
- Data must be stored in SQLite database
- Program must use a menu-driven interface
- Code must be structured using functions
- Program must handle invalid inputs safely

CONSTRAINTS:
- Maximum 2 tables (team, player)
- No external database hosting required
- No internet/API dependency

SUCCESS CRITERIA:
- All CRUD operations must work correctly
- Database must maintain data integrity
- User interface must be simple and readable



----------------------------------------
FEATURES (FUNCTIONAL REQUIREMENTS)
----------------------------------------
1. Add new player
2. View all players
3. Search players by team
4. Update player information
5. Delete player
6. Exit program

----------------------------------------
DATABASE DESIGN
----------------------------------------

TABLE 1: team
- team_id (INTEGER PRIMARY KEY)
- team_name (TEXT)
- country (TEXT)

TABLE 2: player
- player_id (INTEGER PRIMARY KEY)
- player_name (TEXT)
- role (TEXT)
- runs (INTEGER)
- team_id (INTEGER FOREIGN KEY -> team.team_id)

RELATIONSHIP:
- One team has many players (1-to-many relationship)

----------------------------------------
INPUTS
----------------------------------------
- Player name (string)
- Role (string)
- Runs scored (integer)
- Team selection (integer ID)

----------------------------------------
OUTPUTS
----------------------------------------
- List of players
- Filtered search results
- Confirmation messages (added/updated/deleted)

----------------------------------------
TESTING STRATEGY (SUMMARY)
----------------------------------------
- Normal inputs (valid player data)
- Boundary cases (0 runs, empty input)
- Invalid inputs (text instead of numbers)
- Foreign key tests (invalid team_id)

----------------------------------------
PROGRAM STRUCTURE (TO BE BUILT IN DEVELOPMENT)
----------------------------------------
- connect_database()
- add_player()
- view_players()
- search_players()
- update_player()
- delete_player()
- main_menu()

========================================
"""