import unittest 
from unittest.mock import MagicMock
from loginmanager import LoginManager

class TestLoginManager(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = MagicMock()
        self.login_manager = LoginManager(self.mock_cursor)

    def testAuthenticateTrue(self):
        #mock will return 1 meaning the user exists
        self.mock_cursor.fetchone.return_value = [1]
        self.assertTrue(self.login_manager.authenticate('jett', 'dash123'))

    def testAuthenticateFalse(self):
        self.mock_cursor.fetchone.return_value = [0]
        self.assertFalse(self.login_manager.authenticate('jett', 'dash123'))

    def testRegisterTrue(self):
        self.mock_cursor.fetchone.return_value = [0]
        self.assertTrue(self.login_manager.register_user('new_user', 'password'))

    def testRegisterFalse(self):
        self.mock_cursor.fetchone.return_value = [1]
        self.assertFalse(self.login_manager.register_user('new_user', 'password'))


if __name__ == '__main__':
    unittest.main()