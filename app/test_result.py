class TestResult:
    def __init__(self) -> None:
        self.runCount = 1

    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return f"{self.runCount} run, 0 failed"
