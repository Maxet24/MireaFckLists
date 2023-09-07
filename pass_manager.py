import secrets
import json
import os
from datetime import datetime

SESSION_FILE = "pary.json"
# SESSION_FILE = "/home/maxet24mirea/mysite/pary.json"

def generate_random_hash(length=16):
    """Generate a random hash of specified length."""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def create_paru(entry_datetime, subject):
    random_hash = generate_random_hash()

    if os.path.exists(SESSION_FILE):

        with open(SESSION_FILE, 'r') as file:
            hash_dict = json.load(file)

        with open(SESSION_FILE, "w") as file:
            hash_dict[random_hash] = {
                'entry_datetime': entry_datetime.strftime("%d/%m/%y %H:%M"),
                'subject': subject,
                'botaniki': []
            }
            json.dump(hash_dict, file, indent=4)
    else:
        with open(SESSION_FILE, "w") as file:
            hash_dict = {random_hash: {
                'entry_datetime': entry_datetime.strftime("%d/%m/%y %H:%M"),
                'subject': subject,
                'botaniki': []
            }}
            json.dump(hash_dict, file, indent=4)

    return random_hash

def add_botanik(para_hash, vk_user_id, entry_datetime):
    """Add a list of messages to the session identified by the hash key."""

    if not os.path.exists(SESSION_FILE):
        return

    with open(SESSION_FILE, "r+") as file:
        data = json.load(file)

        if para_hash in data:

            botanik = {
                'vk_user_id': vk_user_id,
                'entry_datetime': entry_datetime.strftime("%d/%m/%y %H:%M")
            }

            if vk_user_id not in [i['vk_user_id'] for i in data[para_hash].setdefault("botaniki", [])]:
                data[para_hash].setdefault("botaniki", []).append(botanik)
                file.seek(0)  # Move the file cursor to the beginning
                json.dump(data, file, indent=4)
                file.truncate()  # Remove any remaining content
            else:
                print("Already registered.")
        else:
            print("Para not found.")

def get_botaniki(hash_key):
    if not os.path.exists(SESSION_FILE):
        return {}

    with open(SESSION_FILE, "r") as file:
        data = json.load(file)
        if hash_key in data:
            return data[hash_key]
        else:
            return {}

def get_name_by_vk_id(vk_user_id):
    kenty_by_id = {
        '359450337': 'Глебов Максим',
        '320931282': 'Чабыкина Милада',
        '404640623': 'Бочкарев Лев',
        '295872959': 'Братищев Тимофей',
        '233200579': 'Махоткин Максим',
        '325807393': 'Минакова Рита',
        '343623138': 'Бердиева Милена',
        '475165162': 'Владислав Кузьмин',
        '309697499': 'Мерзляков Ваня',
        '252225185': 'Пантюхин Илья',
        '625438809': 'Поляков Глеб',
        '544184059': 'Мухаметзянов Данис',
        '751518788': 'Морозов Федор',
        '390777779': 'Симин Вадим',
        '220020101': 'Сердюк Никита',
        '413680055': 'Артюхин Никита',
        '349307490': 'Кратов Антон',
        '675122892': 'Хуриева Аня',
        '430753343': 'Погосян Аня',
        '452443586': 'Кудров Вадим',
        '413900461': 'Прохоренко Коля',
        '166276158': 'Соболев Никита',
        '748008601': 'Беженарь Тимур',
        '647993774': 'Халиман Дмитрий',
        '817978267': 'Комягин Михаил',
        '368832955': 'Мерченко Семён',
        '457004557': 'Петрушов Иван'
    }

    return kenty_by_id.setdefault(str(vk_user_id), 'Unknown')

def del_botaniki(para_hash):

    if not os.path.exists(SESSION_FILE):
        return

    with open(SESSION_FILE, "r+") as file:
        data = json.load(file)

        if para_hash in data:
            data[para_hash]['botaniki'] = []
            file.seek(0)  # Move the file cursor to the beginning
            json.dump(data, file, indent=4)
            file.truncate()  # Remove any remaining content

if __name__ == "__main__":
    # add_botanik("XeFEWhN74nQ7jhIp", "359450337", datetime.strptime("07/09/23 12:41", "%d/%m/%y %H:%M"))
    # create_paru(datetime.strptime("07/09/23 14:20", "%d/%m/%y %H:%M"), 'phs_lab')
    # get_botaniki("XeFEWhN74nQ7jhIp")
    # print(get_name_by_vk_id(457004557))
    # del_botaniki('ksc4eHDjjPNSmtU9');
    pass


# geo_lec geo_pra phy_pra