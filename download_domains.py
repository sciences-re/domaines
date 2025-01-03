#!/usr/bin/env nix-shell
#! nix-shell -i python3 -p python3Packages.urllib3 python3Packages.beautifulsoup4 python3Packages.lxml python3Packages.tldextract

import time
import urllib
import tldextract
from bs4 import BeautifulSoup

fer = "https://pub.federation.renater.fr/metadata/fer/all.xml"
xml = urllib.request.urlopen(fer)
soup = BeautifulSoup(xml.read(), features="xml")
preauthorized_domains = set([tldextract.extract(item.text).registered_domain for item in soup.find_all("shibmd:Scope")])
print(f"The preauthorized domains set contains {len(preauthorized_domains)} domains.")
with open("fer_domains.txt", "wt") as f:
    for domain in preauthorized_domains:
        f.write(f"{domain}\n")
