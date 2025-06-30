import os
import json
import boto3
from pprint import pprint
from logger import create_log

from flask import (
    Flask, jsonify, abort, request,  redirect, url_for,
    render_template, send_from_directory,
    flash, session as flask_session
)

from database_ops import (
    get_all_locations_data,
    get_all_languages,
    get_all_countries,
    get_location_data,
    get_map_data,
    get_place_details,
)

from dotenv import load_dotenv
load_dotenv()

# ----------------------------------------------------------------------------------------------
# Flask App Setup
# ----------------------------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.config.update(SESSION_COOKIE_SECURE=True, SESSION_COOKIE_SAMESITE="None")

IMAGE_DIRECTORY = os.environ.get("IMAGE_DIRECTORY", "images")
S3_BASE_URL = os.environ.get("S3_BASE_URL")
AUTH_ENABLED = os.environ.get("AUTHENTICATE_USERS", "false").lower() == 'true'


# ----------------------------------------------------------------------------------------------
# Setup for AWS Services
# ----------------------------------------------------------------------------------------------

aws_session = boto3.Session(
    aws_access_key_id=os.environ.get("IAM_AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("IAM_AWS_SECRET_KEY"),
    region_name=os.environ.get("IAM_AWS_REGION"),
)

cognito = aws_session.client(
    service_name="cognito-idp",
    region_name=os.environ.get("COG_APP_REGION", "us-east-1")
)

sns = aws_session.client(
    service_name="sns",
    region_name=os.environ.get("SNS_REGION", "us-east-1")
)


# ----------------------------------------------------------------------------------------------
# Test Endpoints:
# ----------------------------------------------------------------------------------------------

@app.route('/test')
def index():
    create_log("App", f"{request.remote_addr} hit the test api.")
    return jsonify("server is live"), 200


# ----------------------------------------------------------------------------------------------
# User Authentication Endpoints
# ----------------------------------------------------------------------------------------------

# Routes for login using email:
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        create_log("App", f"{request.remote_addr} visited the login page.")
        return render_template("auth_login.html")

    try:
        if not AUTH_ENABLED:
            flash("Authentication is disabled.", "info")
            return redirect(url_for("main"))

        data = request.form
        email = data["email"]
        password = data["password"]

        create_log("App", f"{request.remote_addr} tried to login with email: {email}.")

        # Authenticate user with Cognito
        # If invalid credentials, Cognito will throw an `exception`
        response = cognito.initiate_auth(
            ClientId=os.environ.get("COG_APP_CLIENT_ID"),
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": email, "PASSWORD": password},
        )

        # pprint(response)

        # Mark the user as logged in
        flask_session['logged_in'] = True
        flask_session['user_email'] = email

        # Send login notification
        sns.publish(
            TopicArn=os.environ.get("SNS_TOPIC_ARN"),
            Message=f"User {email} has logged in successfully",
            Subject="New User Login",
        )

        flash("Login successful!", "success")

        # Redirect to the last visited page or index
        next_page = flask_session.pop('next', '/')
        return redirect(next_page)

    except Exception as e:
        create_log("App", f"{request.remote_addr} failed to login with email: {email}.")
        # flash("Login failed. Please try again.", category='success')
        flash(str(e), "error")
        return render_template("auth_login.html")


# Routes for signup using email:
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("auth_signup.html")

    try:
        if not AUTH_ENABLED:
            flash("Authentication is disabled.", "info")
            return redirect(url_for("main"))

        data = request.form  # Using form data instead of JSON
        email = data["email"]
        password = data["password"]

        # Sign up user with Cognito
        response = cognito.sign_up(
            ClientId=os.environ.get("COG_APP_CLIENT_ID"),
            Username=email,
            Password=password,
            UserAttributes=[
                {"Name": "email", "Value": email},
            ],
        )

        # pprint(response)

        flash("Please check your email for verification code", "success")
        return redirect(url_for("verify", email=email))

    except Exception as e:
        flash(str(e), "error")
        return render_template("auth_signup.html")


# Routes for verification using email:
@app.route("/verify", methods=["GET", "POST"])
def verify():
    email = request.args.get("email")

    if request.method == "GET":
        return render_template("auth_verify.html", email=email)

    try:
        if not AUTH_ENABLED:
            flash("Authentication is disabled.", "info")
            return redirect(url_for("main"))

        data = request.form
        code = data["code"]

        # Confirm sign up with verification code
        cognito.confirm_sign_up(
            ClientId=os.environ.get("COG_APP_CLIENT_ID"),
            Username=email,
            ConfirmationCode=code
        )

        flash("Email verified successfully! Please login.", "success")
        return redirect(url_for("login"))

    except Exception as e:
        flash(str(e), "error")
        return render_template("auth_verify.html", email=email)


# Routes for logout and clear the flask session:
@app.route("/logout")
def logout():
    if not AUTH_ENABLED:
        flash("Authentication is disabled.", "info")
        return redirect(url_for("main"))

    flask_session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


# ----------------------------------------------------------------------------------------------
# Main Application Routes
# ----------------------------------------------------------------------------------------------

# Main page of the website, if authenticated, render the main page:
@app.route("/")
def main():
    # If authentication is enabled, check if the user is logged in
    if AUTH_ENABLED:
        if not flask_session.get('logged_in', False):
            # Store the current endpoint for post-login redirection
            flask_session['next'] = request.path
            flash("Please log in to continue.", "warning")
            return render_template('auth_login.html')

        user = flask_session.get('user_email', 'Guest')
        create_log("App", f"{request.remote_addr} visited the main page as user: {user}.")

    else:
        # If authentication is not enabled, render the main page directly
        flask_session['logged_in'] = True
        flask_session['user_email'] = "Guest"
        user = "Guest"

    return render_template("index.html", user_mail=user), 200


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


# ----------------------------------------------------------------------------------------------
# ChatBot endpoints:
# ----------------------------------------------------------------------------------------------

# This is just initial setup. Much more with AI can be done here!
@app.route("/chatBot")
def chatbot():
    create_log("App", f"{request.remote_addr} visited the chatbot page.")
    return render_template("chatbot.html")


# ----------------------------------------------------------------------------------------------
# Testing:
# ----------------------------------------------------------------------------------------------

# Get all locations in a country with country_code:
if __name__ == "__main__":
    create_log("App", "Sever Started", pre_lines=1, post_lines=1)
    app.run(debug=True, host="0.0.0.0", port=5000)
