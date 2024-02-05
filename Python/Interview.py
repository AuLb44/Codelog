def response( input ) :
	# Enter your code here
	response = []
	for i in range(1, input + 1):
		if (i % 3 == 0) and (i % 5 == 0):
			response.append('FizzBuzz')
		elif i % 3 == 0:
			response.append('Fizz')
		elif i % 5 == 0:
			response.append('Buzz')
		else:
			response.append(i)
	return response

def version_compare( version1, version2 ):
    Ver1 = version1.replace('.','')
    Ver2 = version2.replace('.','')
    Diff = len(Ver2) - len(Ver1)
    if Diff > 0:
     for i in range(Diff):
            Ver1 = Ver1+'0'
    print(Ver1)
    print(Ver2)
                         
	 	
print(version_compare("2","2.0"))