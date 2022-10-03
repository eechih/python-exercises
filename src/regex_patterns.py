import re

email_pattern = r"([A-Za-z0-9]+[-+_.])*[A-Za-z0-9]+@[A-Za-z0-9]+(.[A-Z|a-z]{2,})*"
EMAIL_PATTERN = re.compile(pattern=email_pattern)

# 高強度密碼：6位數以上，並且至少包含：大寫字母、小寫字母、數字、符號各一（只允許八種符號：'@', '$', '!', '#', '%', '*', '?', '&'）
strong_password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,}$"
STRONG_PASSWORD_PATTERN = re.compile(pattern=strong_password_pattern)
