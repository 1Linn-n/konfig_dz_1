import unittest
from unittest.mock import patch
from shell_emulator.shell_emulator import VirtualShell

class TestTacCommand(unittest.TestCase):
    def setUp(self):
        self.shell = VirtualShell("testuser", "localhost", "virtual_fs.zip", "test_log.csv", "")

    def test_tac(self):
        with patch("builtins.print") as mocked_print:
            self.shell.tac(["readme.md"])
            mocked_print.assert_called()  # Ensures output is printed

if __name__ == "__main__":
    unittest.main()
