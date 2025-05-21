# MySQL code to create the db and all:

import os
import json
import pymysql
from datetime import datetime
from logger import create_log
from dotenv import load_dotenv


# -----------------------------------------------------------------------------
# Decide database and define connection:
# -----------------------------------------------------------------------------

load_dotenv()

DB_MODE = os.environ.get("DB_MODE")
create_log("DB", f"Using Database Mode: {DB_MODE}")

# Determine DB configuration based on mode
try:
    # Local MySQL Database:
    if DB_MODE == 'local':
        DB_CONFIG = {
            "host": os.environ.get("LOCAL_DB_HOST"),
            "user": os.environ.get("LOCAL_DB_USER"),
            "password": os.environ.get("LOCAL_DB_PASSWORD"),
            "db": os.environ.get("LOCAL_DB_DB"),
            "charset": os.environ.get("LOCAL_DB_CHARSET"),
        }

    # Remote MySQL Database (RDS):
    elif DB_MODE == 'remote':
        DB_CONFIG = {
            "host": os.environ.get("DB_HOST"),
            "user": os.environ.get("DB_USER"),
            "password": os.environ.get("DB_PASSWORD"),
            "db": os.environ.get("DB_DB"),
            "charset": os.environ.get("DB_CHARSET"),
        }

    def get_db_connection():
        if DB_MODE in ['local', 'remote']:
            return pymysql.connect(**DB_CONFIG)         # type: ignore
        else:
            raise Exception("DB_MODE not set correctly in .env file.")

except Exception as e:
    print(f"Database connection error: {e}")
    create_log("DB", f"Database connection error: {e}")
    # exit(1)


# -------------------------------------------------------------------------------------
# Database:
# -------------------------------------------------------------------------------------

# Clear entire database:
def clear_db():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DROP TABLE IF EXISTS LOCATIONS")
                cur.execute("DROP TABLE IF EXISTS MAPS")
                cur.execute("DROP TABLE IF EXISTS LOCATION_DETAILS")
                conn.commit()
        create_log("DB", "Database cleared successfully.")
    except Exception as e:
        create_log("DB", f"Error clearing database: {e}")


# -------------------------------------------------------------------------------------
# Tables Management:
# -------------------------------------------------------------------------------------

# Create the Locations table to hold the basic data:
def create_locations():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS LOCATIONS (
                        id INT PRIMARY KEY,
                        name TEXT,
                        location TEXT,
                        image TEXT,
                        image2 TEXT,
                        image3 TEXT,
                        image4 TEXT
                    )
                    """
                )
            conn.commit()
    except Exception as e:
        create_log("DB", f"Error creating LOCATIONS table: {e}")


# Create the Maps table to hold the map data for the location:
def create_maps():
    create_log("DB", "Creating the table MAPS.")
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS MAPS (
                        id INT PRIMARY KEY,
                        location_id INT,
                        map_iframe TEXT,
                        latitude FLOAT,
                        longitude FLOAT,
                        FOREIGN KEY (location_id) REFERENCES LOCATIONS(id)
                    )
                    """
                )
            conn.commit()
    except Exception as e:
        create_log("DB", f"Error creating table MAPS: {e}")


# Details table to hold the details of the location for web page:
def create_location_details():
    create_log("DB", "Creating the table LOCATION_DETAILS.")
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS LOCATION_DETAILS (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        location_id INT,
                        description_intro TEXT,
                        description_history TEXT,
                        description_highlights TEXT,
                        description_tips TEXT,
                        FOREIGN KEY (location_id) REFERENCES LOCATIONS(id) 
                    )
                    """
                )
            conn.commit()
    except Exception as e:
        create_log("DB", f"Error creating table LOCATION_DETAILS: {e}")


# -------------------------------------------------------------------------------------
# Data Operations:
# -------------------------------------------------------------------------------------

# Fn to insert data into Locations table:
def insert_location(id, name, location, image, image2, image3, image4):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO LOCATIONS (id, name, location, image, image2, image3, image4)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (id, name, location, image, image2, image3, image4)
            )
            conn.commit()


# Fn to insert data into Maps table:
def insert_map(location_id, map_iframe, latitude, longitude):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO MAPS (location_id, map_iframe, latitude, longitude)
                VALUES (%s, %s, %s, %s)
                """,
                (location_id, map_iframe, latitude, longitude)
            )
            conn.commit()


# Fn to insert data into Location Details table:
def insert_location_details(location_id, description_intro, description_history, description_highlights, description_tips):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO LOCATION_DETAILS (location_id, description_intro, description_history, description_highlights, description_tips)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (location_id, description_intro, description_history,
                 description_highlights, description_tips)
            )
            conn.commit()


# -------------------------------------------------------------------------------------
# Helper Functions:
# -------------------------------------------------------------------------------------

def get_iframe_code(src, width=350, height=300):
    defaults_just_saved = '''
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14994.081656486365!2d75.15761048715821!3d20.02863330000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdb92609201a9eb%3A0xe0639ba6286a474!2sEllora%20Cave%20No.%2029%20The%20Dhumar%20Lena!5e0!3m2!1sen!2sin!4v1731098951522!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade"></iframe>
    '''

    return f'<iframe src="{src}" width="{width}" height="{height}" style="border:0; border-radius:10px; opacity:1.0; filter: invert(1.0);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'


# -------------------------------------------------------------------------------------
# Functions to call from server:
# -------------------------------------------------------------------------------------

# Fn to call from server which returns location based on id (for specific location page):
def get_location_data(id, output_format='json'):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM LOCATIONS WHERE id = %s
                """,
                (id,)
            )
            location = cur.fetchone()
            headers = [desc[0] for desc in cur.description]

    resp = dict(zip(headers, location)) if location else {}
    return json.dumps(resp, indent=5) if output_format == 'json' else resp


# Get map data of location based on location_id:
def get_map_data(location_id, output_format='json'):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM MAPS WHERE location_id = %s
                """,
                (location_id,)
            )
            location_map = cur.fetchone()
            headers = [desc[0] for desc in cur.description]

    resp = dict(zip(headers, location_map)) if location_map else {}
    return json.dumps(resp, indent=5) if output_format == 'json' else resp


# Get all locations: (meant to be called from the client side js)
def get_all_locations_data(output_format='json'):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM LOCATIONS")
            locations = cur.fetchall()
            headers = [desc[0] for desc in cur.description]

    locations_list = [dict(zip(headers, row)) for row in locations]
    return json.dumps(locations_list, indent=5) if output_format == 'json' else locations_list


# Get location details (text data) to render the page for a specific location:
def get_place_details(place_id, output_format='json'):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT location_id, description_intro, description_history, description_highlights, description_tips
                FROM LOCATION_DETAILS
                WHERE location_id = %s
                """,
                (place_id,)
            )
            location_details = cur.fetchone()
            headers = [desc[0] for desc in cur.description]

    resp = dict(zip(headers, location_details)) if location_details else {}
    return json.dumps(resp, indent=5) if output_format == 'json' else resp
