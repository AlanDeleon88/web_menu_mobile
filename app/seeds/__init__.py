from flask.cli import AppGroup
from .users import seed_users, undo_users
from .menus import seed_menu, undo_menu
from .sub_menus import seed_sub_menu, undo_sub_menu
from .restaurant import seed_restaurant, undo_restaurant

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_restaurant()
    seed_menu()
    seed_sub_menu()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_sub_menu()
    undo_menu()
    undo_restaurant()
    undo_users()
    # Add other undo functions here
