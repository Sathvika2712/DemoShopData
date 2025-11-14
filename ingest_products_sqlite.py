import sqlite3
from pathlib import Path

from generate_products_dataset import DATASET

DB_PATH = Path("ecommerce.db")


def ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            rating REAL NOT NULL
        )
        """
    )


def ingest_dataset(conn: sqlite3.Connection) -> None:
    conn.executemany(
        """
        INSERT OR REPLACE INTO products (
            product_id, product_name, category, price, rating
        ) VALUES (
            :product_id, :product_name, :category, :price, :rating
        )
        """,
        DATASET,
    )


def main() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        ensure_table(conn)
        ingest_dataset(conn)
        conn.commit()
    print(f"Ingested {len(DATASET)} rows into {DB_PATH.resolve()}")


if __name__ == "__main__":
    main()

