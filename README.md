# Shell Emulator

## Описание
Эмулятор UNIX-подобной оболочки, поддерживающий команды `ls`, `cd`, `exit`, `whoami`, и `tac`.

## Описание всех функций и настроек

### Функции

- **ls**: Показывает содержимое текущего каталога.
- **cd**: Перемещается между каталогами виртуальной файловой системы.
- **whoami**: Выводит имя текущего пользователя.
- **tac**: Выводит содержимое файла в обратном порядке построчно.
- **exit**: Завершает работу эмулятора.
- **execute_startup_script**: Выполняет команды из файла стартового скрипта.
- **log_action**: Логирует действия пользователя в CSV-файл.

### Настройки

Программа запускается с использованием следующих аргументов командной строки:

1. `username`: Имя пользователя для эмулятора.
2. `hostname`: Имя хоста для отображения в приглашении.
3. `vfs_path`: Путь к архиву ZIP, содержащему виртуальную файловую систему.
4. `log_path`: Путь к CSV-файлу для логирования команд.
5. `startup_script`: Путь к скрипту, выполняемому при старте.

Пример конфигурации:

```sh
python shell_emulator.py meizu localhost virtual_fs.zip logs/session_log.csv startup_script.sh
```

## Описание команд для сборки проекта

### Установка зависимостей

```sh
pip install -r requirements.txt
```

### Запуск Shell Emulator

```sh
python shell_emulator.py <username> <hostname> <vfs_path> <log_path> <startup_script>
```

Пример:

```sh
python shell_emulator.py user1 myhost virtual_fs.zip logs/session_log.csv startup_script.sh
```

## Примеры использования

### Пример файловой структуры

Пример содержимого архива `virtual_fs.zip`:

```sh
/
├── docs/
│   └── file2.txt
├── conf/
│   └── conf.txt
├── file1.txt
└── readme.md
```

### Команды Shell Emulator

1. **`ls`**  
   Показывает содержимое текущего каталога:  
   user1@myhost:/docs$ ls  
   file2.txt  

2. **`cd`**  
   Переходит в указанный каталог:  
   user1@myhost:/$ cd docs  
   user1@myhost:/docs$ ls  
   file2.txt  

3. **`whoami`**  
   Выводит имя пользователя:  
   user1@myhost:/$ whoami  
   user1  

4. **`tac`**  
   Выводит содержимое файла в обратном порядке:  
   user1@myhost:/docs$ tac file2.txt  
   (обратный порядок строк файла)

5. **`exit`**  
   Завершает эмулятор:  
   user1@myhost:/docs$ exit  
   Exiting shell...

## Результаты прогона тестов

Для тестирования функционала выполните:

```sh
python -m unittest discover
```

### Пример вывода тестов

```sh
Loaded file: conf/conf.txt
Loaded file: docs/file1.txt
Loaded file: file2.txt
Loaded file: readme.md
Startup script not found or not provided.
.Loaded file: conf/conf.txt
Loaded file: docs/file1.txt
Loaded file: file2.txt
Loaded file: readme.md
Startup script not found or not provided.
Exiting shell...
.Loaded file: conf/conf.txt
Loaded file: docs/file1.txt
Loaded file: file2.txt
Loaded file: readme.md
testuser
conf
docs
file2.txt
readme.md
file1.txt
Hello from file1!
Welcome to file2.
Exiting shell...
conf
docs
file2.txt
readme.md
.Loaded file: conf/conf.txt
Loaded file: docs/file1.txt
Loaded file: file2.txt
Loaded file: readme.md
testuser
conf
docs
file2.txt
readme.md
file1.txt
Hello from file1!
Welcome to file2.
Exiting shell...
file1.txt
.Loaded file: conf/conf.txt
Loaded file: docs/file1.txt
Loaded file: file2.txt
Loaded file: readme.md
testuser
.Loaded file: conf/conf.txt
Loaded file: docs/file1.txt
Loaded file: file2.txt
Loaded file: readme.md
Startup script not found or not provided.
.Loaded file: conf/conf.txt
Loaded file: docs/file1.txt
Loaded file: file2.txt
Loaded file: readme.md
Startup script not found or not provided.
.
----------------------------------------------------------------------
Ran 7 tests in 0.020s

OK
```
