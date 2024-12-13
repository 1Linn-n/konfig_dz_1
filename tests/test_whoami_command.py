import unittest
from unittest.mock import patch
from shell_emulator.shell_emulator import VirtualShell

class TestWhoamiCommand(unittest.TestCase):
    def setUp(self):
        self.shell = VirtualShell("testuser", "localhost", "virtual_fs.zip", "test_log.csv", "")

    def test_whoami(self):
        with patch("builtins.print") as mocked_print:
            self.shell.whoami([])
            mocked_print.assert_called_with("testuser")

if __name__ == "__main__":
    unittest.main()
