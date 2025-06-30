# 🌦️ Weather-Data-ETL-Pipeline 

This project is an **ETL (Extract, Transform, Load) pipeline** that fetches weather forecast data from a public API, processes it, and stores it in a local SQLite database for analysis and querying.

---

## 📊 What Is ETL and How It Applies Here?
ETL stands for Extract, Transform, Load, and it's a common data engineering process used to gather, clean, and store data for analysis or further use.

In this project:

🟢 Extract: The script fetches hourly weather forecast data in JSON format from the Open-Meteo API. This raw data includes timestamps and temperature readings.

🟡 Transform: Using pandas, the raw data is transformed into a clean, tabular structure. It renames columns, formats timestamps, and prepares the data for analysis (e.g., converting to a proper datetime format).

🔵 Load: The cleaned dataset is then loaded into a local SQLite database using SQLAlchemy. This makes it easy to query and analyze the data using SQL.

This structure makes the project modular, easy to expand (e.g., adding new cities or weather metrics), and ready for integration with dashboards or further analytics.


## 🗄️ Database Structure

Table `clima` columns:

| Column       | Type     | Description                    |
|--------------|----------|--------------------------------|
| time         | datetime | Timestamp of the weather data |
| temp_celsius | float    | Temperature in Celsius degrees |

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- SQLAlchemy
- SQLite (embedded local database)
- Requests (for API calls)

## ⚙️ How It Works

1. **Extract**: Downloads hourly temperature forecast data for Buenos Aires from [Open-Meteo](https://open-meteo.com/).
2. **Transform**: Processes the JSON response to extract and clean relevant data.
3. **Load**: Inserts the data into the `clima` table inside a SQLite database (`data/clima.db`).


   
