from builder_pattern.house_builder import HouseBuilder

if __name__ == '__main__':
    builder = HouseBuilder()

    house = (
        builder
        .set_location("Rosh Ha'ayin")
        .set_owner("David Menahem")
        .set_size(120)
        .set_year(2020)
        .build()
    )

    print(house)