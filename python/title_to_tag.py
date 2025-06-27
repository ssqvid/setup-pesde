import json
import subprocess
import sys


def title_to_tag(title: str) -> str:
    out = subprocess.check_output(
        'gh release list -R pesde-pkg/pesde --json tagName,name',
        shell=True,
    )

    versions = json.loads(out)

    tag = ''

    for v in versions:
        if v.get('name') == title:
            tag = v.get('tagName')

    if not tag:
        sys.exit(1)

    return tag


if __name__ == '__main__':
    title = sys.argv[1]
    print(title_to_tag(title))
