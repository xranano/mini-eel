from fetch_api import fetch_locations, fetch_characters, fetch_episodes;
from process_data import process_locations, process_episodes, process_data;
from insert_data import insert_location, insert_episodes, insert_data;

def main():
    # characters
    print("Fetching data...")
    characters = fetch_characters()

    print("Processing data and saving to file...")
    process_data(characters)

    print("Inserting data into the database...")
    insert_data(characters)


    #locations
    print("fetching locations");
    locations = fetch_locations();

    print("processing data");
    process_locations(locations);

    print("inserting data");
    insert_location(locations)

    #episodes
    print("Fetching data...");
    episodes = fetch_episodes();

    print("Processing data...");
    process_episodes(episodes);

    print("Inserting data...");
    insert_episodes(episodes);

if __name__ == "__main__":
    main()