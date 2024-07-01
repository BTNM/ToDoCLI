import configparser
from pathlib import Path
import typer
from todocli import DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

def init_app(db_path: str) -> int:
    """Initialize the application."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code
    return SUCCESS