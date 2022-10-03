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
