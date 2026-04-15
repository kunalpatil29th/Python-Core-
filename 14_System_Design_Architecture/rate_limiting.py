# rate_limiting.py

"""
Definition: Rate Limiting is a technique used to control the rate of requests sent or received by a network interface or service to prevent abuse and ensure fair usage.
"""

import time

class RateLimiter:
    def __init__(self, limit, interval):
        self.limit = limit
        self.interval = interval
        self.requests = []

    def allow_request(self):
        now = time.time()
        self.requests = [r for r in self.requests if r > now - self.interval]
        if len(self.requests) < self.limit:
            self.requests.append(now)
            return True
        return False

# Usage
limiter = RateLimiter(limit=3, interval=5)
for i in range(5):
    if limiter.allow_request():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Blocked (Rate Limit Exceeded)")
    time.sleep(0.5)
