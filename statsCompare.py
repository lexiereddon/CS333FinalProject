
class StatsCompare:
    def compare_players(self, player1_stats, player2_stats):
        result = {}
        keys = ['acs', 'kills', 'deaths','assists']
        for i, key in enumerate(keys):
            if player1_stats[i] > player2_stats[i]:
                result[key] = 'Player1'
            elif player1_stats[i] < player2_stats[i]:
                result[key] = 'Player2'
            else:
                result[key] = 'Tie'
        return result