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
    if mo:
        assert is_valid is True
    else:
        assert is_valid is False


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
    if mo:
        assert is_valid is True
    else:
        assert is_valid is False


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


if __name__ == "__main__":
    pytest.main()
