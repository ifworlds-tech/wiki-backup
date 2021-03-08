import mwclient
from pathlib import Path

site = mwclient.Site("wiki.ifworlds.org")

if __name__ == "__main__":
    for p in site.pages:
        print(p.text())
        break