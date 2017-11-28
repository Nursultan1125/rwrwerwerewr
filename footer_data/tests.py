from django.test import TestCase

from footer_data.models import TitleFooter, ListFooter


class FooterTest(TestCase):
    def setUp(self):
        self.title = TitleFooter(title_body="Контакты")
        self.title.save()

    def test_get_list_footer(self):
        for i in range(10):
            list_footer = ListFooter(title_footer=self.title, list_body=str(i))
            list_footer.save()

        self.assertEqual(self.title.get_list_footer().count(), 10)
