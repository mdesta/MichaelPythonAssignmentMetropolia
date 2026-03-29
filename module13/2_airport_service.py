import os

import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("AIRPORT_DB_HOST", "localhost"),
        user=os.getenv("AIRPORT_DB_USER", "test_m_flight"),
        password=os.getenv("AIRPORT_DB_PASSWORD", "newpassword"),
        database=os.getenv("AIRPORT_DB_NAME", "test_flight_game_db"),
    )


@app.get("/airport/<string:icao>")
def airport(icao: str):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT ident, name, municipality FROM airport WHERE ident=%s",
            (icao.upper(),),
        )
        row = cursor.fetchone()
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500
    finally:
        try:
            cursor.close()
            db.close()
        except Exception:
            pass

    if not row:
        return jsonify({"error": "Airport not found"}), 404

    return jsonify(
        {
            "ICAO": row["ident"],
            "Name": row["name"],
            "Location": row["municipality"] or "",
        }
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
