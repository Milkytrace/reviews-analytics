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

