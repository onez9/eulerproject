# кратчайший пароль




with open('p079_keylog.txt', mode='r', encoding='utf8') as fi:
    import re
    txt=re.findall(r'\w+', fi.read())

    print(txt)