import translators as ts
import time
import sys

#Gets user input then reads file
lang = input('What language would you like to convert to?')
with open(sys.argv[1] + '.srt', 'r', encoding='utf-8') as f:     #Bug note, if user inputs invalid language, fix this.
    read_data = f.readlines()


#creates new list and stores translated strings
new_list = []
for i in read_data:
    if any(char.isalpha() for char in i):
        try:
            t = ts.translate_text(i, translator='google', to_language= lang)
            time.sleep(0.3)
            new_list.append(t + '\n')
            print(t)
        except:
            print('error')
            time.sleep(30)
    else:
        new_list.append(i)

#Creates new translated file    
with open(sys.argv[1] + '_' + lang + '.srt', 'w+', encoding='utf-8') as f:
    for i in new_list:
        f.write(i)


