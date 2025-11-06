def test_get_product(self):
    """It should Get a single Product"""
    test_product = self._create_products(1)[0]
    response = self.client.get(f"{BASE_URL}/{test_product.id}")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    self.assertEqual(data["name"], test_product.name)


def test_get_product_not_found(self):
    """It should not Get a Product thats not found"""
    response = self.client.get(f"{BASE_URL}/0")
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    data = response.get_json()
    self.assertIn("was not found", data["message"])


def test_update_product(self):
    """It should Update a Product"""
    products = self._create_products(1)
    test_product = products[0]
    update_data = {"description": "Updated Description"}
    response = self.client.put(f"{BASE_URL}/{test_product.id}", json=update_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    updated_product = response.get_json()
    self.assertEqual(updated_product["description"], "Updated Description")


def test_delete_product(self):
    """It should Delete a Product"""
    products = self._create_products(1)
    test_product = products[0]
    response = self.client.delete(f"{BASE_URL}/{test_product.id}")
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    # Confirm deletion
    response = self.client.get(f"{BASE_URL}/{test_product.id}")
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


def test_list_all_products(self):
    """It should List all Products"""
    self._create_products(5)
    response = self.client.get(BASE_URL)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    self.assertEqual(len(data), 5)


def test_list_products_by_name(self):
    """It should List Products filtered by name"""
    products = self._create_products(5)
    name_filter = products[0].name
    response = self.client.get(BASE_URL, query_string={"name": name_filter})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    for product in data:
        self.assertEqual(product["name"], name_filter)


def test_list_products_by_category(self):
    """It should List Products filtered by category"""
    products = self._create_products(10)
    category_filter = products[0].category.name
    response = self.client.get(BASE_URL, query_string={"category": category_filter})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    for product in data:
        self.assertEqual(product["category"], category_filter)


def test_list_products_by_availability(self):
    """It should List Products filtered by availability"""
    products = self._create_products(10)
    availability_filter = products[0].available
    response = self.client.get(BASE_URL, query_string={"available": availability_filter})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    for product in data:
        self.assertEqual(product["available"], availability_filter)
