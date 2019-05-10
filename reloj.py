import time,os
while True:
	t=time.localtime()
	os.system("cls")
	print(str(t[3])+":"+str(t[4])+":"+str(t[5]))
	time.sleep(1)