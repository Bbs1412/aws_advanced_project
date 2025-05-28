import os
import json
from pprint import pprint
from logger import create_log
from flask import Flask, render_template, jsonify, send_from_directory, abort, request
from sq_db import get_all_locations_data, get_place_details, get_location_data, get_map_data

app = Flask(__name__)

IMAGE_DIRECTORY = os.environ.get("IMAGE_DIRECTORY")
S3_BASE_URL = os.environ.get("S3_BASE_URL")


@app.route('/test')
def index():
    create_log("App", f"{request.remote_addr} hit the test api.")
    return jsonify("server is live"), 200


@app.route("/")
def main():
    create_log("App", f"{request.remote_addr} visited the main page.")
    return render_template("index.html"), 200


@app.route("/get_all_locations")
def get_all_locations():
    create_log("DB", f"{request.remote_addr} requested all locations data.")
    # print(get_all_locations_data(output_format='json'))
    return get_all_locations_data(output_format="json"), 200


@app.route("/get_img/<img_name>")
def get_image(img_name):
    create_log("Img", f"{request.remote_addr} requested image {img_name}.")

    try:
        return send_from_directory(IMAGE_DIRECTORY, img_name), 200
    except FileNotFoundError:
        abort(404)


@app.route("/place/<int:place_id>")
def place_detail(place_id):
    create_log("DB", f"{request.remote_addr} requested place {place_id} data.")

    place_data = get_location_data(place_id, output_format="dict")
    place_details = get_place_details(place_id, output_format="dict")
    place_map = get_map_data(place_id, output_format="dict")

    final_data = place_data.copy()
    for key, value in place_details.items():
        final_data[key] = value

    for key, value in place_map.items():
        final_data[key] = value

    final_data["s3_base_url"] = S3_BASE_URL
    return render_template("place_detail.html", place=final_data), 200


@app.route('/get_s3_base_url')
def get_s3_base_url():
    create_log("Env", f"{request.remote_addr} requested 'S3_base_URL'.")
    return jsonify(S3_BASE_URL), 200


if __name__ == "__main__":
    create_log("App", "Sever Started", pre_lines=1, post_lines=1)
    app.run(debug=True, host="0.0.0.0", port=5000)
