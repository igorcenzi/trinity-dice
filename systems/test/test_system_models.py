from django.test import TestCase

from systems.models import System
from classes.models import Class


class TestSystemModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.system_name = "Dungeons & Dragons"
        cls.system_dice = 20
        cls.system_version = 3.5
        cls.system_classes = [
            {"name": "Warrior"},
            {"name": "Ranger"},
            {"name": "Archer"},
            {"name": "Mage"}
        ]

        cls.system = System.objects.create(
            name=cls.system_name,
            dice=cls.system_dice,
            version=cls.system_version,
        )

        for klass in cls.system_classes:
            my_class, _ = Class.objects.get_or_create(klass)
            cls.system.classes.add(my_class)

    def test_should_create_system(self):
        self.assertTrue(hasattr(self.system, "id"))
        self.assertTrue(hasattr(self.system, "name"))
        self.assertTrue(hasattr(self.system, "dice"))
        self.assertTrue(hasattr(self.system, "version"))
        self.assertTrue(hasattr(self.system, "is_active"))
        self.assertTrue(hasattr(self.system, "classes"))
        self.assertTrue(hasattr(self.system, "created_at"))
