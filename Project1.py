import random as rd # 랜덤 모듈 로드

while True:                                              # 게임이 끝나도 다시 하기 위해 while문 생성
    cpu_rd = rd.randint(1, 10)                           # 컴퓨터가 1부터 10까지 숫자 중 랜덤으로 하나 저장
    print("1과 10 사이의 숫자 중 하나를 입력해 주십시오.") # 숫자 정했다고 알려주고 입력하라고 알려줌
    
    while True:                                                              # 컴퓨터 숫자가 내가 입력한 숫자가 같지 않을 경우 반복
        try:                                                                 # 예외가 발생할 수도 있는 코드
            my_num = int(input("예상 숫자: "))                                # 예상 숫자 입력하고 저장
            if my_num in list(range(1, 11)):                                  # 입력한 숫자가 범위 안에 있을 경우
                if my_num < cpu_rd:                                           # 입력한 숫자가 컴퓨터 숫자보다 클 경우
                    print(f"{my_num}보다 큽니다. 다시 입력하세요.")            # 크다고 알려줌
                elif my_num > cpu_rd:                                         # 입력한 숫자가 컴퓨터 숫자보다 작을 경우
                    print(f"{my_num}보다 작습니다. 다시 입력하세요.")           # 작다고 알려줌
                else:                                                         # 입력한 숫자가 컴퓨터 숫자와 일치할 경우
                    print(f"{my_num}가 정답입니다.")                           # 정답이라고 출력
                    break                                                     # 맞쳤으므로 반복문 벗어남
            else:                                                             # 입력한 숫자가 범위 외의 숫자일 경우
                print(f"{my_num}은 범위를 벗어난 숫자입니다. 다시 입력하세요.") # 벗어났다고 알려주고 input_num 입력문으로 다시 되돌아감
        except ValueError:                                                    # 숫자 이외의 다른 값을 입력한 코드
            print("잘못된 입력입니다. 숫자를 입력해 주십시오.")                 # 다시 입력하라고 출력문 작성
    
    while True:                                                           # 게임을 계속할지 말지 여부 묻는 반복문
        y_n = input("게임을 다시 하시겠습니까? (y/n): ").lower()           # 게임을 다시 할지 여부를 알려줌 (대문자인 경우 소문자로 변환)
        if y_n == "y":                                                    # 게임을 다시 하고 싶을 경우
            break                                                         # 다시 처음 반복문으로 돌아감
        elif y_n == "n":                                                  # 게임을 그만 하고 싶을 경우
            print("게임을 종료합니다. 다음에 또 만나요!")                   # 게임 종료문 알림
            exit()                                                        # 강제 종료
        else:                                                             # y와 n 이외의 다른 값을 입력한 경우
            print(f"{y_n}는 잘못된 입력입니다. y 또는 n으로 입력해 주세요.") # 다시 입력하라고 출력문 작성