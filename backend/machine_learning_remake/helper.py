from ipaddress import ip_address
from urllib.parse import urlsplit


def is_ip(hostname: str) -> int:
    try:
        ip_address(hostname)
        return 1
    except ValueError:
        return 0


def count_letters(url: str) -> int:
    return len([c for c in url if c.isascii() and c.isalpha()])


def count_digits(url: str) -> int:
    return len([c for c in url if c.isascii() and c.isdecimal()])


def calculate_ratio(text: str) -> tuple:
    if len(text) == 0:
        return (0, 0, 1)

    d_ratio = count_digits(text) / len(text)
    l_ratio = count_letters(text) / len(text)
    o_ratio = 1 - d_ratio - l_ratio

    return (d_ratio, l_ratio, o_ratio)


def parse_url(url: str, verbose: bool = False) -> dict:
    component = urlsplit(url)

    # URL parsed
    scheme = component.scheme
    netloc = component.netloc
    path = component.path or "/"
    query = component.query
    fragment = component.fragment

    # Path parsed
    paths = [p for p in path.split("/") if p]

    # Netloc parsed
    username = component.username or ""
    password = component.password or ""
    hostname = component.hostname or ""
    port = str(component.port) or ""

    # Domain parsed
    domains = list(hostname.split(".")) if not is_ip(hostname) else ""
    
    if domains and domains[0] == "www":
        domains.pop(0)
    
    tld = domains[-1] if len(domains) > 0 else ""
    sld = domains[-2] if len(domains) > 1 else ""
    subdomain = ".".join(domains[:-2]) if len(domains) > 2 else ""

    if verbose:
        print(f"{url=}")
        print("--- URL parsed ---")
        print(f"{scheme=}")
        print(f"{netloc=}")
        print(f"{path=}")
        print(f"{query=}")
        print(f"{fragment=}")
        print("--- Path parsed ---")
        print(f"{paths=}")
        print("--- Netloc parsed ---")
        print(f"{username=}")
        print(f"{password=}")
        print(f"{hostname=}")
        print(f"{port=}")
        print("--- Domain parsed ---")
        print(f"{domains=}")
        print(f"{tld=}")
        print(f"{sld=}")
        print(f"{subdomain=}")
        print("------")

    return {
        "url": url,
        # URL parsed
        "scheme": scheme,
        "netloc": netloc,
        "path": path,
        "query": query,
        "fragment": fragment,
        # Path parsed
        "paths": paths,
        # Netloc parsed
        "username": username,
        "password": password,
        "hostname": hostname,
        "port": port,
        # Domain parsed
        "domains": domains,
        "tld": tld,
        "sld": sld,
        "subdomain": subdomain,
    }


def analyze_url(url: str, tld_occurrence: dict[str, int]) -> dict:
    component = parse_url(url)
    path_d_ratio, path_l_ratio, path_o_ratio = calculate_ratio(component["path"])
    tld_d_ratio, tld_l_ratio, tld_o_ratio = calculate_ratio(component["tld"])
    sld_d_ratio, sld_l_ratio, sld_o_ratio = calculate_ratio(component["sld"])
    subdomain_d_ratio, subdomain_l_ratio, subdomain_o_ratio = calculate_ratio(
        component["subdomain"]
    )

    return {
        # Flags
        "is_https": int(component["scheme"] == "https"),
        "is_http": int(component["scheme"] == "http"),
        "is_auth": int(component["username"] != ""),
        "is_ip": is_ip(component["hostname"]),
        "has_port": int(component["port"] != ""),
        # Length
        "scheme_length": len(component["scheme"]),
        "path_length": len(component["path"]),
        "query_length": len(component["query"]),
        "fragment_length": len(component["fragment"]),
        "username_length": len(component["username"]),
        "password_length": len(component["password"]),
        "port_length": len(component["port"]),
        "tld_length": len(component["tld"]),
        "sld_length": len(component["sld"]),
        "subdomain_length": len(component["subdomain"]),
        # Count
        "domains_count": len(component["domains"]),
        "paths_count": len(component["paths"]),
        # Ratio
        "path_d_ratio": path_d_ratio,
        "path_l_ratio": path_l_ratio,
        "path_o_ratio": path_o_ratio,
        "tld_d_ratio": tld_d_ratio,
        "tld_l_ratio": tld_l_ratio,
        "tld_o_ratio": tld_o_ratio,
        "sld_d_ratio": sld_d_ratio,
        "sld_l_ratio": sld_l_ratio,
        "sld_o_ratio": sld_o_ratio,
        "subdomain_d_ratio": subdomain_d_ratio,
        "subdomain_l_ratio": subdomain_l_ratio,
        "subdomain_o_ratio": subdomain_o_ratio,
        # Occurrence
        "tld_occurrence": tld_occurrence.get(component["tld"], 0)
    }


if __name__ == "__main__":
    # parse_url("", verbose=True)
    # parse_url("https://www.google.com", verbose=True)
    # parse_url("https://www.google.com/search", verbose=True)
    # parse_url("https://www.google.com/search?q=asdf", verbose=True)
    # parse_url("https://www.google.com/search?q=asdf#zxcv", verbose=True)
    # parse_url("https://username:password@127.0.0.1:500", verbose=True)

    print(analyze_url(""))
    print(analyze_url("https://www.google.com"))
    print(analyze_url("https://www.google.com/search"))
    print(analyze_url("https://www.google.com/search/id"))
    print(analyze_url("https://www.google.com/search?q=asdf"))
    print(analyze_url("https://www.google.com/search?q=asdf#zxcv"))
    print(analyze_url("https://username:password@127.0.0.1:500"))
