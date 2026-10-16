"""Manage milk collection records using an in-memory SQLite database."""

import hashlib
import sqlite3


def create_connection():
    """Create a database connection and initialize the milk table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE milk (
            id INTEGER PRIMARY KEY,
            farmer TEXT,
            litres REAL,
            fat REAL,
            day TEXT
        )
        """
    )
    return connection


def record_milk(connection, farmer, litres, fat, day):
    """Record a farmer's milk collection using parameterized SQL."""
    connection.execute(
        "INSERT INTO milk (farmer, litres, fat, day) VALUES (?, ?, ?, ?)",
        (farmer, litres, fat, day),
    )
    connection.commit()


def farmer_token(farmer):
    """Generate a SHA-256 token for a farmer's name."""
    return hashlib.sha256(farmer.encode("utf-8")).hexdigest()


def daily_total(connection, day):
    """Calculate the total litres collected on a particular day."""
    rows = connection.execute(
        "SELECT litres FROM milk WHERE day = ?",
        (day,),
    ).fetchall()
    total = sum(row[0] for row in rows)
    return f"Total: {total:.1f} litres"


def top_farmer(connection):
    """Return the farmer who supplied the most milk."""
    row = connection.execute(
        """
        SELECT farmer, SUM(litres)
        FROM milk
        GROUP BY farmer
        ORDER BY SUM(litres) DESC
        LIMIT 1
        """
    ).fetchone()
    return row[0] if row else None


def print_slip(farmer):
    """Print a message indicating that a farmer's slip is ready."""
    print(f"Printing slip for {farmer}")


def low_fat(connection):
    """Return farmers whose milk fat is missing or below 3.5."""
    rows = connection.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [
        farmer
        for farmer, fat in rows
        if fat is None or fat < 3.5
    ]


def main():
    """Run a sample milk collection workflow."""
    connection = create_connection()

    try:
        record_milk(connection, "Gopal", 12.5, 4.1, "Mon")
        record_milk(connection, "Lata", 20.0, 3.2, "Mon")

        print(
            daily_total(connection, "Mon"),
            top_farmer(connection),
            low_fat(connection),
        )
        print_slip("Gopal")
        print(farmer_token("Lata"))
    finally:
        connection.close()


if __name__ == "__main__":
    main()
