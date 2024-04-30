with open('file.txt', 'r') as file:
    sentences = file.readlines()[1:]  

words_list = []
for sentence in sentences:
    words = sentence.split()  
    words_list.extend(words)  

print('Kata-kata dalam file:')
print(words_list)


with open('file.txt', 'a') as file:
    file.write('\n')
    file.write('===============Kata Unik pada Isi Berita===============\n')
    
    for i in range(0, len(words_list), 12):
        words_chunk = words_list[i:i+12]  
        file.write(str(words_chunk) + '\n')


