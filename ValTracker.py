#Author: Lexie Reddon
#Date: 5/6/2025
#Purpose: CS 333 Final Project, Interact with a database that tracks Valorant Stats from the Campions 2023 Tournament. 

import psycopg
from loginmanager import LoginManager
from statsCompare import StatsCompare
from databaseManager import DatabaseManager

#connect to database

with psycopg.connect(
        host="localhost",
        port=5432,
        database="testdb",
        user="testuser",
        password="testpass"
    )as conn:
    database_manager = DatabaseManager(conn)
    with conn.cursor() as cur:
        print("This is ValTracker 2.0.")
        print("Welcome to ValTracker!  \nWe have recorded all statistics about the Valorant 2023 Champions Tournament. \n")

        login_manager = LoginManager(cur)
        stats_compare = StatsCompare()
        logged_in = False
        while not logged_in:
            logged_in = login_manager.login()


        cond = 1
        while(cond != 0):

            choice = input("\nPlease choose from the following options: \n 1. View final score of a match \n 2. View stats for a specific player \n 3. View an agent pickrate \n 4. Cast your community vote \n 5. Compare stats for two players \n 6. Exit ValTracker \n")

            if choice == '1':
                team1 = input("You have chosen to view the final score of a match. Please enter the first team: \n")
                team2 = input("Now enter the second team: \n")
                record = database_manager.get_final_scores(team1, team2)
                if record:
                        print("\n", team1, "scored", record[0], "against", team2, "who scored", record[1], "\n \n")
                else:
                    print("\nThere was no result found. Please be sure the team names are correct.\n\n")
            elif choice == '2':
                player = input("You have chosen to see stats for a specific player. Please enter the player's name: \n")
                record = database_manager.get_player_stats(player)
                if record:
                    print("\nThe player",player,"had an acs of", record[0], ",", record[1], "kills,", record[2], "deaths, and", record[3], "assists.\n\n")
                else:
                    print("\nThere was no result found. Please be sure the player's name is correct.\n\n")
            elif choice == '3':
                agent = input("You have chosen to view an agent pickrate. Please first enter the agent: \n")
                map = input("Please enter the map: \n")
                record = database_manager.get_agent_pickrate(agent, map)
                if record:
                        print("\nThe pickrate for the agent",agent, "on ",map,"is", record[0], "%. \n \n")
                else:
                    print("\nThere was no result found. Please be sure the agent name and map name are correct.\n\n")
            elif choice == '4':
                username = input("You have chosen to cast your community votes! First enter your username: \n")
                user_id = login_manager.get_user_id(username)
                if user_id:
                        playerVote = input("Now enter the player name for the 'Most Unlucky Player': \n")
                        toxicTeamVote = input("Now enter the team name for the 'Most Toxic Team': \n")
                        tryhardTeamVote = input("Now enter the team name for the 'Most Tryhard Team': \n")

                        result = login_manager.cast_vote(user_id, playerVote, toxicTeamVote, tryhardTeamVote)

                else:
                        print("Username not found. Please try again.")
            elif choice == '5':
                play1 = input("Type the name of the first player:\n")
                cur.execute("SELECT acs, kill, death, assist FROM playerstats WHERE player = %s", (play1,))
                record1 = cur.fetchone()
                play2 = input("Type the name of the second player:\n")
                cur.execute("SELECT acs, kill, death, assist FROM playerstats WHERE player = %s", (play2,))
                record2 = cur.fetchone()
                if record1 and record2 :
                    PVP = stats_compare.compare_players(record1, record2)
                    for stat, winner in PVP.items():
                        print(f"{winner} has more {stat}")
                else:
                    print("\nThere was no result found. Please be sure the player's names are correct.\n\n")

            elif choice == '6':
                print("Thank you for using ValTracker!")
                cond = 0
            
        conn.commit()