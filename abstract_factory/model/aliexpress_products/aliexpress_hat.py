from abstract_factory.accessories_interfaces import Hat


class AliexpressHat(Hat):
    def wear(self):
        return "I am wearing my new hat from Aliexpress"
