from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog
from minecraft import get_versions, launch_minecraft
from settings import save_settings
import logging

logger = logging.getLogger("MinecraftLauncher")

class MinecraftLauncherGUI(QWidget):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Minecraft Launcher")
        self.setGeometry(100, 100, 400, 300)

        # Поле для ввода ника
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Введите ник")
        self.username_input.setText(self.settings.get("username", ""))

        # Комбо-бокс для выбора версии
        self.version_combobox = QComboBox(self)
        self.version_combobox.addItems(get_versions())  # Загружаем версии из minecraft.py

        # Кнопка для выбора папки Minecraft
        self.select_folder_button = QPushButton("Выбрать папку Minecraft", self)
        self.select_folder_button.clicked.connect(self.select_folder)

        # Кнопка для запуска игры
        self.play_button = QPushButton("Играть", self)
        self.play_button.clicked.connect(self.start_game)

        # Компоновка интерфейса
        layout = QVBoxLayout(self)
        layout.addWidget(self.username_input)
        layout.addWidget(self.version_combobox)
        layout.addWidget(self.select_folder_button)
        layout.addWidget(self.play_button)

    def select_folder(self):
        """Выбор папки Minecraft."""
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку Minecraft")
        if folder:
            self.settings["minecraft_directory"] = folder
            save_settings(self.settings)
            logger.info(f"Папка Minecraft выбрана: {folder}")

    def start_game(self):
        """Запуск Minecraft."""
        username = self.username_input.text()
        version = self.version_combobox.currentText()
        minecraft_directory = self.settings.get("minecraft_directory", "")

        if not minecraft_directory:
            logger.error("Папка Minecraft не выбрана.")
            return

        # Сохраняем имя пользователя в настройках
        self.settings["username"] = username
        save_settings(self.settings)

        # Запуск игры
        launch_minecraft(version, minecraft_directory, username)