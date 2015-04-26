def cent(number,main_dict):
	array, length = [],len(str(number))
	g1 = [i for i in [number//100 * 100, number%100] if i != 0]
	g2 = [(number//(10 ** i) % 10) * (10 ** i) for i in range(2, -1,-1)]
	g = g1 if g1[-1] in main_dict else g2
	for n,i in enumerate(g):
		if (n == 0 and length == 3) or (i not in main_dict):
			array.append(main_dict[int(str(i)[0])])
		array.append(main_dict[i] if i in main_dict else main_dict[10 ** (length - 1)])
	return main_dict[number] if number in main_dict.keys() else ' '.join(array)
def convert(number):
	main_dict = {0:"",1:"one",2:"two", 3: "three",4:"four", 5:"five", 6:"six", 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:"eleven",12:"twelve",13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand',1000000:'million',10 ** 9:'billion', 10 ** 12:'trillion',10**15:'quadrillion'}
	things = [(number//(10 ** i))%1000 for i in range(15, -3, -3)] #trillions, billions, millions, thousand, _blank_
	things = [(cent(things[i],main_dict) + " " + ['quadrillion','trillion','billion','million','thousand',''][i]).strip() for i in range(len(things)) if things[i] != 0]
	return ' '.join(things)
print(convert(420))
