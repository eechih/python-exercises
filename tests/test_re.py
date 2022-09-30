import re

import pytest


def test_compile():
    phone_num_regex = re.compile(r"\d\d-\d\d\d\d-\d\d\d\d")
    assert isinstance(phone_num_regex, re.Pattern)

    phone_num_regex_2 = re.compile(phone_num_regex)
    assert isinstance(phone_num_regex_2, re.Pattern)

    assert phone_num_regex == phone_num_regex_2


def test_search():
    phone_num_regex = re.compile(r"\d\d-\d\d\d\d-\d\d\d\d")
    mo = phone_num_regex.search("Call me at 02-8888-1688 by today.")
    assert isinstance(mo, re.Match)
    assert mo.group() == "02-8888-1688"
    assert mo.group(0) == "02-8888-1688"
    with pytest.raises(IndexError):
        mo.group(1)
    assert mo.groups() == ()


def test_match():
    phone_num_regex = re.compile(r"\d\d-\d\d\d\d-\d\d\d\d")
    mo = phone_num_regex.match("Call me at 02-8888-1688 by today.")
    assert mo is None
    mo = phone_num_regex.match("02-8888-1688 by today.")
    assert isinstance(mo, re.Match)
    assert mo.group() == "02-8888-1688"
    assert mo.group(0) == "02-8888-1688"
    with pytest.raises(IndexError):
        mo.group(1)
    assert mo.groups() == ()


def test_fullmatch():
    phone_num_regex = re.compile(r"\d\d-\d\d\d\d-\d\d\d\d")
    mo = phone_num_regex.fullmatch("Call me at 02-8888-1688 by today.")
    assert mo is None
    mo = phone_num_regex.fullmatch("02-8888-1688 by today.")
    assert mo is None
    mo = phone_num_regex.fullmatch("02-8888-1688")
    assert isinstance(mo, re.Match)
    assert mo.group() == "02-8888-1688"
    assert mo.group(0) == "02-8888-1688"
    with pytest.raises(IndexError):
        mo.group(1)
    assert mo.groups() == ()


def test_find_all():
    phone_num_regex = re.compile(r"\d\d-\d\d\d\d-\d\d\d\d")
    string = "Please call David at 02-8888-1688 by today. 02-9888-9898 is his office number."
    ret = phone_num_regex.findall(string)
    assert isinstance(ret, list)
    assert ret == ["02-8888-1688", "02-9888-9898"]


def test_group_pattern():
    phone_num_regex = re.compile(r"(\d\d)-(\d\d\d\d)-(\d\d\d\d)")
    mo = phone_num_regex.search("Call me at 02-8888-1688 by today.")
    assert isinstance(mo, re.Match)
    assert mo.group() == "02-8888-1688"
    assert mo.group(0) == "02-8888-1688"
    assert mo.group(1) == "02"
    assert mo.group(2) == "8888"
    assert mo.group(3) == "1688"
    with pytest.raises(IndexError):
        mo.group(4)
    assert mo.groups() == ("02", "8888", "1688")

    string = "Please call David at 02-8888-1688 by today. 02-9888-9898 is his office number."
    ret = phone_num_regex.findall(string)
    assert isinstance(ret, list)
    assert ret == [("02", "8888", "1688"), ("02", "9888", "9898")]


def test_outside_group_pattern():
    phone_num_regex = re.compile(r"((\d\d)-(\d\d\d\d)-(\d\d\d\d))")
    mo = phone_num_regex.search("Call me at 02-8888-1688 by today.")
    print(mo)
    assert isinstance(mo, re.Match)
    assert mo.group() == "02-8888-1688"
    assert mo.group(0) == "02-8888-1688"
    assert mo.group(1) == "02-8888-1688"
    assert mo.group(2) == "02"
    assert mo.group(3) == "8888"
    assert mo.group(4) == "1688"
    with pytest.raises(IndexError):
        mo.group(5)
    assert mo.groups() == ("02-8888-1688", "02", "8888", "1688")

    string = "Please call David at 02-8888-1688 by today. 02-9888-9898 is his office number."
    ret = phone_num_regex.findall(string)
    assert isinstance(ret, list)
    assert ret == [("02-8888-1688", "02", "8888", "1688"), ("02-9888-9898", "02", "9888", "9898")]


def test_sub():
    name_regex = re.compile(f"prize - \w+")
    result = name_regex.sub("HIDE", "first prize - Phoebe, second prize - Vivi, third prize - Ming")
    assert result == "first HIDE, second HIDE, third HIDE"

    name_regex = re.compile(f"prize - (\w)\w+")
    result = name_regex.sub(r" \1***", "first prize - Phoebe, second prize - Vivi, third prize - Ming")
    assert result == "first  P***, second  V***, third  M***"

    name_regex = re.compile(f"(prize - \w)\w+")
    result = name_regex.sub(r"\1***", "first prize - Phoebe, second prize - Vivi, third prize - Ming")
    assert result == "first prize - P***, second prize - V***, third prize - M***"


if __name__ == "__main__":
    pytest.main()
