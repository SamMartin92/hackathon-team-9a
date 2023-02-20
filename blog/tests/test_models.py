from django.test import TestCase

class TestModels(TestCase):

    def setUp(self):
        self.ngo1 = NGO.object.create(
            name = 'NGO 1',
            category = ('Children', 'Children'),
            location = 'NGO Location', 
            geo_extend = ('Local', 'Local'),
            description = 'Description',
            phone = '866667876',
            email = 'test@email.com',
            website = 'https://www.test.com',
            image = null
        )

    def test_Model_created(self):
        self.assertAlmostEquals(self.ngo1.name, 'NGO 1')
