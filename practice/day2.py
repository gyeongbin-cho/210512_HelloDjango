#if문 예제2
# lions = ["임영빈","김민지","김현조","김재원"]
# lionking = " 한지훈"

# if lionking in lions:
#   print("아... 회장님 안녕하세요")
  
# else:
#   print("어 회장님 안오셨는데요")

#if문 예제3
# score = 86
# if score >= 90:
#   print("A입니다")
# elif score >= 80:
#   print("B입니다")
# elif score >= 70:
#   print("C입니다")
# else:
#   print("F입니다")

#반복문
# for i in range (10,13):
#   print(i,"번 손님 주문하신 음료나왔습니다!")

#for문 예제2 코드
# cookies = ["우유맛쿠키","라떼맛쿠키","허브맛쿠키"]

# for jelly in cookies:
#   print(jelly,"일해라!")

#while문(똑같은 반복문)
# num =1
# while num<11:
#   print(num,"번 손님 주문하신 음료나왔습니다!")
#   num = num+1

# mental = 50
# while True:
#   print("강의를 듣습니다")
#   mental = mental-10
#   print("현재 멘탈 게이지 :",mental)
#   if mental == 0:
#     print("제발 이제 그만")
#     break

# num = 0
# while num < 10:
#     num = num+1
#     if num % 2 == 0:
#         continue
#     print("홀수 :", num)

#쓰기 귀찮을때 사용하기 유용함
# a = 2
# b = 3

# c = 20
# d = 30

# def add(a,b):
#   print("지금 입력된 수는", a, "와", b, "이다")
#   return a+b

# print(add(a,b))
# print(add(c,d))
# print(add(10,100))

# a = 7
# b = 3

# def add(a,b):
#   return a+b

# sum = add(a,b)
# print(sum)

	
# def add2(a,b):
#   if a>5:
#     return "a가 5보다 큼"
#   return a+b
 
# sum2 = add2(a,b)
# print(sum2)

#함수
# num = int(input("숫자를 입력하세요"))


# def func(num):
#     if(num > 10):
#         print("10보다 큽니다")
#     elif(num == 10):
#         print("10과 같습니다")
#     else:
#         print("10보다 작습니다")


# func(num)

#클래스 선언
# class Member:
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major

#     def show_info(self):
#         print("이름은", self.name)
#         print("학과는", self.major)

#     def work(self):
#         print(self.name,"일하세요 일")

#     def order_time(self, time):
#         print("{0}씨 {1}까지 다 해오세요".format(self.name, time))

# #객체 생성
# member1 = Member("임영빈", "컴퓨터공학과")
# member2 = Member("김민지", "문화콘텐츠문화경영학과")
# member3 = Member("김현조", "정보통신공학과")
# member4 = Member("김재원", "전자공학과")
# member5 = Member("한지훈", "컴퓨터공학과")

# #영빈오빠 자기소개시키기
# member1.show_info()
# #민지언니 일시키기
# member2.work()
# #현조언니 재촉하기
# member3.order_time("9시")
# #김재원 이름출력
# print(member4.name)
# #한지훈 과 출력
# print(member5.major)