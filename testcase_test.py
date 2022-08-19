from app.test_case import TestCase
from app.was_run import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun


TestCaseTest("testRunning").run()