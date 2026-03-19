# list type에 대해서 알아보기

nums = [10, 20, 30, 40, 50]
names = ["kim", "park", "jo", "oh", "choi"]

# list 에 들어있는 데이터를 앞에서부터 순서대로 참조하면서 어떤 동작을 할 일들이 많이 발생한다.
for item in nums : 
    print(item)


for item in names :
    print("names를 순서대로 출력중...")
    print(item)

r1 = range(5) # [0,1,2,3,4]
r2 = range(10) # [0,1,2,3,4,5,6,7,8,9]

print(r1)
print(r2)

for item in range(5):
    print(item)

# result2에 들어가는 값을 예상해보세요.
result2 = range(len(names))

# 반복문 돌면서 인덱스도 같이 필요하다면
for i in range(len(names)): # [0,1,2,3,4]
    print("list의 index와 함께 출력합니다")
    print(i, names[i]) # 반복문 돌면서 i에 들어있는 인덱스를 이용하여 순서대로 참조

print("종료합니다.")