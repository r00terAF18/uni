import argparse
import os
from pathlib import Path
from subprocess import call
from sys import executable, platform

# define constants
BASE_DIR = Path(__file__).resolve().parent
DENY_FOLDER = ["env", "media", "static", "shuut_uni", ".vscode", ".git"]
DJANGO_APPS = []
PYTHON = executable

# helper function to swap indexes in a list
def swap_pos(list_to_swap: list, p1: int, p2: int) -> None:
    """
    Takes in a list and swaps index p1 for index p2 in the given list\n
    Returns void
    """
    list_to_swap[p2], list_to_swap[p1] = list_to_swap[p1], list_to_swap[p2]


def cls():
    if "linux" in platform:
        call("clear")
    else:
        call("cls")


# get a list of installed apps based on being a dir or not
def find_apps():
    for folder in os.listdir(BASE_DIR):
        if os.path.isdir(folder):
            if folder not in DENY_FOLDER:
                DJANGO_APPS.append(folder)

    swap_pos(DJANGO_APPS, 3, 1)
    swap_pos(DJANGO_APPS, 9, 0)

    # 0               1                 2               3           4                   5               6               7           8           9               10              11
    # ['adminpanel', 'conference_app', 'event_app', 'faculty_app', 'general_post_app', 'lecture_app', 'newsletter', 'news_app', 'pages_app', 'professor_app', 'sidebar_app', 'slider_app']


# make migrations for each app
def makemigrations():
    for app in DJANGO_APPS:
        call(f"{PYTHON} manage.py makemigrations {app}")
        # call(f"{PYTHON} manage.py migrate")


# run migrations
def migrate():
    call(f"{PYTHON} manage.py migrate")


# removes all migrations and also remove the db
def reset_migrations():
    for app in DJANGO_APPS:
        mig_folder = BASE_DIR / app / "migrations"
        call(f"rm -r {mig_folder}")
    call(f"rm app_db.db")


# print a sexy ass logo
def logo():
    with open("logo.txt", "r") as f:
        l = f.read()
        f.close()
    print(l)


# main script loop
def main():
    find_apps()
    in_app = True
    while in_app:
        cls()
        logo()
        print("\n")
        print(f"[1] Migrate (Auto)")
        print(f"[2] Reset DB (Auto)")
        print(f"[0] Exit app")
        usr_input = input(">> ")
        if usr_input == "1":
            cls()
            makemigrations()
            migrate()
        elif usr_input == "2":
            cls()
            reset_migrations()
        elif usr_input == "0":
            in_app = False

    cls()
    logo()


if __name__ == "__main__":
    main()
