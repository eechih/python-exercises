import pytest

from src.regex_patterns import *


@pytest.mark.parametrize("email,is_valid", [
    # ---- Valid Email Address ----
    ("simple@example.com", True),
    ("very.common@example.com", True),
    ("disposable.style.email.with+symbol@example.com", True),
    ("other.email-with-hyphen@example.com", True),
    ("fully-qualified-domain@example.com", True),
    ("user.name+tag+sorting@example.com", True),
    ("x@example.com", True),  # 域內部分只有一個字母
    ("example-indeed@strange-example.com", True),
    ("admin@mailserver1", True),  # ICANN強烈不建議無點的電子郵件地址
    ("example@s.example", True),
    # ---- Invalid Email Address ----
    ("Abc.example.com", False),  # 沒有@字符
    ("A@b@c@example.com", False),  # 在引號外只允許有一個@
    ("john..doe@example.com", False),  # @之前有兩個連續的點
    ("john.doe@example..com", False),  # @之後有兩個連續的點
])
def test_email_regex(email, is_valid):
    mo = EMAIL_PATTERN.fullmatch(email)
    assert bool(mo) is is_valid


@pytest.mark.parametrize("password,is_valid", [
    # ---- Valid Password ----
    ("Geek1@", True),
    ("Geek1@Geek1@", True),
    # ---- Invalid Password ----
    ("Gek1@", False),  # 不足6個字元
    ("geek1@", False),  # 缺少大寫字母
    ("GEEK1@", False),  # 缺少小寫字母
    ("Geek@@", False),  # 缺少數字
    ("Geek11", False),  # 缺少符號
    ("Geek1@_", False),  # 不接受底線符號
])
def test_strong_password_regex(password, is_valid):
    mo = STRONG_PASSWORD_PATTERN.fullmatch(password)
    assert bool(mo) is is_valid


@pytest.mark.parametrize("url,is_valid,protocol,domain,path,query", [
    ("https://www.google.com", True, "https", "www.google.com", "", ""),
    ("https://www.google.com/search?q=apple", True, "https", "www.google.com", "/search", "q=apple"),
    ("git@github.com:python", False, None, None, None, None),
])
def test_url_pattern(url, is_valid, protocol, domain, path, query):
    mo = URL_PATTEN.fullmatch(url)
    if mo:
        assert is_valid is True
        assert mo.group() == url
        assert mo.group(0) == url
        assert mo.group(1) == protocol
        assert mo.group(2) == domain
        assert mo.group(3) == path
        assert mo.group(4) == query
        assert mo.groups() == (protocol, domain, path, query)
        assert mo.groupdict() == {}
    else:
        assert is_valid is False


@pytest.mark.parametrize("url,is_valid,protocol,domain,path,query", [
    ("https://www.google.com", True, "https", "www.google.com", "", ""),
    ("https://www.google.com/search?q=apple", True, "https", "www.google.com", "/search", "q=apple"),
    ("git@github.com:python", False, None, None, None, None),
])
def test_url_pattern_named_groups(url, is_valid, protocol, domain, path, query):
    mo = URL_PATTEN_NAMED_GROUPS.fullmatch(url)
    if mo:
        assert is_valid is True
        assert mo.group() == url
        assert mo.group(0) == url
        assert mo.group(1) == protocol
        assert mo.group(2) == domain
        assert mo.group(3) == path
        assert mo.group(4) == query
        assert mo.groups() == (protocol, domain, path, query)
        assert mo.groupdict() == {"protocol": protocol, "domain": domain, "path": path, "query": query}
        assert mo.group("protocol") == protocol
        assert mo.group("domain") == domain
        assert mo.group("path") == path
        assert mo.group("query") == query
    else:
        assert is_valid is False


@pytest.mark.parametrize("card_number,is_valid", [
    ("4012-8888-8888-1881", True),
    ("4012 8888 8888 1881", True),
    ("4012888888881881", True),
    ("4012-8888-8888-1", True),
    ("4012 8888 8888 1", True),
    ("4012888888881", True),
    ("4012_8888_8888_1881", False),  # 只接受空白或破折號形成分隔的卡號
    ("401288888888188", False),  # 長度非 13 或 16 碼
    ("1012888888881881", False),  # 非 4 開頭
])
def test_visa_card_number_pattern(card_number, is_valid):
    mo = VISA_CARD_NUMBER_PATTERN.match(card_number)
    assert bool(mo) is is_valid


@pytest.mark.parametrize("card_number,is_valid,expected_groups", [
    ("5111-0051-1105-1128", True, ("5111", "0051", "1105", "1128")),
    ("5111 0051 1105 1128", True, ("5111", "0051", "1105", "1128")),
    ("5111005111051128", True, ("5111", "0051", "1105", "1128")),
    ("5111_0051_1105_1128", False, None),  # 只接受空白或破折號形成分隔的卡號
    ("511100511105112", False, None),  # 長度非 16 碼
    ("501100511105112", False, None),  # 非 51 ~ 55 開頭
    ("561100511105112", False, None),  # 非 51 ~ 55 開頭
])
def test_master_card_number_pattern(card_number, is_valid, expected_groups):
    mo = MASTER_CARD_NUMBER_PATTERN.match(card_number)
    if mo:
        assert is_valid is True
        assert mo.groups() == expected_groups
    else:
        assert is_valid is False


if __name__ == "__main__":
    pytest.main()
