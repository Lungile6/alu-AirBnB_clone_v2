<<<<<<< HEAD
#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """ Test for amenity"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        new.name = "amenity"
        self.assertEqual(type(new.name), str)
=======
#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """ Test for amenity"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        new.name = "amenity"
        self.assertEqual(type(new.name), str)
        
>>>>>>> 24a8f224a90deb32363c2a6fc9aaa2bd43a456cd
