import time
import mwclient
from pathlib import Path

site = mwclient.Site("wiki.ifworlds.org")
root = Path("data")

if __name__ == "__main__":
    for p in site.pages:
        path = root / f"{p.name}.txt"
        path.parent.mkdir(exist_ok=True, parents=True)
        print(p.name)
        with open(path, 'w') as f:
            f.write(p.text())
        time.sleep(2)