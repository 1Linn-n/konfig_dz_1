import unittest
from shell_emulator.shell_emulator import VirtualShell

class TestExitCommand(unittest.TestCase):
    def setUp(self):
        self.shell = VirtualShell("testuser", "localhost", "virtual_fs.zip", "test_log.csv", "")

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.shell.exit_shell([])

if __name__ == "__main__":
    unittest.main()
