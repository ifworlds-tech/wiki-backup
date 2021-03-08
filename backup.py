import time
import mwclient
from pathlib import Path

site = mwclient.Site("wiki.ifworlds.org")
root = Path("data")

ns_list = [
    ('模板', '模板'),
    ('主空间', ''),
    ('模块', '模块'),
    ('概念', '概念'),
    ('属性', '属性'),
    ('项目', '项目'),
    ('教程', '教程'),
    ('编辑推荐', '编辑推荐'),
    ('帮助', '帮助'),
    ('Form', 'Form')
]

reversed_ns = {
    v: k
    for k, v in site.namespaces.items()
}

missing_ns = {ns for _, ns in ns_list} - set(reversed_ns.keys())
assert not missing_ns, missing_ns

if __name__ == "__main__":
    for ns_name, ns in ns_list:
        ns_id = reversed_ns[ns]
        for p in site.allpages(namespace=ns_id):
            path = root / ns_name / f"{p.page_title}.txt"
            path.parent.mkdir(exist_ok=True, parents=True)
            print(f"{ns}:{p.page_title}")
            with open(path, 'w') as f:
                f.write(p.text())
            time.sleep(2)