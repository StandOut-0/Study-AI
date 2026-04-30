# '''
#  키보드로 입력받아 요구대로 처리하고 출력하시오.
#  입력 내용 :
#   회원이름 : 이순신 (member_name : str)
#   회원아이디 : leess88@hi.org (member_id : str)
#   패스워드 : pass1234 (member_passwd : str)
#   나이 : 45 (age : int)
#   키 : 187.5 (height : float)
# 출력 내용 : format() 메소드 사용함
#  이순신 회원의 아이디는 leess88@hi.org 이고, 암호는 pass** 입니다.
#  나이는 45세이고, 키는 187.5 cm 입니다.
 
# 출력시 처리조건 :
#   암호는 첫글자부터 4글자만 슬라이싱한 다음 나머지 글자수에 맞춰서     * 로 출력되게 함
#   키는 소숫점아래 첫자리까지만 출력되게 포멧팅함
# '''

# member_name = input("회원이름 : ")
# member_id = input("회원아이디 : ") 
# member_passwd = input("패스워드 : ")
# age = int(input("나이 : "))
# height = float(input("키 : "))
# passwd_len = len(member_passwd)
# print(
#     "{} 회원의 아이디는 {} 이고, 암호는 {}{} 입니다."
#     .format(
#         member_name, 
#         member_id, 
#         member_passwd[:4], "*" * (passwd_len - 4)))
# print("나이는 {}세이고, 키는 {:.1f} cm 입니다."
#     .format(age, height))

# # format 함수와 format 서식
# print_str1 = "나이는 {}세이고, 키는 {:.1f} cm 입니다."
# print_str2 = "나이는 %d세이고, 키는 %.1f cm 입니다."
# print(print_str1.format(age, height))
# print(print_str2 % (age, height))

# 진수
print("10진수: %d" % 10)
print("8진수: %o" % 10)
print("16진수: %x" % 10)

# 실수형
print("실수형: %f" % 3.141592)
print("소숫점 2자리까지: %.2f" % 3.141592)

# 문자열
print("문자열: %s" % "Hello")
print("문자열: %10s" % "Hello") # 10칸 확보 후 오른쪽 정렬
print("문자열: %-10s" % "Hello") # 10칸 확보 후 왼쪽 정렬