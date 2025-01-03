#!/usr/bin/env nix-shell
#! nix-shell -i python3 -p python3Packages.urllib3 python3Packages.beautifulsoup4 python3Packages.lxml python3Packages.tldextract

import time
import urllib
import tldextract
from bs4 import BeautifulSoup

urls = ["https://pub.federation.renater.fr/metadata/edugain/all.xml", "https://pub.federation.renater.fr/metadata/fer/all.xml"]
preauthorized_domains = set()
for url in urls:
    xml = urllib.request.urlopen(url)
    soup = BeautifulSoup(xml.read(), features="xml")
    preauthorized_domains.update(set([tldextract.extract(item.text).registered_domain for item in soup.find_all("shibmd:Scope")]))
print(f"The preauthorized domains set contains {len(preauthorized_domains)} domains.")
with open("fer_domains.txt", "wt") as f:
    for domain in preauthorized_domains:
        f.write(f"{domain}\n")
