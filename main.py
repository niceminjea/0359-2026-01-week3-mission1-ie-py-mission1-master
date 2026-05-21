# 파일이름 :특급전사 판독기
# 작 성 자 :김민재

subjects = ['팔굽혀펴기','뜀걸음','사격','윗몸일으키기','정신전력']
soldiers = {}

def input_scores (name) :
    grades = []
    specialcount = 0
    scores = []
    total = 0
    print(f'{name} 병사 특급전사 판별 시작')
    
    for i in range (len (subjects)):
        subject = subjects[i]
        score = int(input(f'{subject} 점수를 입력하시오:'))

        if score < 0 :
            print('음수이므로 오류입니다')
            score = 0
        elif score > 100 :
            print('100점 초과는 오류입니다.')
            score = 0

        scores.append(score)
        total += score

        print(f'({subjects[i]}: {score}점')

    print(f'총점: {total}점 / 500점')

    if total >= 450 :
        result = '특급전사'
    elif total >= 400: 
        result = '1급'
    elif total >= 350:
        result = '2급'
    else :
        result = '불합격 보충 체력단련 요망'
    return {'scores': scores, 'total':total, 'result':result}

def show_result(name,value):
    print(f'{name} 병사 판별 결과 확인')
    for i in range(len(subjects)):
        print(f'{subjects[i]}: {value["scores"][i]}점')
        print(f'총점: {value["total"]}점/500점')

        if value ['result'] == '특급전사' :
            print('축하합니다! 특급전사입니다')
            print('2박3일 포상휴가 지급입니다')
        else :
            print('특급전사가 아닙니다')
            print(f'특급전사까지 {450-value["total"]}점 남았다')

def analyze():
    global soldiers

    if len(soldiers) == 0:
        print('병사 데이터를 다시 입력하세요')
        return
    
    total_count = len(soldiers)
    special_soldiers = []

    for name, data in soldiers.items():
        if data ['result'] == '특급전사':
            special_soldiers.append(name)

    print(f'전체 분석 결과')
    print(f'총 평가 병사 수:{total_count}명')
    print(f'특급전사 수:{len(special_soldiers)}명')

def judge_special(name, scores):
    total = 0
    print(f'{name} 병사 판별 결과')

    for i in range(len(subjects)):
         print(f'  {subjects[i]}: {scores[i]}점')
         total += scores[i]
    print(f'  총점: {total}점 / 500점')

    special = total >= 450
    return special

while True: 
    print('특급전사 판별 프로그램')
    print('1.입력')
    print('2.조회')
    print('3.분석')
    print('4.판별')
    print('5.종료')
    choice = input('항목을 선택하시오')

    if choice == '1' :
        name = input('평가할 병사의 이름을 입력하시오:')
        value = input_scores(name)
        soldiers[name]=value
        print(f'판정결과: {value["result"]}')
    
    elif choice == '2':
        if len(soldiers)==0:
            print('병사이름을 입력하시오')
        else:
            name = input('조회할 병사의 이름을 입력하시오:')
            if name in soldiers:
                show_result(name,soldiers[name])
            else:
                print(f'{name}병사 데이터가 없습니다.')
    elif choice == '3':
        analyze()

    elif choice == '4':
        name = input('판별할 병사의 이름을 입력하시오:')
        scores = []
        for subject in subjects:
            score = int(input(f'{subject}점수를 입력하세요:'))
            scores.append(score)

        result = judge_special(name,scores)

        if result:
            print(f'{name}병사는 특급전사입니다')
        else: 
            print(f'{name}병사는 특급전사가 아니다')

    elif choice == '5':
        print('프로그램을 종료합니다 건강한 군생활 하십쇼')
        break
    else:
        print('다시 입력하시오')

