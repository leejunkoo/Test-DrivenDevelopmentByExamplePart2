class TestResult:
    def __init__(self) -> None:
        self.runCount = 1
        self.failureCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1

    def summary(self):
        return f"{self.runCount} run, {self.failureCount} failed"
