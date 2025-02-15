import sys
from PyQt5.QtWidgets import QApplication
from gui import MinecraftLauncherGUI
from settings import load_settings
from logger import setup_logger

def main():
    # Настройка логирования
    logger = setup_logger()

    # Загрузка настроек
    settings = load_settings()

    # Создаём объект QApplication
    app = QApplication(sys.argv)

    # Создаём и показываем окно лаунчера
    launcher_window = MinecraftLauncherGUI(settings)
    launcher_window.show()

    # Запуск главного цикла приложения
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()