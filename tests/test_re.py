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


def test_non_greedy():
    # 貪婪：嘗試匹配盡可能多的字符
    # 非貪婪：嘗試匹配盡可能少的字符

    # ?? 匹配0次或1次 (非貪婪)
    assert re.search("go??", "goooooood").group() == "g"

    # +? 匹配1次或更多次以上（非貪婪）
    assert re.search("go+?", "goooooood").group() == "go"

    # *? 匹配0次或1次或更多次以上（非貪婪）
    assert re.search("go*?", "goooooood").group() == "g"

    # {n,m}? 匹配n到m次（非貪婪）
    assert re.search("go{2,8}?", "goooooood").group() == "goo"

    # {n,}? 匹配n次或n次以上（非貪婪）
    assert re.search("go{4}?", "goooooood").group() == "goooo"


def test_greedy_versus_non_greedy():
    # Greedy：嘗試匹配盡可能多的字符
    # Non-Greedy：嘗試匹配盡可能少的字符

    s = "abcde abcde"
    assert re.search(".*c", s).group() == "abcde abc"
    assert re.search(".*?c", s).group() == "abc"

    s = "<html><head><title>Title</title>"
    assert re.match("<.*>", s).group() == "<html><head><title>Title</title>"
    assert re.match("<.*?>", s).group() == "<html>"

    s = "This is a number 234-235-22-423"
    assert re.match(r".+(\d+-\d+-\d+-\d+)", s).group(1) == "4-235-22-423"
    assert re.match(r".+?(\d+-\d+-\d+-\d+)", s).group(1) == "234-235-22-423"


if __name__ == "__main__":
    pytest.main()
