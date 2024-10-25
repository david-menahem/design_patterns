from abstract_factory.accessories_factory import AccessoriesFactory
from abstract_factory.accessories_interfaces import Hat, Belt
from abstract_factory.model.amazon_products.amazon_belt import AmazonBelt
from abstract_factory.model.amazon_products.amazon_hat import AmazonHat


class AmazonAccessoriesFactory(AccessoriesFactory):
    def create_hat(self) -> Hat:
        return AmazonHat()

    def create_belt(self) -> Belt:
        return AmazonBelt()

