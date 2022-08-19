from app.test_case import TestCase
from app.was_run import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log


TestCaseTest("testTemplateMethod").run()
