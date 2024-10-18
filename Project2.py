class Person:                              # Person 클래스 정의
    def __init__(self, name, gender, age): # 속성을 초기화하는 메서드
        self.name = name                   # 이름
        self.gender = gender               # 성별
        self.age = int(age)                # 나이
        
    def display(self):                                                                     # display 메서드 정의
        print(f"이름은 {self.name}, 성별은 {self.gender}이며,\n나이는 {self.age}살입니다.")  # 이름, 성별, 나이 출력
        self.greet()                                                                       # greet 결과문도 같이 출력

    def greet(self):                                             # greet 메서드 정의
        if self.age >= 20:                                       # 나이가 20살 이상일 경우
            print(f"안녕하세요, {self.name}님! 성인이시군요!")    # 성인 인사문
        else:                                                    # 나이가 20살 미만일 경우
            print(f"안녕하세요, {self.name}님! 미성년자이시군요!") # 미성년자 인사문

def get_name():                                # 이름 입력받는 함수
    name = input("이름은 무엇입니까? ").strip() # 이름 입력받기
    return name                                # 이름 출력

def get_gender():                                              # 성별 입력받는 함수
    gender = input("성별은 무엇입니까? (male/female) ").strip() # 성별 입력
    if gender in ['male', 'female']:                           # male 또는 female인 경우
        return gender                                          # 성별 그대로 함수
    else:                                                      # 다른 값을 입력한 경우
        print("'male' 또는 'female'만을 입력하셔야 됩니다.")     # 성별을 다시 입력하라는 문자열 출력
        return get_gender()                                    # 성별 입력받는 함수 다시 로드

def get_age():                                                              # 나이 입력받는 함수
    while True:                                                             # 반복문
        try:                                                                # 예외가 발생할 수도 있는 코드
            age = int(input("나이는 몇 살이십니까? "))                       # 나이 입력
            if(age > 0):                                                    # 나이를 숫자로 잘 입력한 경우
                return age                                                  # 나이 그대로 출력
            else:                                                           # 나이를 정수 이외의 숫자로 입력한 경우
                print(f"{age}는 잘못된 값입니다. 나이를 다시 입력해주십시오.") # 다시 입력하라고 출력문
        except ValueError:                                                   # 나이를 숫자 이외의 값으로 입력한 경우
            print("나이는 숫자입니다. 숫자 값를 입력해 주십시오.")             # 다시 입력하라고 출력문

name, gender, age = get_name(), get_gender(), get_age() # 이름, 성별, 나이 입력 받기
my_name = Person(name, gender, age)                     # 이름, 성별, 나이 속성을 가진 my_name 객체 생성
my_name.display()                                       # my_name 객체가 display 메서드 사용하여 출력