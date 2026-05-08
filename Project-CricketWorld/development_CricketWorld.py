"""
========================================
CRICKETWORLD DATABASE APPLICATION
DEVELOPMENT PHASE
========================================

This program connects to a SQLite database and allows users
to manage cricket players and teams using a menu-driven system.

Features:
- Add player
- View all players
- Search by team
- Update player
- Delete player
========================================
"""

import sqlite3

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
DB_NAME = r"C:\Users\Samarth\Documents\sql-python\Project-CricketWorld\CricketWorld"
print("DB path:", DB_NAME)


def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn


# -----------------------------
# ADD PLAYER
# -----------------------------
def add_player():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter player name: ")
    role = input("Enter role: ")
    runs = int(input("Enter runs: "))
    team_id = int(input("Enter team ID: "))

    cursor.execute("""
        INSERT INTO player (player_name, role, runs, team_id)
        VALUES (?, ?, ?, ?)
    """, (name, role, runs, team_id))

    conn.commit()
    conn.close()
    print("Player added successfully!")


# -----------------------------
# VIEW ALL PLAYERS
# -----------------------------
def view_players():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT player.player_id, player.player_name, player.role, player.runs, team.team_name
        FROM player
        JOIN team ON player.team_id = team.team_id
    """)

    rows = cursor.fetchall()

    print("\n--- PLAYER LIST ---")
    for row in rows:
        print(row)

    conn.close()


# -----------------------------
# SEARCH BY TEAM
# -----------------------------
def search_by_team():
    conn = connect_db()
    cursor = conn.cursor()

    team_name = input("Enter team name: ")

    cursor.execute("""
        SELECT player.player_name, player.role, player.runs
        FROM player
        JOIN team ON player.team_id = team.team_id
        WHERE team.team_name = ?
    """, (team_name,))

    results = cursor.fetchall()

    print("\n--- SEARCH RESULTS ---")
    for r in results:
        print(r)

    conn.close()


# -----------------------------
# UPDATE PLAYER
# -----------------------------
def update_player():
    conn = connect_db()
    cursor = conn.cursor()

    player_id = int(input("Enter player ID to update: "))
    new_runs = int(input("Enter new runs: "))

    cursor.execute("""
        UPDATE player
        SET runs = ?
        WHERE player_id = ?
    """, (new_runs, player_id))

    conn.commit()
    conn.close()
    print("Player updated successfully!")


# -----------------------------
# DELETE PLAYER
# -----------------------------
def delete_player():
    conn = connect_db()
    cursor = conn.cursor()

    player_id = int(input("Enter player ID to delete: "))

    cursor.execute("""
        DELETE FROM player
        WHERE player_id = ?
    """, (player_id,))

    conn.commit()
    conn.close()
    print("Player deleted successfully!")


# -----------------------------
# MAIN MENU
# -----------------------------
def main():
    while True:
        print("\n===== CRICKETWORLD MENU =====")
        print("1. Add Player")
        print("2. View Players")
        print("3. Search by Team")
        print("4. Update Player")
        print("5. Delete Player")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            view_players()
        elif choice == "3":
            search_by_team()
        elif choice == "4":
            update_player()
        elif choice == "5":
            delete_player()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# -----------------------------
# RUN PROGRAM
# -----------------------------
if __name__ == "__main__":
    main()