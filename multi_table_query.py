import sqlite3
from pathlib import Path
from typing import Sequence

DB_PATH = Path("ecommerce.db")

CUSTOMERS: Sequence[tuple[str, str]] = (
    ("CUST001", "Ava Martinez"),
    ("CUST002", "Noah Patel"),
    ("CUST003", "Olivia Chen"),
    ("CUST004", "Liam Johnson"),
)

ORDERS: Sequence[tuple[str, str, str, int, float]] = (
    ("ORD1001", "CUST001", "P0003", 1, 88.00),
    ("ORD1002", "CUST002", "P0015", 2, 179.98),
    ("ORD1003", "CUST003", "P0027", 1, 129.50),
    ("ORD1004", "CUST004", "P0038", 1, 149.00),
    ("ORD1005", "CUST001", "P0045", 1, 32.99),
)


def ensure_aux_tables(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            product_id TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            order_total REAL NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
        """
    )


def seed_aux_tables(conn: sqlite3.Connection) -> None:
    conn.executemany(
        "INSERT OR REPLACE INTO customers (customer_id, customer_name) VALUES (?, ?)",
        CUSTOMERS,
    )
    conn.executemany(
        """
        INSERT OR REPLACE INTO orders (
            order_id, customer_id, product_id, quantity, order_total
        ) VALUES (?, ?, ?, ?, ?)
        """,
        ORDERS,
    )


def run_multi_table_query(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    query = """
        SELECT
            o.order_id,
            c.customer_name,
            p.product_name,
            p.category,
            o.quantity,
            o.order_total
        FROM orders o
        INNER JOIN customers c ON o.customer_id = c.customer_id
        INNER JOIN products p ON o.product_id = p.product_id
        ORDER BY o.order_id
    """
    return conn.execute(query).fetchall()


def main() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        ensure_aux_tables(conn)
        seed_aux_tables(conn)
        results = run_multi_table_query(conn)

    print("Joined order summary:")
    for row in results:
        print(
            f"{row['order_id']}: {row['customer_name']} bought {row['quantity']} "
            f"x {row['product_name']} ({row['category']}) for ${row['order_total']:.2f}"
        )


if __name__ == "__main__":
    main()

