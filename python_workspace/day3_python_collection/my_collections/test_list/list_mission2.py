"""
    키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
입력 내용 :
    국어 점수 : 78.5 (kor : float)
    영어 점수 : 88.7 (eng: float)
    수학 점수 : 93.5 (mat : float)
처리 내용 :
    3명의 학생 점수를 입력 받음, 각 학생의 총점과 평균은 각각 계산함
    학생별 점수는 각 리스트에 저장한 다음, [국어, 영어, 수학, 총점, 평균]
    각 학생 점수를 리스트(sungjuk_list)에 순서대로 저장 처리함
    [[국, 영, 수, 총, 평], [국, 영, 수, 총, 평], [국, 영, 수, 총, 평]]
    3명의 점수의 총합(total_score : int)과 전체평균(average_score : float)를
    계산하시오.
출력 내용 :
    리스트에 저장된 값들을 출력함,   국, 영, 수, 총, 평균 순서로 출력
     -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
    전체 총점과 전체 평균을 출력하시오.
    이때 반복문이나 조건문을 사용하지 않는다.
"""

def practice1():
    korean_score1 = float(input("국어 점수 : "))
    english_score1 = float(input("영어 점수 : "))
    math_score1 = float(input("수학 점수 : "))
    total_score1 = korean_score1 + english_score1 + math_score1
    average_score1 = total_score1 / 3

    sungjuk_list1 = [korean_score1, english_score1, math_score1, total_score1, average_score1]
    print("국어: {:.2f}, 영어: {:.2f}, 수학: {:.2f}, 총점: {:.2f}, 평균: {:.2f}".format(
        sungjuk_list1[0], sungjuk_list1[1], sungjuk_list1[2], sungjuk_list1[3], sungjuk_list1[4]
    ))  




    korean_score2 = float(input("국어 점수 : "))
    english_score2 = float(input("영어 점수 : "))
    math_score2 = float(input("수학 점수 : "))
    total_score2 = korean_score2 + english_score2 + math_score2
    average_score2 = total_score2 / 3

    sungjuk_list2 = [korean_score2, english_score2, math_score2, total_score2, average_score2       ]
    print("국어: {:.2f}, 영어: {:.2f}, 수학: {:.2f}, 총점: {:.2f}, 평균: {:.2f}".format(
        sungjuk_list2[0], sungjuk_list2[1], sungjuk_list2[2], sungjuk_list2[3], sungjuk_list2[4]
    ))  




    korean_score3 = float(input("국어 점수 : "))
    english_score3 = float(input("영어 점수 : "))
    math_score3 = float(input("수학 점수 : "))
    total_score3 = korean_score3 + english_score3 + math_score3
    average_score3 = total_score3   / 3

    sungjuk_list3 = [korean_score3, english_score3, math_score3, total_score3, average_score3       ]
    print("국어: {:.2f}, 영어: {:.2f}, 수학: {:.2f}, 총점: {:.2f}, 평균: {:.2f}".format(
        sungjuk_list3[0], sungjuk_list3[1], sungjuk_list3[2], sungjuk_list3[3], sungjuk_list3[4]
    ))  


    total_score = total_score1 + total_score2 + total_score3
    average_score = total_score / 3
    print("총점: {:.2f}, 평균: {:.2f}".format(
        total_score, average_score
    ))



practice1()