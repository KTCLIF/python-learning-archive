"""
    fuction type

    - 특정 시점에 여러 줄의 code를 일괄 실행하고자 할 때 사용한다.
    - 함수도 data 이다 (변수에 담을 수 있다)
    - 함수 안에 저장된 code를 일괄 실행하는 것을 함수를 call 한다고 이야기한다.
    - 함수는 저장된 code를 다 실행하고 나면 원래 call 했던 위치로 실행의 흐름이 넘어온다.
    - call  했던 위치로 돌아오면서 어떤 data를 반드시 가져온다.

"""

def test1():
    print("test1() 호출됨")

test1()
result1 = test1()

# 매개변수가 선언되어 있는 함수
# 매개변수에 대입할 값을 전달해야지 호출 할 수가 있다.
# 매개변수의 이름은 마음대로 지을 수 있따.

def test2(arg):
    print("전달 받은 내용:", arg)
    print(f"전달 받은 내용: {arg} ")

test2(None)
test2(10)
test2("kim")

# 값(숫자)을 2개 전달 받아서 전달 받은 두 수의 합을 출력하는 함수
def print_sum(num1: int, num2: int): #강제되는 것은 아니나 타입 힌트를 명시할 수 있음
    # num1 = 10
    # num2 = 20
    sum = num1+num2
    print(f"{num1} + {num2} = {sum}")

print_sum(10, 20)
print_sum(5,7)

def print_info(name: str, addr: str):
    print(f" 이름은 {name} 이고 주소는 {addr}")

print_info("김구라", "노량진")
# keyword를 이용해서 인자(argument)를 전달할 수도 있다.
print_info(addr="행신동", name="해골")

def get_sum(num1: int, num2: int):
    sum=num1+num2
    return sum

result2 = get_sum(10, 20)
# 함수 호출 시 어떤 값으로 대체가 된다. //최종적으로 남는 것은 str 데이터


print("종료됩니다.")