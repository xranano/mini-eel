import requests

def fetch_characters():
    url = "https://rickandmortyapi.com/api/character";
    all_characters = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        all_characters.extend(data['results']);
        url = data['info']['next'];

    return all_characters;

def fetch_locations():
    url = "https://rickandmortyapi.com/api/location";
    all_locations = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        all_locations.extend(data['results']);
        url = data['info']['next'];

    return all_locations;

def fetch_episodes():
    url = "https://rickandmortyapi.com/api/episode";
    all_episodes = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        all_episodes.extend(data['results']);
        url = data['info']['next'];

    return all_episodes;