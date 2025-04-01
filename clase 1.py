ho = int(input("pon las horas trabajadas en la semana: "))
ss = int(input("salario por semana: "))

if ho == 40 and ss==100000:
    ss + 0
elif ho == 60 and ss==100000:
    ss + 50000
elif ho == 80 :
    ss + 100000
else:
    print ("no se puede calcular")

print (ss)
