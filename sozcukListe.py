"""
Bir yazı okuyunuz. 

Yazı boşluk karakterleriyle ayrılmış sözcüklerden oluşmuş olsun. 

Aynı sözcükleri atarak sözcükleri bir listeye yerleştiriniz. 

Örneğin girilen yazı şöyle olsun:

bugün hava evet bugün çok hava güzel güzel

Sonuç olarak şöyle bir liste elde edilmeli:

['bugün', 'hava', 'evet', 'çok', 'güzel']

Elde edilen listedeki sözcüklerin yazıdaki sözcük sırasında olması gerekmektedir. 
 


"""
# s = print('Bir yazı giriniz:')

s = 'bugün hava evet bugün çok hava güzel güzel'

result = []

for word in s.split():
    if word not in result:
        result.append(word)

print(result)
