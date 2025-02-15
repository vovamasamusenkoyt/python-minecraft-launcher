import minecraft_launcher_lib
import subprocess
import logging
from mods.forge import install_forge, is_forge_installed
from mods.optifine import install_optifine, is_optifine_installed

logger = logging.getLogger("MinecraftLauncher")

def get_versions():
    """
    Получает список всех доступных версий (ванильные, Forge, Optifine).
    """
    try:
        # Ванильные версии
        vanilla_versions = minecraft_launcher_lib.utils.get_version_list()
        release_versions = [v["id"] for v in vanilla_versions if v["type"] == "release"]

        # Forge версии
        forge_versions = ["1.12.2 (Forge)", "1.16.5 (Forge)"]  # Пример версий Forge

        # Optifine версии
        optifine_versions = ["1.12.2 (Optifine)", "1.16.5 (Optifine)"]  # Пример версий Optifine

        # Объединяем все версии
        all_versions = release_versions + forge_versions + optifine_versions
        logger.info("Версии Minecraft успешно загружены.")
        return all_versions
    except Exception as e:
        logger.error(f"Ошибка при загрузке версий: {e}")
        return []

def launch_minecraft(version, minecraft_directory, username):
    """
    Запускает Minecraft (ванильную версию, Forge или Optifine).
    """
    try:
        options = {
            "username": username,
        }

        if "(Forge)" in version:
            # Запуск Forge
            version = version.replace(" (Forge)", "")
            if not is_forge_installed(version, minecraft_directory):
                logger.info(f"Установка Forge для версии {version}...")
                install_forge(version, minecraft_directory)
            command = minecraft_launcher_lib.forge.get_minecraft_command(version, minecraft_directory, options)
        elif "(Optifine)" in version:
            # Запуск Optifine
            version = version.replace(" (Optifine)", "")
            if not is_optifine_installed(version, minecraft_directory):
                logger.info(f"Установка Optifine для версии {version}...")
                install_optifine(version, minecraft_directory)
            command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
        else:
            # Запуск ванильной версии
            command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)

        subprocess.run(command)
        logger.info(f"Запуск Minecraft версии {version}...")
    except Exception as e:
        logger.error(f"Ошибка при запуске Minecraft: {e}")