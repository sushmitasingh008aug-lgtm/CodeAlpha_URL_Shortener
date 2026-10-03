from flask import Blueprint, request, jsonify, redirect

from database import get_db_connection
from utils import generate_short_code


# Create Blueprint
url_routes = Blueprint("url_routes", __name__)


# -----------------------------------
# TEST DATABASE
# -----------------------------------

@url_routes.route("/test-db")
def test_db():

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT 1")

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return str(result)


# -----------------------------------
# SHORTEN URL
# -----------------------------------

@url_routes.route("/shorten", methods=["POST"])
def shorten_url():
    """
    Create a short URL
    ---
    tags:
      - URL Shortener

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - url
          properties:
            url:
              type: string
              example: https://www.google.com

    responses:
      200:
        description: Short URL created successfully
        schema:
          type: object
          properties:
            original_url:
              type: string
            short_code:
              type: string
            short_url:
              type: string

      400:
        description: URL is required
    """

    # Get JSON data
    data = request.get_json()

    # Check URL
    if not data or "url" not in data:

        return jsonify({
            "error": "URL is required"
        }), 400

    # Get original URL
    original_url = data["url"]

    # Generate short code
    short_code = generate_short_code()

    # Connect to database
    connection = get_db_connection()

    cursor = connection.cursor()

    # Insert URL into database
    cursor.execute(
        """
        INSERT INTO urls (original_url, short_code)
        VALUES (%s, %s)
        """,
        (original_url, short_code)
    )

    # Save changes
    connection.commit()

    # Close database
    cursor.close()
    connection.close()

    # Create short URL
    short_url = f"http://127.0.0.1:5000/{short_code}"

    # Return response
    return jsonify({
        "original_url": original_url,
        "short_code": short_code,
        "short_url": short_url
    })


# -----------------------------------
# REDIRECT SHORT URL
# -----------------------------------

@url_routes.route("/<short_code>")
def redirect_url(short_code):
    """
    Redirect to original URL
    ---
    tags:
      - URL Shortener

    parameters:
      - name: short_code
        in: path
        type: string
        required: true
        example: aB72xK

    responses:
      302:
        description: Redirects to original URL

      404:
        description: Short URL not found
    """

    # Connect to database
    connection = get_db_connection()

    cursor = connection.cursor()

    # Search for short code
    cursor.execute(
        """
        SELECT original_url
        FROM urls
        WHERE short_code = %s
        """,
        (short_code,)
    )

    # Get result
    result = cursor.fetchone()

    # Close database
    cursor.close()
    connection.close()

    # If short code doesn't exist
    if result is None:

        return jsonify({
            "error": "Short URL not found"
        }), 404

    # Get original URL
    original_url = result[0]

    # Redirect user
    return redirect(original_url)