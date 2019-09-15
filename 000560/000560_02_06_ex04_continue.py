#000560_02_06_ex04_continue.py
i = 0
while True:
	i=i+1
	if i == 2:
		print ('skipping(i=2)')
		continue
	if i == 5:
		print ('breaking(i=5)')
		break
	print (i)
	
print ('Finished')