from abstract_factory.accessories_factory import AccessoriesFactory
from abstract_factory.accessories_interfaces import Hat, Belt
from abstract_factory.model.aliexpress_products.aliexpress_belt import AliexpressBelt
from abstract_factory.model.aliexpress_products.aliexpress_hat import AliexpressHat


class AliexpressAccessoriesFactory(AccessoriesFactory):
    def create_hat(self) -> Hat:
        return AliexpressHat()

    def create_belt(self) -> Belt:
        return AliexpressBelt()

