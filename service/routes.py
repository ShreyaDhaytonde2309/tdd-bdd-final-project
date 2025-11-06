######################################################################
# L I S T   A L L   P R O D U C T S
######################################################################
@app.route("/products", methods=["GET"])
def list_products():
    """List all products or filter by name, category, or availability"""
    app.logger.info("Request to list products")
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")
    products = None

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available is not None:
        # Convert available string to boolean
        available_bool = available.lower() == "true"
        products = Product.find_by_availability(available_bool)
    else:
        products = Product.all()

    results = [product.serialize() for product in products]
    app.logger.info("Returning %d products", len(results))
    return jsonify(results), status.HTTP_200_OK


######################################################################
# R E A D   A   P R O D U C T
######################################################################
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    app.logger.info(f"Request for product with id [{product_id}]")
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")
    app.logger.info(f"Returning product: {product.name}")
    return product.serialize(), status.HTTP_200_OK


######################################################################
# U P D A T E   A   P R O D U C T
######################################################################
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    app.logger.info(f"Request to update product with id [{product_id}]")
    check_content_type("application/json")

    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")

    data = request.get_json()
    product.deserialize(data)
    product.update()

    app.logger.info(f"Product [{product_id}] updated")
    return product.serialize(), status.HTTP_200_OK


######################################################################
# D E L E T E   A   P R O D U C T
######################################################################
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    app.logger.info(f"Request to delete product with id [{product_id}]")
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")
    product.delete()
    app.logger.info(f"Product [{product_id}] deleted")
    return "", status.HTTP_204_NO_CONTENT
