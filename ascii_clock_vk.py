###12 hour clock
#Vishwa Code Section
elif t_type == 12:
	if (t_type == 12):
    	if (hour > 12):
        	hour_extra = hour
        	hour -= 12
        	clock[0] = str(int(hour/10))
        	clock[1] = str(int(hour%10))
	if char != '':  
    	for i in range(5):
        	for j in range(len(clock)):
            	if clock[j]==':':
                	print(colon[i], end=' ')
            	if clock[j] == '0':
                	if j != 0:
                    	print(zero[i].replace('0', char), end=' ')
            	if clock[j] == '1':
              	print(one[i].replace('1', char), end=' ')
            	if clock[j] == '2':
              	print(two[i].replace('2', char), end=' ')
            	if clock[j] == '3':
              	print(three[i].replace('3', char), end=' ')
            	if clock[j] =='4':
                	print(four[i].replace('4', char), end=' ')
            	if clock[j] =='5':
                	print(five[i].replace('5', char), end=' ')
            	if clock[j] =='6':
                	print(six[i].replace('6', char), end=' ')
            	if clock[j] =='7':
              	print(seven[i].replace('7', char), end=' ')
            	if clock[j] =='8':
              	print(eight[i].replace('8', char), end=' ')
            	if clock[j] =='9':
              	print(nine[i].replace('9', char), end=' ')
        	if hour_extra < 12:
          	print(a[i], end=' ')
          	print(m[i], end= '')
          	print()
        	else:
          	print(p[i], end=' ')
          	print(m[i], end= '')
          	print()
	#no thanks
	else:
    	for i in range(5):
      	for j in range(len(clock)):
          	if clock[j]==':':
              	print(colon[i], end=' ')
          	if clock[j] == '0':
              	if j != 0:
                  	print(zero[i], end=' ')
          	if clock[j] == '1':
            	print(one[i], end=' ')
          	if clock[j] == '2':
            	print(two[i], end=' ')
          	if clock[j] == '3':
            	print(three[i], end=' ')
          	if clock[j] =='4':
              	print(four[i], end=' ')
          	if clock[j] =='5':
              	print(five[i], end=' ')
          	if clock[j] =='6':
              	print(six[i], end=' ')
          	if clock[j] =='7':
            	print(seven[i], end=' ')
          	if clock[j] =='8':
            	print(eight[i], end=' ')
          	if clock[j] =='9':
            	print(nine[i], end=' ')

      	if hour_extra < 12:
        	print(a[i], end=' ')
        	print(m[i], end= '')
        	print()
      	else:
        	print(p[i], end=' ')
        	print(m[i], end= '')
        	print()
