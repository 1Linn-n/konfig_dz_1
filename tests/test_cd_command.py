import unittest
from unittest.mock import patch
from shell_emulator.shell_emulator import VirtualShell

class TestCdCommand(unittest.TestCase):
    def setUp(self):
        self.shell = VirtualShell("testuser", "localhost", "virtual_fs.zip", "test_log.csv", "")

    def test_cd(self):
        with patch("builtins.print") as mocked_print:
            self.shell.cd(["docs"])
            self.assertEqual(self.shell.current_dir, "/docs/")
            self.shell.cd([".."])  # Go back
            self.assertEqual(self.shell.current_dir, "/")
            mocked_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
