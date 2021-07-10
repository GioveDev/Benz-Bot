import sys
from distest import TestCollector
from distest import run_dtest_bot
import distest

import time

test_collector = TestCollector()

@test_collector()
async def test_reply(interface):
    await interface.assert_reply_matches("Herr Benz talk to me pls","[\s\S]")

if __name__ == "__main__":
    run_dtest_bot(sys.argv, test_collector)
