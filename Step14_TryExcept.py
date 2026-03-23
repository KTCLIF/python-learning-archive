
# main으로 실행했을 때(현재 파일에서 run 했을 때) 실행할 code 블럭
if __name__ == "__main__" :
  
  try:
    # 문자열
    num1_str : str = input("젯수 입력:")
    num2_str : str = input("피젯수 입력:")

    # 입력한 문자열을 숫자로 형변환
    num1 : int = int(num1_str)
    num2 : int = int(num2_str)

    result = num2/num1

    # 결과를 출력
    print(f"{num2}를 {num1}으로 나눈 결과값 : {result}")
  except Exception as e:
    print("어떤 에러가 발생했습니다.",e)
  else: # 예외가 발생하지 않으면 실행이 되는 블럭 //필요성이 낮은 블럭
    pass
  finally: # 정상수행 or 예외가 발생해도 반드시 실행이 보장되는 블럭
    pass

  # except ValueError as ve: # ve에는 에러 정보가 들어있다.
  #   print(ve)
  # except ZeroDivisionError as zde:
  #   print(zde)
  #   print("어떤 수를 0으로 나눌 수는 없습니다!")

  # 어떤 중요한 마무리 작업을 합니다.
  print ("중요한 마무리 작업을 합니다")