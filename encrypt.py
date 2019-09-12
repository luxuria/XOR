# 10進数表記の文字列を2進数表記の文字列に変換する
def convert_to_binary(s: str) -> str:
    binary_str: str = ''
    for c in s:
        binary_str += str(bin(ord(c)).replace('0b', ''))
    return binary_str

# 文字列を指定した字数に分轄したものを配列として返す、あまりはそのまま返す
# e.g. 'abcdefghijklmn' を 3文字ごとに分割
#       -> ['abc', 'def', 'ghi', 'jkl', 'mn']
def split_str_by_designated_number(s: str, designated_num: int) -> list:
    end = ''
    if len(s) % designated_num != 0:
        # 指定された文字数分後ろを切り取る
        end = s[designated_num * -1:]
        s = s[:designated_num * -1]

    array = []
    # 指定された文字数ごとに文字列を分割していく
    for _ in range(len(s) // designated_num):
        array.append(s[:designated_num])
        s = s[designated_num:]

    if end:
        array.append(end)

    return array

def enc(key: str, plain: str) -> str:
    key_len: int   = len(key)
    splitted_plain_list = split_str_by_designated_number(plain, key_len)
    encrypted: str = ''
    for splitted_plain in splitted_plain_list:
        for i in range(len(splitted_plain)):
            encrypted += str(int(splitted_plain[i]) ^ int(key[i]))
    return encrypted

with open('key.txt', 'r') as f:
    key = f.read().strip()
binary_key = convert_to_binary(key)

with open('flag.txt', 'r') as f:
    flag = f.read().strip()
binary_flag = convert_to_binary(flag)

cipher = enc(key=binary_key, plain=binary_flag)
with open('enc.txt', 'w') as f:
    f.write(cipher)