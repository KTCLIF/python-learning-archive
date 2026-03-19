# dict type에 대해서 알아보자

'''
    - dict type
    1. key:value 형태로 데이터를 저장한다.
    2. 순서가 없는 데이터이다.
    3. key 값을 잉룡해서 저정된 값을 참조한다.
'''

# 회원 1명의 데이터
mem1 = {"num":1, "name":"kimgura", "isMan":True}
# 회원 1명의 데이터
# info1 = [1, "kimgura", True]
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

# dict 안의 내용을 수정하기
mem1["num"] = 2
mem1["name"] = "이정호"
mem1["isMan"] = False

mem2={"num":2, "name":"해골", "isMan":False}


print("종료됩니다")