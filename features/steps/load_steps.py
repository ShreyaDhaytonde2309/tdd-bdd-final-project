import requests
from service.common import status

@when('I load the product data')
def step_impl(context):
    # Delete all existing products
    response = requests.get(context.rest_endpoint + "/products")
    for product in response.json():
        requests.delete(f"{context.rest_endpoint}/products/{product['id']}")

    # Load the database with new products from context.table
    for row in context.table:
        payload = {
            "name": row['name'],
            "description": row['description'],
            "price": float(row['price']),
            "available": row['available'].lower() in ['true', '1'],
            "category": row['category']
        }
        context.resp = requests.post(context.rest_endpoint + "/products", json=payload)
        assert context.resp.status_code == status.HTTP_201_CREATED
