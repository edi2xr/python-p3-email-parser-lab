# lib/email_address_parser.py

import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Use regex to find valid emails in the string
        matches = re.findall(r"[A-Za-z0-9\._%+-]+@[A-Za-z0-9\.-]+\.[A-Za-z]{2,}", self.emails)
        # Remove duplicates by using set, then sort
        return sorted(set(matches))
