from django.core import management

from healingcirclemassage.common.tests import CommonTestCase

class TestStory(CommonTestCase):
    def setUp(self):
        CommonTestCase.setUp(self)

    def test_navigation(self):
        """ Alice goes to the home page

        she should...
        """
        alice = self.alice
        # see the index page
        templates_used = ["home.html", "base.html"]
        doc = alice.clicks_a_link("/", templates_used=templates_used)
        # follow the links to the other static sections
        for link in ["faq", "news", "resume", "services", "writings", "testimonials", "events"]:
            alice.clicks_a_link("/"+link+"/")
        # goes to the appointments page
        doc = alice.clicks_a_link("/appointments/")
        
