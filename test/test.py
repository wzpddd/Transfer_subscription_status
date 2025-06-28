from http.client import responses

import requests

url = "https://test-admin-fomsv2.everimaging.com/api/user_info?appleName=&pageNo=1&pageSize=10&type=email&value=wzptestpro01%40fotor.com"
cookies = {
    "fotorAdmin.sid":"s%3AorrQWQQl9u5cWYqbOW19a8NNZkf5vHnf.i3IcxUxN0G3vLDOVV4bsngKhIS%2F0L9KLXft0GF%2FXs%2F4; Path=/; Expires=Sun, 29 Jun 2025 17:02:17 GMT; HttpOnly"
}

responses = requests.get(url, cookies=cookies).json()
uid = responses.get('data', [{}])[0].get('uid')
print(uid)
