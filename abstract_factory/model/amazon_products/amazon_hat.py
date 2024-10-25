from abstract_factory.accessories_interfaces import Hat


class AmazonHat(Hat):
    def wear(self):
        return "I am wearing my new hat from Amazon"

