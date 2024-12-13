import unittest
import os
from unittest.mock import patch
from shell_emulator.shell_emulator import VirtualShell

class TestStartupScript(unittest.TestCase):
    def test_startup_script(self):
        # Create a temporary startup script
        startup_script = "test_startup.sh"
        with open(startup_script, "w") as script:
            script.write("whoami\n")
        shell = VirtualShell("testuser", "localhost", "virtual_fs.zip", "test_log.csv", startup_script)
        with patch("builtins.print") as mocked_print:
            shell.execute_startup_script(startup_script)
            mocked_print.assert_any_call("testuser")
        os.remove(startup_script)

if __name__ == "__main__":
    unittest.main()
