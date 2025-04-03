import os

import psycopg2
import requests
from bs4 import BeautifulSoup

# Database connection using environment variable for password
conn = psycopg2.connect(
    dbname="Discs",
    host="localhost",
    port="4000",
)
cur = conn.cursor()

# Sample data for testing
name = "Destroyer"
brand = "Innova"
speed = 12
glide = 5
turn = -1
fade = 3

# Insert into PostgreSQL
insert_query = """
INSERT INTO discs (name, brand, speed, glide, turn, fade)
VALUES (%s, %s, %s, %s, %s, %s)
"""

try:
    cur.execute(insert_query, (name, brand, speed, glide, turn, fade))
    conn.commit()  # Commit the transaction
    print(f"Added {name} to database.")
except Exception as e:
    print(f"Error inserting {name}: {e}")

# Fetch and print inserted data to verify
# Close the connection
cur.close()
conn.close()

print("Database test complete.")
