import http.client
import json

# 表示するユーザ名
USER_ID = "hypervisitor"
# ユーザの投稿数
ITEM_NUM = 10
# ページ番号 (1から100まで)
PAGE = "1"
# 1ページあたりに含まれる要素数 (1から100まで)
PAR_PAGE = "100"

conn = http.client.HTTPSConnection("qiita.com", 443)

conn.request("GET", "/api/v2/users/" + USER_ID + "/items?page=" + PAGE + "&per_page=" + PAR_PAGE)
res = conn.getresponse()
print(res.status, res.reason)
data = res.read().decode("utf-8")

# 文字列からJSON オブジェクトへでコード
jsonstr = json.loads(data)
ITEM_NUM = len(jsonstr)
print(type(jsonstr))
if isinstance(jsonstr, list) == True:
    print("list type")

iterable = iter(jsonstr)


if isinstance(jsonstr[0], dict) == True:
    print("dict type")

print("==========================================================")
# ヘッダ出力
print("\"no\",\"created_at\",\"tile\",\"url\"")

# 投稿数を指定
for num in range(ITEM_NUM):
    print(type(jsonstr[num]))
    created_at = jsonstr[num]['created_at']
    tile = jsonstr[num]['title']
    url = jsonstr[num]['url']

    # ダブルクォートありCSV形式で出力
    print("\"" + str(num) + "\",\"" + created_at + "\",\"" + tile + "\",\"" + url + "\"")

print("==========================================================")
conn.close()