# Simple product checker

def mostrar_productos(productos):
    """
    Show all products in the list.
    """
    for producto in productos:
        print(producto)


def buscar_producto(productos, nombre):
    """
    Search for a product by name.
    """
    for producto in productos:
        if producto.lower() == nombre.lower():
            return producto
    return None


# List of products
productos = ["Laptop", "Mouse", "Keyboard"]

# Show products
print("Product list:")
mostrar_productos(productos)

# Ask user
nombre = input("Enter a product name: ")

# Search process
resultado = buscar_producto(productos, nombre)

if resultado:
    print("Product found:", resultado)
else:
    print("Product not found")