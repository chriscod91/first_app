from django.test import TestCase

# Create your tests here.
class TestCase(TestCase):
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_index_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")
        