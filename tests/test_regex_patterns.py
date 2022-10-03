import pytest

from src.regex_patterns import EMAIL_PATTERN, STRONG_PASSWORD_PATTERN


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
    if is_valid:
        assert mo is not None
    else:
        assert mo is None


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
    if is_valid:
        assert mo is not None
    else:
        assert mo is None


if __name__ == "__main__":
    pytest.main()
