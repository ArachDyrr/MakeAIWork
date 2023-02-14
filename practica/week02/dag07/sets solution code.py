# Oplossing opgave 1
fibonacciList = list(set(fibonacciList))
fibonacciList.sort()
print (fibonacciList)

# Oplossing opgave 2
benStr = str(list(benelux)[0])[:2]+str(list(benelux)[2])[:2]+str(list(benelux)[1])[:3]
print (benStr)

benList = [str(list(benelux)[0])[:2],str(list(benelux)[2])[:2],str(list(benelux)[1])[:2]]
print (benList)
