ip_addr = input("ip 주소입력:(예192.168.0.1)")

# .으로 분리해서 list에 담아오기
ip_parts = ip_addr.split(".")

# list 안에 저장된 item 확인
print(ip_parts)

# 빈 배열을 하나 만들고
binary_parts=[]
for item in ip_parts:
    # :08b 는 뒤에서부터 읽으면 b(2진수)로 변환하되 총 8자리로 변환하고
    # 빈 곳은 0으로 채움
    print(f"{int(item):08b}")
    binary_parts.append(f"{int(item):08b}")

print(binary_parts)

result = ".".join(binary_parts)

print(result)

print(f" 입력한 ip: {ip_addr}")
print(f" 2진수 변환한 ip: {result}")