import random   #랜덤 모듈 불러오기
from time import sleep  #실행 일시정지 모듈
import sys #파이썬 변수, 함수 직접 제어 모듈.

start="a"

user=input("\n               ○\n\n이것은 당신의 가상 고양이의 알입니다. \n\na버튼을 눌러 쓰다듬어 봅시다\n\n")

if user==start:
    
    print("             (^._.^)ﾉ \n\n축하합니다! 당신의 고양이가 태어났습니다.\n")
    sleep(1.5)
else:
    print("이런, 알이 싸늘하군요! 뭔가 잘못된 모양입니다....\n")
    sleep(1.5)
    sys.exit(1)
            
    

x=0
while x<10:
    
    needs=["             (ↀ ᆺ ↀ)\n\n당신의 고양이가 지루해 보입니다.\n",
           "             o ㅅ o;;\n\n당신의 고양이가 뭔가 급해 보입니다.\n",
           "             ㅇㅅㅇ)\n\n당신의 고양이가 밖을 가만히 응시하고 있군요...\n",
           "             ｡＾･ｪ･＾｡\n\n당신의 고양이에게서 꼬르륵 소리가 납니다.\n",
           "             ⋆ㅠㅅㅠ⋆\n\n당신의 고양이가 꼬질해졌습니다.\n"]
    need=random.choice(needs)
    print(need)
    if (needs.index(need))==int(input("무엇을 할까요? 숫자를 입력해주세요.\n\n0:놀아주기 1:화장실 가기 2:산책시키기 3:먹이주기 4:목욕시키기\n\n")):
        from time import sleep
        if (needs.index(need))==0:
            print("\n야바위 게임을 시작합니다.\n\n             ○ ● ○\n\n")
            options=["왼쪽","중앙","오른쪽"]
            computer=random.choice(options)
            user=input("어느 곳에 공이 들어 있을까요?(왼쪽,중앙,오른쪽)\n")
            if computer==user:
                print("\n정답을 맞췄습니다! \n\n             (=^･^=)\n\n당신의 고양이는 함께 노는 것이 즐거운 것 같습니다.\n\n")
                sleep(1.5)
            else:
                print("\n틀렸습니다... 당신의 고양이는 어딘가 시무룩해 보입니다.\n\n")
                sleep(1.5)  
        if (needs.index(need))==1:
          print("\n             o(=´∇｀=)o\n\n당신의 고양이가 상쾌해진 것 같아 보이는군요.\n\n")
          sleep(1.5)
        if (needs.index(need))==2:
          print("\n             (⁎>ㅅ<)\n\n당신의 고양이는 새로운 친구를 만나서 신이 난 것 같습니다!\n\n")
          sleep(1.5)
        if (needs.index(need))==3:
          print("\n             ﾍ(=^･ω･^= )ﾉ\n\n당신의 고양이는 만족한 것 같아 보입니다.\n\n")
          sleep(1.5)
        if (needs.index(need))==4:
          print("\n             ω(=＾・＾=)ω\n\n당신의 고양이는 뽀송해졌습니다.\n\n")
          sleep(1.5)
        x+=1
    else:
        print("｡＾x . x＾｡\n\n당신의 고양이가 사망했습니다. \n\nx를 눌러 조의를 표하십시오")
        end="x"

        user=input("")

        if user==end:
            print("고양아 안녕~")
            sleep(1.5)
            break
        else:
            break
else:
     print("당신의 고양이가 떠날 시간이 되었군요... 고양이는 당신을 잊지 못할 겁니다.\n\n\n｡＾x . x＾｡\n\n고양아 안녕~")
     sleep(1.5)
             
    
        
    

