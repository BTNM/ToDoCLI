"""ToDo CLI entry point script"""
#todocli/__main__.py

from todocli import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()


