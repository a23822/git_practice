import webbrowser

# 모모랜드 모든 멤버들의 검색 페이지를 한 번에 여는 코드

arr = ["나윤" ,"혜빈", "아인" ,"낸시", "주이" ,"연우" ,"제인", "데이지", "태하"]

url = "https://search.daum.net/search?q="

# 리스트를 한번씩 돌면서 웹 브라우저를 연다.
for member in arr:
    webbrowser.open(url+member)

"""
keyword = input("모모랜드 멤버 중 한 명의 이름을 적어주세요 : ")

webbrowser.open(url+ keyword)
"""