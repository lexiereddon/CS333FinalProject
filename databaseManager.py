
class DatabaseManager:
    def __init__(self,conn):
        self.conn = conn
        self.cur = conn.cursor()

    def get_final_scores(self, team1, team2):
        self.cur.execute("SELECT score_team, score_opp FROM matches WHERE team = %s AND opponent = %s", (team1, team2))
        return self.cur.fetchone()

    def get_player_stats(self, player):
        self.cur.execute("SELECT acs, kill, death, assist FROM playerstats WHERE player = %s", (player,))
        return self.cur.fetchone()
    
    def get_agent_pickrate(self, agent, map_name):
        self.cur.execute( "SELECT pick_rate FROM agentpickrates WHERE agent = %s AND map = %s", (agent, map_name))
        return self.cur.fetchone()
