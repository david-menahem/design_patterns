from abstract_factory.aliexpress_accessories_factory import AliexpressAccessoriesFactory
from abstract_factory.amazon_accessories_factory import AmazonAccessoriesFactory
from abstract_factory.client_code import client_code

if __name__ == '__main__':
    aliexpress_factory = AliexpressAccessoriesFactory()
    client_code(aliexpress_factory)

    amazon_factory = AmazonAccessoriesFactory()
    client_code(amazon_factory)

