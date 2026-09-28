import re

def test1() -> bool:
    with open("test.md") as f:
        content = f.read()
    urls = re.findall(r'(?<!\!)\[[^\]]+\]\((https?://[^\s)]+)\)', content)
    correct = ['https://link1.com', 'https://link3.com']
    if urls == correct:
        return True
    else:
        return False

def test2() -> bool:
    with open("test.md") as f:
        content = f.read()
    urls = re.findall(r'(?<!\!)\[[^\]]+\]\((./[^\s)]+)\)', content)
    correct = ['./link4.md', './link8.md']
    if urls == correct:
        return True
    else:
        return False

def test3() -> bool:
    with open("test.md") as f:
        content = f.read()
    urls = re.findall(r'(?<!\!)\[[^\]]+\]\((/[^\s)]+)\)', content)
    correct = ['/link5.md', '/link7.md']
    if urls == correct:
        return True
    else:
        return False

def test4() -> bool:
    with open("test.md") as f:
        content = f.read()
    urls = re.findall(r'(?<!\!)\[[^\]]+\]\((#[^\s)]+)\)', content)
    correct = ['#link2', '#link6']
    if urls == correct:
        return True
    else:
        return False

def main():
    if test1() == True:
        print('passed')
    else:
        print('failed')
    
    if test2() == True:
        print('passed')
    else:
        print('failed')
    
    if test3() == True:
        print('passed')
    else:
        print('failed')
    
    if test4() == True:
        print('passed')
    else:
        print('failed')

main()