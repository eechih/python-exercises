import re

email_pattern = r"([A-Za-z0-9]+[-+_.])*[A-Za-z0-9]+@[A-Za-z0-9]+(.[A-Z|a-z]{2,})*"
EMAIL_PATTERN = re.compile(pattern=email_pattern)
