import requests
import json

book_id = '4305547728'
url = "http://dushu.baidu.com/api/pc/getDetail?data={%22book_id%22:%22"+book_id+"%22}"
users = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
        }
if __name__ == '__main__':
    r = requests.get(url,headers=users)
    j = json.loads(r.text)
    book_name = j['data']['novel']['book_name']#书名
    book_title = j['data']['novel']['lastChapter']['chapter_title']#章节名
    update_time = j['data']['novel']['lastChapter']['cp_update_time']#更新时间
    print("书名："+book_name)
    print("标题："+book_title)
    print("更新时间："+update_time)
