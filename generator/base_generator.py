from faker import Faker
import random


class BaseGenerator:
    faker = Faker("En")

    def get_id(self, uid):
        if uid is None:
            return random.randint(10000, 99999)
        return uid

    def get_name(self, name):
        if name is None:
            return self.faker.name()
        return name

    def create_category(self, category_value=None, uid=None, name=None):
        if category_value is None:
            category = {
                "id": self.get_id(uid),
                "name": self.get_name(name)
            }
            return category
        return category_value

    def get_photo_urls(self, photo_urls=None, url_count=1):
        lst = []
        if photo_urls is None:
            for i in range(url_count):
                photo = self.faker.image_url()
                lst.append(photo)
            return lst
        return photo_urls

    def get_tags(self, tags_value=None, tags_count=1, uid=None, name=None):
        lst = []
        if tags_value is None:
            for i in range(tags_count):
                tags = {
                    "id": self.get_id(uid),
                    "name": self.get_name(name)
            }
            lst.append(tags)
            return lst
        return tags_value

    def get_status(self, status):
        if status is None:
            return "available"
        return status

