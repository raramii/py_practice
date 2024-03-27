# not 연산자 조합하기
x = 10
under_20 = x < 20
print("under_20: ", under_20)
print("not under_20: ", not under_20)

# 조건문 기본 활용
# if문을 사용하여 양수를 입력하면 "양수"
# 음수 입력하면 "음수"
# 0 입력하면 "0" 출력

num = input("정수 입력 : ") # 입력받기
num = int(num) # 정수로 형변환

if num > 0 :
    print("양수")

if num < 0 :
    print("음수")

if num == 0 :
    print("0")

# 시간 가져와서 오전, 오후 판단
import datetime # 시간 가져오는 라이브러리 호출

now = datetime.datetime.now() # 현재시간 가져오기

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 오전, 오후 구분
import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print("현재 시간은 {}시로 오전".format(now.hour))

if now.hour > 12 :
    print("현재 시간은 {}시로 오후".format(now.hour))

# 계절 구분
import datetime
season = datetime.datetime.now()

if 3 <= season.month <= 5 :
    print("현재는 {}월이므로 봄".format(season.month))

if 6 <= season.month <=8 :
    print("현재는 {}월이므로 여름".format(season.month))

if 9 <= season.month <= 11 :
    print("현재는 {}월이므로 가을".format(season.month))

if 12 <= season.month <= 2 :
    print("현재는 {}월이므로 겨울".format(season.month))

# 숫자를 입력 받아 끝자리로 짝수 홀수 구분
# 1.
num = input("숫자 입력 : ")
num = int(num)

if num % 2 == 0:
    print("짝수")

if num % 2 != 0:
    print("홀수")

# 2.
num = input("입력 : ")
last_character = num[-1]
last_number = int(last_character)
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수")

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수")

# 3.
num = input("입력 : ")
last_character = num[-1]

if last_character in "02468":
    print("짝수")

if last_character in "13579":
    print("홀수")