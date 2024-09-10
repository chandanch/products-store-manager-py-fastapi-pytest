from faker import Faker

faker = Faker()


class Category:
    def __init__(
        self, id: int, name: str, slug: str, is_active: bool, level: int, parent_id: int
    ) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.is_active = is_active
        self.level = level
        self.parent_id = parent_id


def generate_random_category_as_dict(id: int = 1):
    return {
        "id": id or faker.random_int(1, 1999),
        "name": faker.word(),
        "slug": faker.slug(),
        "is_active": faker.boolean(),
        "level": faker.random_int(1, 20),
        "parent_id": None,
    }
