from abstract_factory.accessories_interfaces import Belt


class AmazonBelt(Belt):
    def wear(self):
        return "I am wearing my new belt from Amazon"

