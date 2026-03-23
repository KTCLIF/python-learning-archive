# BinaryTest/gui02.py

# ui ToolKit 을 사용할수 있는 interface 객체 import 하기 
import tkinter as tk

def clicked():
    print("버튼을 클릭했네요?")
    # Entry(입력창) 에 입력한 문자열 읽어오기
    input_value=entry.get().strip() # 좌우 공백 제거 strip()
    # 빈 값일 경우 안내 문구 표시
    if not input_value:
        return # 함수를 호출한 곳으로 실행의 흐름을 돌려준다(함수를 여기서 종료한다)

    try:
        # 입력한 문자열을 정수로 변환
        num = int(input_value)
        # 2진수 형태의 문자열로 변경해서 
        binary_result = f"{num:08b}"
        # 출력하기
        result_label.config(text=binary_result, fg="blue")
    except Exception as e:
        result_label.config(text="숫자만 입력 가능 합니다", fg="red")
   

if __name__ == "__main__" :
    # root 창 생성
    root = tk.Tk()
    # 제목 설정 
    root.title("나의 App")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text="10 진수를 2진수로 변환")
    # pady => padding y => y축 padding => 위아래 padding
    label.pack(pady=20)

    # 입력창 
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() 