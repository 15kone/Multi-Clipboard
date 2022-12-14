import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "list":
        print(data)

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")

    elif command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("Data saved!")

    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
