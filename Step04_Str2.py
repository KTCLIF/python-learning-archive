# Step04_STr2.py

"""
    여러분의 이름과, 주소, 좋아하는 음식 2가지를 작성해서 채팅차에 올려보세요

    json, xml, yaml ...

    jason은 javascript 객체 표기법을 따르는 문서 형식이다.
    {
    "name":"가나다",
    "addr":"한국",
    "foods":["불고기","잡채"]
    }
    //{
    "key":value, //value = 10/10.1/"xxx"/true/false/{}/[]/null 숫자/문자/논리값/object/array/빈값(7가지)
    }

"""

# json 모듈 import 하기
import json
import re

# info는 str type 이긴 한데 문자열이 특별한 형식(json)을 띄고 있다.
info = '''{
    "name":"가나다",
    "addr":"한국",
    "foods":["불고기","잡채"]
}
'''

# result는 str(json형식)의 문자열이 python의 dict로 변경된 값을 갖고 있다. //info는 문자열이기 때문에 그대로 사용 X
result = json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

# dict에 저장된 데이터를 json 문자열로 변환 //반대동작 json.loads <-> json.dumps
result2 =json.dumps(result)

print("종료됨")