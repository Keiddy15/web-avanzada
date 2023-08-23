products = [
    {
        "id": 123,
        "name": "Notebook",
        "price": 12.500,
        "cat_id": 1
    },
    {
        "id": 124,
        "name": "Soap",
        "price": 10.500,
        "cat_id": 2
    }
]

categories = [
    {
        "id": 1,
        "name": "School Supplies",
    },
    {
        "id": 2,
        "name": "Cleaning",
    }
]

product_category_relation = {}

id_to_category_name = {cat["id"]: cat["name"] for cat in categories}

for product in products:
    product_name = product["name"]
    category_id = product["cat_id"]
    category_name = id_to_category_name.get(category_id, "Category not found")
    
    product_category_relation[product_name] = category_name

for product, category in product_category_relation.items():
    print(f"Product: {product}, Category: {category}")
