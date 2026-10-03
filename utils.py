import string
import random

from database import get_db_connection


def generate_short_code(length=6):

    characters = string.ascii_letters + string.digits

    while True:

        # Generate random code
        short_code = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        # Check whether code already exists
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM urls
            WHERE short_code = %s
            """,
            (short_code,)
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        # If code does not exist, return it
        if result is None:
            return short_code