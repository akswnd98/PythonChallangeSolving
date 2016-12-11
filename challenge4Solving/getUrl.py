from urllib import request

conn = request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
short_bytes = b""
short_bytes_list = []
short_str = ""
url_str = ""
i = 0
while 1:
    short_bytes = conn.read()

    short_bytes_list = list(short_bytes)
    short_bytes_list.reverse()

    i = 0
    for x in short_bytes_list:
        if x == b" "[0]:
            break
        i += 1

    short_bytes_list = short_bytes_list[0: i]
    short_bytes_list.reverse()
    short_bytes = bytes(short_bytes_list)
    short_str = str(short_bytes)[2: -1]
    if not short_str.isdigit():
        break
    
    url_str = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + short_str
    conn = request.urlopen(url_str)

print(url_str)
