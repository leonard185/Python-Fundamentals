Text = input('Text:')

count = 0

for character in Text:
    if (character in 'aAeEiIoOuU'):
        count += 1
        print('Count:',count)