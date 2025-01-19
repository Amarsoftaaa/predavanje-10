import json


with open("data.json", "r" ) as file:
    data = json.load(file)
    data.append({
        "name": "sejo jukic",
        "age": 310,
        "height": 181,
        "gender": "male"
    })
    print(data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
