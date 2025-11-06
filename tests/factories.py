class ProductFactory(factory.Factory):
    """Creates fake products for testing"""
    class Meta:
        """Maps factory to data model"""
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.fuzzy.FuzzyChoice(
        choices=[
            "Hat", "Pants", "Shirt", "Apple", "Banana",
            "Pots", "Towels", "Ford", "Chevy", "Hammer", "Wrench"
        ]
    )
    description = factory.Faker("text")
    price = factory.fuzzy.FuzzyDecimal(0.5, 2000.0, 2)
    available = factory.fuzzy.FuzzyChoice(choices=[True, False])
    category = factory.fuzzy.FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )
