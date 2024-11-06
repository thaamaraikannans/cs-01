import re

# pattern = r"\D"
pattern = r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[\dA-Za-z]{4,6}$"

numbercial = "heLlo123"

res = re.match(pattern, numbercial)

response = re.search(r"[bB]{10,}", "bbbbbbbbbb")


pattern = r"(?P<day>[]{2})-(?P<month>[\d]{2})-(?P<year>\d{4})"
match = re.search(pattern, "25-25-2024")

print(match)