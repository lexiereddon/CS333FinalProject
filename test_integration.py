import unittest
import psycopg
from unittest.mock import MagicMock
from loginmanager import LoginManager
from databaseManager import DatabaseManager
from statsCompare import StatsCompare

class test_integration(unittest.TestCase):
    def setUp(self):
        self.conn = psycopg.connect("host=localhost port=5432 dbname=valorantProPlay")
        self.db_manager = DatabaseManager(self.conn)
        self.cur = self.conn.cursor()
        self.login_manager = LoginManager(self.cur)
        self.stats_compare = StatsCompare()

    def test_get_final_scores(self):
        result = self.db_manager.get_final_scores('ZETA', 'DRX')
        self.assertEqual(result, (5, 13))

    def test_get_player_stats(self):
        result = self.db_manager.get_player_stats('Foxy9')
        self.assertEqual(result, (178,13,13,0))


    def test_get_agent_pickrate(self):
        result = self.db_manager.get_agent_pickrate('viper','Haven')
        self.assertEqual(result, (0.25,))


    def testfullFlow(self):
        self.assertTrue(self.login_manager.authenticate('jett','dash123'))
        self.assertFalse(self.login_manager.authenticate('jettnumberonefan','dash12312'))
        result = self.db_manager.get_agent_pickrate('fade', 'Haven')
        self.assertEqual(result, (0.25,))

    def testCompStats(self):
        expected_result = {
            'acs': 'Player1',
            'kills': 'Player1',
            'deaths': 'Player2',
            'assists': 'Player2'
        }
        pResult1 = self.db_manager.get_player_stats('Foxy9')
        pResult2 = self.db_manager.get_player_stats('Carpe')
        result = self.stats_compare.compare_players(pResult1, pResult2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()