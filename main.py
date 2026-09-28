import re

def parse():
    with open("test.md") as f:
        content = f.read()
    urls = re.findall(r'(?<!\!)\[[^\]]+\]\((https?://[^\s)]+)\)', content)
    print(urls)
    return 0

def main() -> int:
    p = parse()
    print(p)
    return p

main()