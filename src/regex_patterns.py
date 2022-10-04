import re

email_pattern = r"([A-Za-z0-9]+[-+_.])*[A-Za-z0-9]+@[A-Za-z0-9]+(.[A-Z|a-z]{2,})*"
EMAIL_PATTERN = re.compile(pattern=email_pattern)

# 高強度密碼：6位數以上，並且至少包含：大寫字母、小寫字母、數字、符號各一（只允許八種符號：'@', '$', '!', '#', '%', '*', '?', '&'）
strong_password_pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,}"
STRONG_PASSWORD_PATTERN = re.compile(pattern=strong_password_pattern)

# URL 網址，允許 http, https, ftp 協定，並且可取出 Protocol, Domain, Path, Query
url_pattern = r"(?:(https?|ftp)://)?((?:[a-zA-Z0-9.-]+\.)+(?:[a-zA-Z0-9]{2,4}))((?:/[\w+=%&.~-]*)*)\??([\w+=%&.~-]*)"
URL_PATTEN = re.compile(pattern=url_pattern)

# URL 網址，允許 http, https, ftp 協定，並且可取出 Protocol, Domain, Path, Query (外加功能：分組命名、添加註釋)
url_pattern_named_groups = r"""
    (?:(?P<protocol>https?|ftp)://)?                        # Protocol 
    (?P<domain>(?:[a-zA-Z0-9.-]+\.)+(?:[a-zA-Z0-9]{2,4}))   # Domain
    (?P<path>(?:/[\w+=%&.~-]*)*)\??                         # Path
    (?P<query>[\w+=%&.~-]*)                                 # Query
"""
URL_PATTEN_NAMED_GROUPS = re.compile(pattern=url_pattern_named_groups, flags=re.VERBOSE)

# 信用卡系列

# Visa Card：由數字 4 開始，有效長度為 13 或 16 碼，可使用空白或破折號做分隔。
# 範例："4012-8888-8888-1"、"4012 8888 8888 1"、"4012888888881"
# 範例："4012-8888-8888-1881"、"4012 8888 8888 1881"、"4012888888881881"
visa_card_number_pattern = r"^4\d{3}([\ \-]?)\d{4}\1\d{4}\1(\d{1}|\d{4})$"
VISA_CARD_NUMBER_PATTERN = re.compile(pattern=visa_card_number_pattern)

# Master Card：卡號開頭固定由 "51" 到 "55" 的數字，有效長度為 16 碼，可使用空白或破折號做分隔。
# 範例："5111-0051-1105-1128"、"5111 0051 1105 1128"、"5111005111051128"
master_card_number_pattern = r"^(5[1-5]\d{2})(?:[\ \-]?)(\d{4})(?:[\ \-]?)(\d{4})(?:[\ \-]?)(\d{4})$"
MASTER_CARD_NUMBER_PATTERN = re.compile(pattern=master_card_number_pattern)
