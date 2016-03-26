import re, urllib.request, urllib.parse

url = 'http://weibo.cn/'


class Spider:
    def __init__(self, cookie, user_id):
        self.cookie = cookie
        self.user_id = user_id
        self.base_url = url + str(user_id) + '?page='

    def run(self):
        f = open('output.csv', 'w')
        f.write('时间,转发,评论,赞\n')

        page_index = 1
        while True:
            page = self.send_request_to_weibo(self.base_url + str(page_index))
            post_list = get_post_list(page)
            if post_list is None:
                break
            else:
                for post in post_list:
                    post_data = get_data(post)
                    f.write(str.format('{},{},{},{}\n', get_time(post), post_data[1], post_data[2], post_data[0]))
                break

        f.close()

    def send_request_to_weibo(self, url):
        print(url)

        request = urllib.request.Request(url)
        request.add_header('Cookie', self.cookie)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36')
        response = urllib.request.urlopen(request)

        return response.read().decode('utf-8')


def get_post_list(page):
    pattern = r'<div class="c".*?<div class="s"></div>'
    return re.findall(pattern, page)


def get_data(post):
    pattern = r'赞\[(.*?)\].*?转发\[(.*?)\].*?评论\[(.*?)\]'
    data_array = re.findall(pattern, post)
    return data_array[len(data_array) - 1]


def get_time(post):
    pattern = r'<span class="ct">(.*?)</span>'
    return re.search(pattern, post).groups()[0]
