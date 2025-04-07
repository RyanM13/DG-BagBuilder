import os

import psycopg2
import requests

# Database connection
conn = psycopg2.connect(
    dbname="Discs",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port="4000",
)
cur = conn.cursor()
print("Connected")

# API endpoint for discs
API_URL = "https://discit-api.fly.dev/disc"

# Fetch the disc data
response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()  # Assuming the data is in JSON format

    for disc in data:
        # Extract relevant disc information
        name = disc.get("name", "Unknown")
        brand = disc.get("brand", "Unknown")
        speed = disc.get("speed", 0)
        glide = disc.get("glide", 0)
        turn = disc.get("turn", 0)
        fade = disc.get("fade", 0)
        print(name)
        print(brand)
        print(speed)
        print(glide)
        print(fade)

        # Insert into PostgreSQL
        insert_query = """
        INSERT INTO discs (name, brand, speed, glide, turn, fade)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            cur.execute(insert_query, (name, brand, speed, glide, turn, fade))
            conn.commit()
            print(f"Added {name} to database.")
        except psycopg2.Error as e:
            conn.rollback()  # Rollback to avoid broken transactions

            print(f"Error inserting {name}: {e}")


else:
    print("Failed to fetch data from the API.")

# Close connection
cur.close()
conn.close()

print("Data insertion complete.")
