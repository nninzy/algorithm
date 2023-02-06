text = input()
happy = text.count(':-)')
sad = text.count(':-(')
emotion = [happy, sad * (-1)]
if happy == 0 and sad == 0:
    print('none')
else:
    total = sum(emotion)
    print('unsure' if total == 0 else 'happy' if total > 0 else 'sad')