from django.test import TestCase

# Create your tests here.

class ViewTests(TestCase):
    def test_add_method(self):
        response = self.client.get('/?a=1&b=2')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 3)

    def test_add_non_number(self):
        response = self.client.get('/?a=1&b=a')
        self.assertContains(response, '输入有误')

    # def test_add_lack_number(self):
    #     response = self.client.get('/?a=1')
    #     self.assertContains(response, '输入有误')