import json
import requests
from dotenv import dotenv_values
from magtifun.magtifun_oop import MagtiFun

config = dotenv_values(".env")


def read_users_from_file():
    with open("vin.json") as users_file:
        users = json.load(users_file)
    return users


def check_user_win(user):
    response = requests.get(f"https://stopcov-api.lotto.ge/Public/Winnings/{user['id']}")
    if response.status_code != 200:
        print(f"Can't retrieve the win status for user {user['name']}")
        return "lost"
    return "won" if response.json() else "did not win"


def send_message_with_status(user, user_status):
    status_geo = "მოიგე" if user_status == "won" else "ვერ მოიგე"
    message = "აიცერი და მოიგეს გათამაშებაში მონაწილე"\
        f" {user['name_ge']}: {status_geo}"\
        f"\nStopcov lottery participant {user['name']}: {user_status}"
    print(message)
    mf = MagtiFun(config["MAGTIFUN_USER"], config["MAGTIFUN_PASSWORD"])
    mf.login()
    mf.send_messages(user["phone"], message)


def main():
    users = read_users_from_file()
    for user in users:
        user_status = check_user_win(user)
        send_message_with_status(user, user_status)

if __name__ == "__main__":
    main()