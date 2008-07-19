from django.core import management

from healingcirclemassage.common.tests import CommonTestCase

class TestStory(CommonTestCase):
    def setUp(self):
        CommonTestCase.setUp(self)

    def test_views_the_home_page(self):
        """ Alice goes to the home page

        she should...
        """
        alice = self.alice
        # see a sidebar with links to each section
        templates_used = ["home.html", "base.html"]
        doc = alice.clicks_a_link("/", templates_used=templates_used)

