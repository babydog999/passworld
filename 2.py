x = 2
x = int(x)
while True :
	passworld = input('請輸入密碼:')
	if passworld != '789ggg321':
		print('密碼錯誤!還有', x , '次機會')
		x =x-1
		if x < 0 :
			break

	elif passworld == '789ggg321' :
		print('登入成功')
		break
		

