"""
Dado dos diccionarios 1 de productos y el 2 de categoría, conocer un 3 que permita tener el nombre del
producto y el nombre de su categoria ejemplo.
"""

products = {
    "Producto A": 10,
    "Producto B": 20,
    "Producto C": 15,
    "Producto D": 32,
}

categories = {
    "Categoría X": ["Producto A", "Producto B"],
    "Categoría Y": ["Producto C"],
}

product_category = {}

for category, product_list in categories.items():
    for product in product_list:
        product_category[product] = category

for product, category in product_category.items():
    print(f"Producto: {product}, Categoría: {category}")
