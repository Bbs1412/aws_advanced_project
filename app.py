import os
import json
import boto3
from pprint import pprint
from logger import create_log
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, send_from_directory, abort, request

from database_ops import (
    get_all_locations_data,
    get_all_languages,
    get_all_countries,
    get_location_data,
    get_map_data,
    get_place_details,
)

load_dotenv()
LOGGING_ENABLED = True if os.environ.get("LOGGING", "false").lower() == 'true' else False
app = Flask(__name__)

IMAGE_DIRECTORY = os.environ.get("IMAGE_DIRECTORY", "images")
S3_BASE_URL = os.environ.get("S3_BASE_URL")


@app.route('/test')
def index():
    create_log("App", f"{request.remote_addr} hit the test api.")
    return jsonify("server is live"), 200


# Main page of the website, render login page, if authenticated, render the main page:
# use the parameter "auth" to check if the user is authenticated
@app.route("/")
def main():
    create_log("App", f"{request.remote_addr} visited the main page.")
    return render_template("index.html"), 200


# Get all locations within a country using country_code:
@app.route("/get_all_locations")
def get_all_locations():
    # Get the country code from the query parameter, defaulting to 'IN'
    country_code = request.args.get("country", "IN")
    create_log("DB", f"{request.remote_addr} requested all locations in '{country_code}'.")

    return get_all_locations_data(country_code=country_code), 200


# Get the image with image name:
@app.route("/get_img/<img_name>")
def get_image(img_name):
    create_log("Img", f"{request.remote_addr} requested image {img_name}.")

    try:
        return send_from_directory(IMAGE_DIRECTORY, img_name), 200
    except FileNotFoundError:
        abort(404)


# Get the rendered page for specific place with place_id:
@app.route("/place/<int:place_id>")
def place_detail(place_id):
    # Get the language from the query parameter, defaulting to 'en' if not provided
    language = request.args.get("lang", "en")
    create_log("DB", f"{request.remote_addr} requested place {place_id} data in '{language}'.")

    place_data = get_location_data(place_id)
    place_details = get_place_details(place_id)
    place_map = get_map_data(place_id)

    final_data = place_data.copy()
    for key, value in place_details.items():
        final_data[key] = value

    for key, value in place_map.items():
        final_data[key] = value

    final_data["s3_base_url"] = S3_BASE_URL

    # pprint(final_data)
    lang_dependant_data = ["description_highlights", "description_history",
                           "description_intro", "description_tips", "location", "name"]

    # pprint(final_data)

    if language != "en":
        create_log('AWS', f"Translating data to '{language}'.")
        # Initialize AWS Translate client
        translate_client = boto3.client(
            "translate",
            aws_access_key_id=os.environ.get('TRANS_AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('TRANS_AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get('TRANS_AWS_REGION_NAME')
        )

        for key in lang_dependant_data:
            final_data[key] = translate_client.translate_text(
                Text=final_data[key],
                SourceLanguageCode="en",
                TargetLanguageCode=language,
            )["TranslatedText"]

        create_log('AWS', f"Data translated to '{language}' successfully.")

    # pprint(final_data)
    return render_template("place_detail.html", place=final_data), 200


# Self explanatory:
@app.route('/get_s3_base_url')
def get_s3_base_url():
    create_log("Env", f"{request.remote_addr} requested 'S3_base_URL'.")
    return jsonify(S3_BASE_URL), 200


# Get all languages from the database:
@app.route('/get_languages')
def get_languages():
    create_log("DB", f"{request.remote_addr} requested all languages.")
    # print(get_all_languages())
    return jsonify(get_all_languages()), 200


# Get all countries from the database:
@app.route('/get_countries')
def get_countries():
    create_log("DB", f"{request.remote_addr} requested all countries.")
    # print(get_all_countries())
    return jsonify(get_all_countries()), 200


# Serve the test_translate.html page:
@app.route('/test_translate')
def test_translate():
    create_log("App", f"{request.remote_addr} requested the test translation page.")
    places = [
        {
            "name": "Ellora Caves",
            "description": "It is a nice place to visit.",
        },
        {
            "name": "Khajuraho Temples",
            "description": "Famous for their intricate sculptures and carvings.",
        },
    ]
    return render_template("test_translate.html", places=places), 200


# Get all locations in a country with country_code:
if __name__ == "__main__":
    create_log("App", "Sever Started", pre_lines=1, post_lines=1)
    app.run(debug=True, host="0.0.0.0", port=5000)
