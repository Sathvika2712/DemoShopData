## E-commerce Dataset Demo

This project generates a synthetic product catalog, loads it into a SQLite database, and demonstrates a multi-table query that joins sample customers, orders, and products.

### Files
- `generate_products_dataset.py` – writes the 50-row dataset to `products.csv`.
- `ingest_products_sqlite.py` – creates `ecommerce.db` (with `products` table) and ingests the dataset.
- `multi_table_query.py` – seeds `customers` and `orders` tables and prints a joined order summary.
- `products.csv` – generated dataset (tracked for convenience).
- `ecommerce.db` – SQLite database populated with the dataset and sample orders.

### Usage
1. Regenerate the CSV (optional):
   ```
   python generate_products_dataset.py
   ```
2. Ingest into SQLite:
   ```
   python ingest_products_sqlite.py
   ```
3. Run the multi-table query demo:
   ```
   python multi_table_query.py
   ```

### Notes
- The scripts expect Python 3.10+ (for type hints) and only rely on the standard library.
- `products.csv` and `ecommerce.db` are included so the dataset can be inspected without rerunning the scripts.

