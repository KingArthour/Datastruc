
print('*** TorKham HanSaa ***')
word = input('Enter Input : ').split(',')

def tor_kum(word):
    check = ''
    word_list = []

    for each in word:
        action = each[0]
        if len(each) > 2:
            new_word = each[2:]
        else:
            new_word = ''
        
        if action == 'P':
            if (check == '' or check[-2:].lower() == new_word[:2].lower()) and len(new_word) > 1:
                word_list.append(new_word)
                check = new_word
                print(f"'{new_word}' -> {word_list}")
            else:
                return f"'{each[2:]}' -> game over"
        elif action == 'R':
            word_list = []
            check = ''
            print("game restarted")
        elif action == 'X':
            break
        else:
            return f"'{each}' is Invalid Input !!!"
    
    return ''

print(tor_kum(word))
