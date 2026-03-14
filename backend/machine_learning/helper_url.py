from urllib.parse import urlsplit, SplitResult, unquote
from ipaddress import ip_address


def is_ip(netloc: str) -> bool:
    try:
        ip_address(netloc)
        return True
    except ValueError:
        return False


def get_tld(hostname: str) -> str:
    _, _, tld = hostname.rpartition(".")
    return tld


def get_subdomain(hostname: str) -> str:
    domain, _, tld = hostname.rpartition(".")
    subdomain, _, _ = domain.rpartition(".")

    return subdomain


def count_obfuscations(url: str) -> int:
    # Special characters in the URL are escaped as "%xx".
    # After unescape they will become 1 character again,
    # which means that the string size will be reduced by 2 for each one found.
    found = (len(url) - len(unquote(url))) / 2

    # Know that we know the quantity, we can tell how many chars were used in obfuscations.
    return found * 3


def count_letters(url: str) -> int:
    return len([c for c in url if c.isascii() and c.isalpha()])


def count_digits(url: str) -> int:
    return len([c for c in url if c.isascii() and c.isdecimal()])


def count_special_chars(url: str) -> int:
    u = (
        url.removeprefix("http")
        .removeprefix("s")
        .removeprefix("://")
        .removeprefix("www.")
    )

    return (
        len(u)
        - count_letters(u)
        - count_digits(u)
        - u.count("=")
        - u.count("?")
        - u.count("&")
    )


def analyze_url(url: str) -> tuple:
    component: SplitResult = urlsplit(url)
    tld = get_tld(component.hostname)
    subdomain = get_subdomain(component.hostname)

    print(component)
    print(
        {
            "username": component.username,
            "password": component.password,
            "hostname": component.hostname,
            "port": component.port,
        }
    )
    print({"tld": tld, "subdomain": subdomain})

    return (
        len(url),  # URLength
        len(component.hostname),  # DomainLength
        is_ip(component.hostname),  # IsDomainIP
        0,  # URLSimilarityIndex
        0,  # CharContinuationRate
        0,  # TLDLegitimateProb
        0,  # URLCharProb
        len(tld),  # TLDLength
        len(subdomain.split(".")),  # NoOfSubDomain
        count_obfuscations(url) != 0,  # HasObfuscation
        count_obfuscations(url),  # NoOfObfuscatedChar
        count_obfuscations(url) / len(url),  # ObfuscationRatio
        count_letters(url),  # NoOfLettersInURL
        count_letters(url) / len(url),  # LetterRatioInURL
        count_digits(url),  # NoOfDegitsInURL
        count_digits(url) / len(url),  # DegitRatioInURL
        url.count("="),  # NoOfEqualsInURL
        url.count("?"),  # NoOfQMarkInURL
        url.count("&"),  # NoOfAmpersandInURL
        count_special_chars(url),  # NoOfOtherSpecialCharsInURL
        count_special_chars(url) / len(url),  # SpacialCharRatioInURL
        component.scheme == "https",  # IsHTTPS
    )


analyze_url("https://www.example.com/")
analyze_url("https://example.com/")
analyze_url("http://example.com/")
analyze_url("https://www.example.ai/")
analyze_url("https://www.store.example.ai/")
analyze_url("https://store.example.ai/")
analyze_url("https://192.168.0.1/")
analyze_url("http://192.168.0.1/")
analyze_url("https://192.168.0.1:5000/")
analyze_url("https://user:pass@192.168.0.1:5000/")
analyze_url("https://www.website.com/q=%20a%20b")
print("https://www.website.com/q=%20a%20b%2F")
print(unquote("https://www.website.com/q=%20a%20b%2F"))
