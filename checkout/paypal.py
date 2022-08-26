import sys
from django.conf import settings

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AVbTvhxXkbJM1bS4BvZH6kC4n2XjgxumlHNYYZ1dtu-iqanZxl1LSHU4HfD5Dq1HgvPkXdvCd3gYxEp_"
        self.client_secret = settings.base.CLIENT_SECRET
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)