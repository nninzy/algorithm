quiz = 0; start = input(); text = ""
while start == "고무오리 디버깅 시작" :
    text = input()
    if text == "고무오리 디버깅 끝" : break;
    elif text == "문제" : quiz += 1
    elif text == "고무오리" :
        if quiz <= 0 : quiz += 2
        else : quiz -= 1
print("고무오리야 사랑해" if quiz == 0 else "힝구")