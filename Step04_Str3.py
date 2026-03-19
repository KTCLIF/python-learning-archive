# yaml 형식의 문자열 다루기

# yaml 문자열을 다룰 때는 외부 모듈을 pip로 설치를 해서 import를 해야한다.
# python 환경을 구성하고 pip install pyyaml 설치 후에 yaml을 다를 수 있다.

# info = '''
# name: 가나다
# addr: 한국
# foods: 
#   - 불고기
#   - 잡채
# isMan: False
# body:
#   wight: 60
#   height: 170
# '''

# 검색 혹은 ai의 도움을 받아서 info에 들어있는 문자열을 dict type으로 바꾸세요
# 그런 다음 dict 에 들어있는 내용을 확인 후 다시  dict에 있는 내용을 이용해서 yaml 문자열 형식으로 변환해보세요.
# 가상환경의 인터프리터로 전환해야함


import json
import yaml

info = '''
{
    "name":"S25",
    "bir":"2025",
    "spec":
    {
        "memory":"512",
        "color":"blue"
    }
}
'''

data_dict = json.loads(info)
print(f"변환: {type(data_dict)}")
print("--- dict ---")
print(data_dict)

yaml_string = yaml.dump(data_dict, allow_unicode=True)
print("\n--- yaml ---")
print(yaml_string)


# yaml 형식의 문자열을 로딩해서 dict type 으로 변경하기
result = yaml.safe_load(info)

print(result)

# result(dict type)을 다시 형식으로 변환하기
result2=yaml.dump(result, allow_unicode=True, sort_key=False)

print(result2)

print("종료합니다.")