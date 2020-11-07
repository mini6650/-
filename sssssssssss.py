
start="a"

user=input("               ○\n\n이것은 당신의 가상 고양이의 알입니다. \n\na버튼을 눌러 쓰다듬어 봅시다\n\n")

if user==start:
    print("             (^._.^)ﾉ \n\n당신의 고양이가 태어났습니다!\n")
    import random
    needs=["(๑ↀ  ᆺ ↀ๑)\n\n당신의 고양이가 지루해 보입니다.",
           "o ㅅ o;;\n\n당신의 고양이가 뭔가 급해 보입니다.",
           "당신의 고양이가 밖을 가만히 응시하고 있군요...",
           "｡＾･ｪ･＾｡\n\n당신의 고양이에게서 꼬르륵 소리가 납니다.",
           "⋆ටᆼට⋆\n\n당신의 고양이가 꼬질해졌습니다."]
    need=random.choice(needs)
    print(need)

else:
    print("이런, 알이 싸늘하군요! 뭔가 잘못된 모양입니다.\n")
