import csv

def process_data(characters, filename = "characters.csv"):
    with open(filename, mode= 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["id", "name", "status", "species", "gender", "image", "url", "created"]);

        for character in characters:
            writer.writerow([
                character["id"],
                character["name"],
                character["status"],
                character["species"],
                character["gender"],
                character["image"],
                character["url"],
                character["created"]
            ])

    print(f"data is written to {filename}");

def process_locations(locations, filename = "locations.csv"):
    with open(filename, mode = 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["id", "name", "type", "dimension"]);
        for location in locations:
            writer.writerow([
                location["id"],
                location["name"],
                location["type"],
                location["dimension"]
            ])
    print(f"data is written to {filename}")

def process_episodes(episodes, filename = "episodes.csv"):
    with open(filename, mode = 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["id", "name", "air_date"]);

        for episode in episodes:
            writer.writerow([
                episode["id"],
                episode["name"],
                episode["air_date"]
            ])

    print(f"data is written to {filename}")