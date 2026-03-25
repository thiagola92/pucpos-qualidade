import pytest

from machine_learning.helper import analyze_url, InvalidUrl


def test_empty_url():
    with pytest.raises(InvalidUrl):
        assert analyze_url("")["URLLength"][0] == 0


def test_url_length():
    analyze = analyze_url("https://www.github.com")
    assert analyze["URLLength"][0] == len("https://www.github.com")


def test_domain_length():
    analyze = analyze_url("https://www.github.com")
    assert analyze["DomainLength"][0] == len("www.github.com")


def test_identify_ip():
    analyze = analyze_url("https://192.168.0.1")
    assert analyze["IsDomainIP"][0]


def test_identify_fake_ip():
    analyze = analyze_url("https://192.168.0.1.example.com")
    assert not analyze["IsDomainIP"][0]


def test_tld_length():
    analyze = analyze_url("https://www.github.com")
    assert analyze["TLDLength"][0] == len("com")


def test_count_zero_subdomain():
    analyze = analyze_url("https://github.com")
    assert analyze["NoOfSubDomain"][0] == 0


def test_count_one_subdomain():
    analyze = analyze_url("https://www.github.com")
    assert analyze["NoOfSubDomain"][0] == 1


def test_count_two_subdomain():
    analyze = analyze_url("https://store.web.github.com")
    assert analyze["NoOfSubDomain"][0] == 2


def test_detect_obfuscation():
    analyze = analyze_url("https://www.github.com/q=my%20example")
    assert analyze["HasObfuscation"][0]


def test_no_obfuscation():
    analyze = analyze_url("https://www.github.com")
    assert not analyze["HasObfuscation"][0]


def test_count_zero_obfuscation():
    analyze = analyze_url("https://www.github.com")
    assert analyze["NoOfObfuscatedChar"][0] == 0


def test_count_one_obfuscation():
    # Remember that one obfuscation use 3 characters.
    analyze = analyze_url("https://www.github.com/q=my%20example")
    assert analyze["NoOfObfuscatedChar"][0] == 3


def test_count_two_obfuscation():
    # Remember that one obfuscation use 3 characters.
    analyze = analyze_url("https://www.github.com/q=my%20example%20test")
    assert analyze["NoOfObfuscatedChar"][0] == 6


def test_no_obfuscation_ratio():
    analyze = analyze_url("https://www.github.com/q=myexample")
    assert analyze["ObfuscationRatio"][0] == 0


def test_obfuscation_ratio():
    analyze = analyze_url("https://www.github.com/q=my%20")
    assert analyze["ObfuscationRatio"][0] > 0


def test_count_letters():
    analyze = analyze_url("https://www.github.com/")
    assert analyze["NoOfLettersInURL"][0] == len("httpswwwgithubcom")


def test_letter_ratio_increase():
    analyze0 = analyze_url("http://www.github.com")
    analyze1 = analyze_url("https://www.github.com")
    assert analyze1["LetterRatioInURL"][0] > analyze0["LetterRatioInURL"][0]


def test_count_zero_digits():
    analyze = analyze_url("https://www.example.com/")
    assert analyze["NoOfDegitsInURL"][0] == 0


def test_count_three_digits():
    analyze = analyze_url("https://www.example123.com/")
    assert analyze["NoOfDegitsInURL"][0] == 3


def test_no_digits_ratio():
    analyze = analyze_url("https://www.example.com/")
    assert analyze["DegitRatioInURL"][0] == 0


def test_digits_ratio():
    analyze = analyze_url("https://www.example123.com/")
    assert analyze["DegitRatioInURL"][0] > 0


def test_count_zero_equals():
    analyze = analyze_url("https://github.com/")
    assert analyze["NoOfEqualsInURL"][0] == 0


def test_count_one_equals():
    analyze = analyze_url("https://github.com/search?q=example")
    assert analyze["NoOfEqualsInURL"][0] == 1


def test_count_zero_question_marks():
    analyze = analyze_url("https://github.com/")
    assert analyze["NoOfQMarkInURL"][0] == 0


def test_count_one_question_marks():
    analyze = analyze_url("https://github.com/search?q=example")
    assert analyze["NoOfQMarkInURL"][0] == 1


def test_count_zero_ampersands():
    analyze = analyze_url("https://github.com/")
    assert analyze["NoOfAmpersandInURL"][0] == 0


def test_count_one_ampersands():
    analyze = analyze_url("https://github.com/search?q=asdf&type=repositories")
    assert analyze["NoOfAmpersandInURL"][0] == 1


def test_count_special_chars():
    analyze = analyze_url("https://github.com/")
    assert analyze["NoOfOtherSpecialCharsInURL"][0] == len("://./")


def test_special_char_ratio_increase():
    analyze0 = analyze_url("https://www.github.com")
    analyze1 = analyze_url("https://www.github.com/")
    assert analyze1["SpacialCharRatioInURL"][0] > analyze0["SpacialCharRatioInURL"][0]


def test_detect_https():
    analyze = analyze_url("https://github.com/")
    assert analyze["IsHTTPS"][0] == 1


def test_detect_no_https():
    analyze = analyze_url("http://github.com/")
    assert analyze["IsHTTPS"][0] == 0
