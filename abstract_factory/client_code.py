from abstract_factory.accessories_factory import AccessoriesFactory


def client_code(factory: AccessoriesFactory):
    belt = factory.create_belt()
    hat = factory.create_hat()

    print(belt.wear())
    print(hat.wear())