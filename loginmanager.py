
class LoginManager:
    def __init__(self, cursor):
        self.cursor = cursor


    def authenticate(self, username, password):
        self.cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s", (username, password)
        )
        record = self.cursor.fetchone()[0]
        return record > 0
    
    def login(self):
        username = input("Enter username: \n")
        password = input("Enter password: \n")
        if self.authenticate(username, password):
            print(f"\nWelcome, {username}!\n")
            return True
        else:
            print("\nInvalid username or password.\n")
            return False
        
    def register_user(self, username, password):
        self.cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = %s",(username)
        )
        if self.cursor.fetchone()[0] > 0:
            print("Username already exists.")
            return False
        self.cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password)
        )
        print("You have successfully created an account!")
        return True


    def cast_vote(self, user_id, most_unlucky, most_toxic_team, most_tryhard_team):
        self.cursor.execute("SElECT COUNT(*) FROM communityvotes WHERE user_id = %s", (user_id,))
        if self.cursor.fetchone()[0] > 0 :
                return "Sorry, you have already cast your vote. You cannot vote more than once."
        self.cursor.execute(
            "INSERT INTO communityvotes (user_id, most_unlucky, most_toxic_team, most_tryhard_team) VALUES (%s, %s, %s, %s)",(user_id, most_unlucky, most_toxic_team, most_tryhard_team)
        )
        return "Your vote has been cast successfully!"
    

    def get_user_id(self, username):
        self.cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        record = self.cursor.fetchone()
        if record:
            return record[0]
        else:
            return None