import sqlite3

def get_revenue(cursor: sqlite3.Cursor, start_date: str, end_date: str) -> float:
    """Retrieve the total revenue generated by the bookstore for a given date range.

    Args:
        cursor (sqlite3.Cursor): The cursor to execute the SQL command.
        start_date (str): The start date of the date range in the format 'YYYY-MM-DD'.
        end_date (str): The end date of the date range in the format 'YYYY-MM-DD'.

    Returns:
        float: The total revenue generated by the bookstore for the given date range.
    """
    query = f"SELECT SUM(b.price * o.quantity) FROM books b, orders o WHERE b.id = o.book_id AND o.order_date BETWEEN ? AND ?"
    cursor.execute(query, (start_date, end_date))
    result = cursor.fetchone()[0]
    return result if result is not None else 0.0