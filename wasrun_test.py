import os

from app.was_run import WasRun

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
