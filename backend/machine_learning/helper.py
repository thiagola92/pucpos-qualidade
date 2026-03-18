from ipaddress import ip_address
from urllib.parse import urlsplit, SplitResult, unquote


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


def count_subdomains(subdomain: str) -> str:
    parts = [s for s in subdomain.split(".") if len(s) != 0]

    return len(parts)


def count_obfuscations(url: str) -> int:
    # Special characters in the URL are escaped as "%xx".
    # After unescape they will become 1 character again,
    # which means that the string size will be reduced by 2 for each one found.
    found = (len(url) - len(unquote(url))) / 2

    # Know that we know the quantity, we can tell how many chars were used in obfuscations.
    return int(found * 3)


def count_letters(url: str) -> int:
    return len([c for c in url if c.isascii() and c.isalpha()])


def count_digits(url: str) -> int:
    return len([c for c in url if c.isascii() and c.isdecimal()])


def count_special_chars(url: str) -> int:
    return (
        len(url)
        - count_letters(url)
        - count_digits(url)
        - url.count("=")
        - url.count("?")
        - url.count("&")
    )


def analyze_url(url: str) -> dict[str, list]:
    component: SplitResult = urlsplit(url)
    tld = get_tld(component.hostname or "")
    subdomain = get_subdomain(component.hostname or "")

    # print(component)
    # print(
    #     {
    #         "username": component.username,
    #         "password": component.password,
    #         "hostname": component.hostname,
    #         "port": component.port,
    #     }
    # )
    # print({"tld": tld, "subdomain": subdomain})

    return {
        "URLLength": [len(url)],
        "DomainLength": [len(component.hostname or "")],
        "IsDomainIP": [int(is_ip(component.hostname or ""))],
        "TLDLength": [len(tld)],
        "NoOfSubDomain": [count_subdomains(subdomain)],
        "HasObfuscation": [int(count_obfuscations(url) != 0)],
        "NoOfObfuscatedChar": [count_obfuscations(url)],
        "ObfuscationRatio": [count_obfuscations(url) / len(url)],
        "NoOfLettersInURL": [count_letters(url)],
        "LetterRatioInURL": [count_letters(url) / len(url)],
        "NoOfDegitsInURL": [count_digits(url)],
        "DegitRatioInURL": [count_digits(url) / len(url)],
        "NoOfEqualsInURL": [url.count("=")],
        "NoOfQMarkInURL": [url.count("?")],
        "NoOfAmpersandInURL": [url.count("&")],
        "NoOfOtherSpecialCharsInURL": [count_special_chars(url)],
        "SpacialCharRatioInURL": [count_special_chars(url) / len(url)],
        "IsHTTPS": [int(component.scheme == "https")],
    }
