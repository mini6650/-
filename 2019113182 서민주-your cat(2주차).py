
start="a" #시작 버튼 변수 지정

user=input("               ○\n\n이것은 당신의 가상 고양이의 알입니다. \n\na버튼을 눌러 쓰다듬어 봅시다\n\n") #사용자의 입력 받음

if user==start: #사용자의 입력과 시작 버튼의 변수(start)가 같을 시 고양이가 태어남.
    print("             (^._.^)ﾉ \n\n당신의 고양이가 태어났습니다!\n")
    import random #랜덤 모듈을 불러옴.
    needs=["             (๑ↀ ᆺ ↀ๑)\n\n당신의 고양이가 지루해 보입니다.\n", #고양이의 요구사항을 리스트로 구성.
           "             o ㅅ o;;\n\n당신의 고양이가 뭔가 급해 보입니다.\n",
           "             당신의 고양이가 밖을 가만히 응시하고 있군요...\n",
           "             ｡＾･ｪ･＾｡\n\n당신의 고양이에게서 꼬르륵 소리가 납니다.\n",
           "             ⋆ටᆼට⋆\n\n당신의 고양이가 꼬질해졌습니다.\n"]
    need=random.choice(needs) #고양이의 요구사항중에 랜덤으로 한가지를 지정하고, 이를 need라는 변수로 선언.
    print(need) #need변수를 출력.
    if (needs.index(need))==int(input("무엇을 할까요? 숫자를 입력해주세요.\n\n0:놀아주기 1:화장실 가기 2:산책 3:먹이주기 4:목욕시키기\n\n")):#need변수의 인덱스 값을 알아내고 그 값과 사용자의 입력값 비교
        if (needs.index(need))==0:
          print("당신의 고양이가 즐거운 것 같습니다.(=^･^=)") #같다면 고양이의 상호작용 스크립트 출력.
       
    else:
        print("당신의 고양이가 사망했습니다. 고양아 안녕~｡＾x . x＾｡") #틀릴 경우 고양이 사망. 시작 버튼의 변수 지정한것과 같은 방식으로 x버튼을 눌러 게임을 종료하는 코드 구성 예정.

x=0     #while문 사용하여 10번 반복하면 고양이가 사망하도록 하는 코드 구성 예정....
while x<10:
x+=1


else:
    print("이런, 알이 싸늘하군요! 뭔가 잘못된 모양입니다.\n") #시작 버튼의 변수 틀릴 경우 알의 부화실패.


