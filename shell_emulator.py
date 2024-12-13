import os
import sys
import zipfile
import csv
from datetime import datetime

class VirtualShell:
    def __init__(self, username, hostname, vfs_path, log_path, startup_script):
        self.username = username
        self.hostname = hostname
        self.current_dir = "/"
        self.log_path = log_path
        self.commands = {
            "ls": self.ls,
            "cd": self.cd,
            "exit": self.exit_shell,
            "whoami": self.whoami,
            "tac": self.tac
        }
        self.vfs = {}
        self.load_vfs(vfs_path)
        self.execute_startup_script(startup_script)

    def log_action(self, command):
        with open(self.log_path, mode='a', newline='') as logfile:
            writer = csv.writer(logfile)
            writer.writerow([datetime.now().isoformat(), self.username, command])

    def load_vfs(self, vfs_path):
        try:
            with zipfile.ZipFile(vfs_path, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    self.vfs[file] = zip_ref.read(file).decode('utf-8')
        except Exception as e:
            print(f"Error loading virtual file system: {e}")
            sys.exit(1)

    def execute_startup_script(self, startup_script):
        if not os.path.exists(startup_script):
            return
        try:
            with open(startup_script, 'r') as script:
                for line in script:
                    self.execute_command(line.strip())
        except Exception as e:
            print(f"Error executing startup script: {e}")

    def ls(self, args):
        dir_content = set()
        for file in self.vfs:
            # Убираем двойные слэши и сравниваем пути корректно
            normalized_file = file.lstrip("/")
            normalized_dir = self.current_dir.lstrip("/")

            # Проверяем, находится ли файл в текущей директории
            if self.current_dir == "/":  # Корневая директория
                relative_path = normalized_file.split("/")[0]
            elif file.startswith(self.current_dir):
                relative_path = file[len(self.current_dir):].strip("/")
            else:
                continue

            # Определяем, это файл или папка
            if "/" in relative_path:
                dir_content.add(relative_path.split("/")[0] + "/")  # Папка
            elif relative_path:
                dir_content.add(relative_path)  # Файл
        print("\n".join(sorted(dir_content)))

    def cd(self, args):
        if len(args) < 1:
            print("cd: missing operand")
            return
        path = args[0]

        if path == "..":  # Переход на уровень выше
            self.current_dir = "/".join(self.current_dir.rstrip("/").split("/")[:-1]) or "/"
        elif path == "/":  # Переход в корень
            self.current_dir = "/"
        else:  # Проверка пути
            if self.current_dir == "/":  # Если находимся в корне
                target_dir = f"{path}/".lstrip("/")
            else:  # Если в подкаталоге
                target_dir = f"{self.current_dir.rstrip('/')}/{path}/".lstrip("/")

            # Проверяем, существует ли путь в VFS
            if any(f.startswith(target_dir) for f in self.vfs):
                self.current_dir = target_dir
            else:
                print(f"cd: no such file or directory: {path}")

    def exit_shell(self, args):
        print("Exiting shell...")
        sys.exit(0)

    def whoami(self, args):
        print(self.username)

    def tac(self, args):
        if len(args) < 1:
            print("tac: missing file operand")
            return
        path = f"{self.current_dir}{args[0]}".lstrip("/")
        if path in self.vfs:
            print("\n".join(self.vfs[path].splitlines()[::-1]))
        else:
            print(f"tac: {args[0]}: No such file")

    def execute_command(self, command_line):
        self.log_action(command_line)
        parts = command_line.split()
        if not parts:
            return
        command, *args = parts
        if command in self.commands:
            self.commands[command](args)
        else:
            print(f"{command}: command not found")

    def start(self):
        while True:
            try:
                command_line = input(f"{self.username}@{self.hostname}:{self.current_dir}$ ")
                self.execute_command(command_line)
            except KeyboardInterrupt:
                print("\nUse 'exit' to leave the shell.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python shell_emulator.py <username> <hostname> <vfs_path> <log_path> <startup_script>")
        sys.exit(1)

    username = sys.argv[1]
    hostname = sys.argv[2]
    vfs_path = sys.argv[3]
    log_path = sys.argv[4]
    startup_script = sys.argv[5]

    shell = VirtualShell(username, hostname, vfs_path, log_path, startup_script)
    shell.start()