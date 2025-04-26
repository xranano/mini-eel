# Mini ETL Project

This project fetches character and episode data from the [Rick and Morty API](https://rickandmortyapi.com/), processes it, and saves the results into CSV files. The processed data can then be inserted into a PostgreSQL database.

---

## 📦 Project Structure

- `fetch_api.py`: Fetches character and episode data from the API.
- `process_data.py`: Processes and writes the data to CSV files.
- `database.py`: Connects to the PostgreSQL database.
- `insert_data.py`: (Optional) Inserts processed CSV data into the database.

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rick-and-morty-etl.git
   cd rick-and-morty-etl

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

3. **Run the fetch script**
   ```bash
   python fetch_api.py

4. **Run the process script**
   ```bash
   python process_data.py

5. **(Optional) Insert into database**
   ```bash
   python insert_data.py


## 🛠 Requirements
- Python 3.8 or higher
- PostgreSQL installed and running (for database operations)

## ✨ Credits
- API provided by the Rick and Morty API.
