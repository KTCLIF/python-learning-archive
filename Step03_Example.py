"""
    회원 한명의 정보는 번호, 이름, 주소로 이루어져있다. //dict
    그리고 그러한 회원이 여러 명이다.
    여러 명의 회원 목록을 하나의 묶음으로(하나의 data)로 순서대로 관리하고 싶다면  //순서대로 = list
"""

# 3명의 회원정보를 각각 dict 에 담은 다음 그 dict를 list에 담는 코드를 작성해서 채팅창에 보내보세요.
mem1 = {"num": 1, "name": "회원1", "addr": "주소1"}
mem2 = {"num": 2, "name": "회원2", "addr": "주소2"}
mem3 = {"num": 3, "name": "회원3", "addr": "주소3"}
# dict 3개를 list에 담기
members = [mem1, mem2, mem3]

a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]
