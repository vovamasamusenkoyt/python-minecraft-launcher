import json
import os
import logging

logger = logging.getLogger("MinecraftLauncher")

def load_settings():
    """
    Загружает настройки из файла settings.json.
    """
    default_settings = {
        "minecraft_directory": os.path.join(os.path.expanduser("~"), ".minecraft"),
        "username": "Player"
    }

    try:
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as file:
                settings = json.load(file)
                logger.info("Настройки успешно загружены.")
                return {**default_settings, **settings}
        else:
            logger.warning("Файл настроек не найден. Используются настройки по умолчанию.")
            return default_settings
    except Exception as e:
        logger.error(f"Ошибка при загрузке настроек: {e}")
        return default_settings

def save_settings(settings):
    """
    Сохраняет настройки в файл settings.json.
    """
    try:
        with open("settings.json", "w") as file:
            json.dump(settings, file, indent=4)
            logger.info("Настройки успешно сохранены.")
    except Exception as e:
        logger.error(f"Ошибка при сохранении настроек: {e}")