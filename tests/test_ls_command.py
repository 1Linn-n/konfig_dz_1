import unittest
from shell_emulator.shell_emulator import VirtualShell


class TestLSCommand(unittest.TestCase):
    def setUp(self):
        self.shell = VirtualShell("testuser", "localhost", "virtual_fs.zip", "logs/session_log.csv",
                                  "startup_script.sh")

    def test_ls_root(self):
        self.shell.current_dir = "/"
        output = self.shell.ls([])
        self.assertIn("docs/", output)
        self.assertIn("readme.md", output)

    def test_ls_subdirectory(self):
        self.shell.current_dir = "/docs/"
        output = self.shell.ls([])
        self.assertIn("file1.txt", output)
        self.assertIn("file2.txt", output)


if __name__ == "__main__":
    unittest.main()
