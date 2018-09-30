data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 50000 == 0:
			print(len(data))
print('檔案讀取完了，總共有',len(data),'筆資料\n')

sum_len = 0
for d in data:
	sum_len += len(d)
avg = sum_len/len(data)
print('算出來了，留言的平均長度是',avg,'字\n')

filter = []
for d in data:
	if len(d) < 100:
		filter.append(d)
print('總共有',len(filter),'筆留言長度小於100\n')

good = []
for d in data:
	if 'excellent' in d:
		good.append(d)
print('總共有',len(good),'筆留言含有 excellent這個詞')

nasty = [m for m in data if 'nasty' in m]
print('其中有',len(nasty),'條留言有 nasty 這個詞')

#文字計數
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] >100:
		print(word, wc[word])

while True:
	 query = input('請問你想查什麼字:(退出請按 q)')
	 if query == 'q':
	 	print('感謝您使用本查詢功能')
	 	break
	 if query in wc:
	 	print(query, ' 出現過的次數是', wc[query], '次')
	 else:
	 	print('這個字沒有出現過哦')




