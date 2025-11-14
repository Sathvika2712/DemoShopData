import csv
from pathlib import Path

DATASET = [
    {"product_id": "P0001", "product_name": "Classic Cotton T-Shirt", "category": "Fashion", "price": 19.99, "rating": 4.3},
    {"product_id": "P0002", "product_name": "Slim Fit Jeans", "category": "Fashion", "price": 54.5, "rating": 4.1},
    {"product_id": "P0003", "product_name": "Running Sneakers", "category": "Fashion", "price": 88.0, "rating": 4.6},
    {"product_id": "P0004", "product_name": "Leather Belt", "category": "Fashion", "price": 32.75, "rating": 4.0},
    {"product_id": "P0005", "product_name": "Canvas Backpack", "category": "Fashion", "price": 47.2, "rating": 4.4},
    {"product_id": "P0006", "product_name": "Silk Scarf", "category": "Fashion", "price": 24.9, "rating": 3.8},
    {"product_id": "P0007", "product_name": "Wool Cardigan", "category": "Fashion", "price": 62.1, "rating": 4.5},
    {"product_id": "P0008", "product_name": "Athletic Socks Pack", "category": "Fashion", "price": 14.25, "rating": 3.9},
    {"product_id": "P0009", "product_name": "Denim Jacket", "category": "Fashion", "price": 79.95, "rating": 4.2},
    {"product_id": "P0010", "product_name": "Smart Casual Blazer", "category": "Fashion", "price": 109.0, "rating": 4.7},
    {"product_id": "P0011", "product_name": "Ultra HD Smart TV", "category": "Electronics", "price": 649.99, "rating": 4.5},
    {"product_id": "P0012", "product_name": "Wireless Noise-Canceling Headphones", "category": "Electronics", "price": 229.0, "rating": 4.6},
    {"product_id": "P0013", "product_name": "Bluetooth Soundbar", "category": "Electronics", "price": 179.5, "rating": 4.2},
    {"product_id": "P0014", "product_name": "4K Action Camera", "category": "Electronics", "price": 259.0, "rating": 4.1},
    {"product_id": "P0015", "product_name": "Portable Bluetooth Speaker", "category": "Electronics", "price": 89.99, "rating": 4.3},
    {"product_id": "P0016", "product_name": "Smart Home Hub", "category": "Electronics", "price": 139.0, "rating": 4.0},
    {"product_id": "P0017", "product_name": "Gaming Laptop 15\"", "category": "Electronics", "price": 1249.0, "rating": 4.4},
    {"product_id": "P0018", "product_name": "Mechanical Keyboard", "category": "Electronics", "price": 119.5, "rating": 4.2},
    {"product_id": "P0019", "product_name": "Wireless Gaming Mouse", "category": "Electronics", "price": 69.95, "rating": 4.1},
    {"product_id": "P0020", "product_name": "Noise-Isolating Earbuds", "category": "Electronics", "price": 59.5, "rating": 3.9},
    {"product_id": "P0021", "product_name": "Stainless Steel Cookware Set", "category": "Home & Kitchen", "price": 199.0, "rating": 4.6},
    {"product_id": "P0022", "product_name": "Adjustable Standing Desk", "category": "Home & Kitchen", "price": 329.0, "rating": 4.4},
    {"product_id": "P0023", "product_name": "Memory Foam Pillow", "category": "Home & Kitchen", "price": 38.75, "rating": 4.2},
    {"product_id": "P0024", "product_name": "Air Purifier with HEPA Filter", "category": "Home & Kitchen", "price": 179.99, "rating": 4.5},
    {"product_id": "P0025", "product_name": "Smart LED Floor Lamp", "category": "Home & Kitchen", "price": 89.0, "rating": 4.1},
    {"product_id": "P0026", "product_name": "Ceramic Dinnerware Set", "category": "Home & Kitchen", "price": 74.95, "rating": 4.0},
    {"product_id": "P0027", "product_name": "Electric Pressure Cooker", "category": "Home & Kitchen", "price": 129.5, "rating": 4.3},
    {"product_id": "P0028", "product_name": "Bamboo Cutting Board Set", "category": "Home & Kitchen", "price": 34.2, "rating": 4.2},
    {"product_id": "P0029", "product_name": "Robot Vacuum Cleaner", "category": "Home & Kitchen", "price": 299.0, "rating": 4.4},
    {"product_id": "P0030", "product_name": "Luxe Throw Blanket", "category": "Home & Kitchen", "price": 56.8, "rating": 4.1},
    {"product_id": "P0031", "product_name": "Organic Facial Cleanser", "category": "Health & Beauty", "price": 22.5, "rating": 4.0},
    {"product_id": "P0032", "product_name": "Vitamin C Serum", "category": "Health & Beauty", "price": 35.0, "rating": 4.3},
    {"product_id": "P0033", "product_name": "Herbal Sleep Aid Capsules", "category": "Health & Beauty", "price": 27.8, "rating": 3.8},
    {"product_id": "P0034", "product_name": "Electric Toothbrush Kit", "category": "Health & Beauty", "price": 69.99, "rating": 4.5},
    {"product_id": "P0035", "product_name": "Aromatherapy Diffuser", "category": "Health & Beauty", "price": 39.95, "rating": 4.2},
    {"product_id": "P0036", "product_name": "Hair Repair Mask", "category": "Health & Beauty", "price": 24.6, "rating": 4.1},
    {"product_id": "P0037", "product_name": "Men's Grooming Set", "category": "Health & Beauty", "price": 48.0, "rating": 4.0},
    {"product_id": "P0038", "product_name": "Fitness Smartwatch", "category": "Health & Beauty", "price": 149.0, "rating": 4.4},
    {"product_id": "P0039", "product_name": "Resistance Band Kit", "category": "Health & Beauty", "price": 29.99, "rating": 4.1},
    {"product_id": "P0040", "product_name": "Protein Powder Blend", "category": "Health & Beauty", "price": 54.2, "rating": 4.3},
    {"product_id": "P0041", "product_name": "Hardcover Mystery Novel", "category": "Books & Media", "price": 24.99, "rating": 4.2},
    {"product_id": "P0042", "product_name": "Self-Help Guidebook", "category": "Books & Media", "price": 18.5, "rating": 3.9},
    {"product_id": "P0043", "product_name": "Children's Picture Story", "category": "Books & Media", "price": 14.75, "rating": 4.4},
    {"product_id": "P0044", "product_name": "Cookbook for Beginners", "category": "Books & Media", "price": 28.0, "rating": 4.1},
    {"product_id": "P0045", "product_name": "Graphic Novel Deluxe Edition", "category": "Books & Media", "price": 32.99, "rating": 4.5},
    {"product_id": "P0046", "product_name": "Travel Photography Book", "category": "Books & Media", "price": 27.5, "rating": 4.0},
    {"product_id": "P0047", "product_name": "Science Fiction Anthology", "category": "Books & Media", "price": 21.0, "rating": 4.2},
    {"product_id": "P0048", "product_name": "Language Learning Workbook", "category": "Books & Media", "price": 19.25, "rating": 3.8},
    {"product_id": "P0049", "product_name": "Historical Biography", "category": "Books & Media", "price": 26.8, "rating": 4.1},
    {"product_id": "P0050", "product_name": "Inspirational Poetry Collection", "category": "Books & Media", "price": 16.95, "rating": 4.0},
]


def write_csv(output_path: Path) -> None:
    fieldnames = ["product_id", "product_name", "category", "price", "rating"]
    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(DATASET)


def main() -> None:
    output_path = Path("products.csv")
    write_csv(output_path)
    print(f"Wrote {len(DATASET)} rows to {output_path.resolve()}")


if __name__ == "__main__":
    main()

