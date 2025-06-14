dictionary = {'alpha': 'beta', 'gamma': 'alpha', 'beta': 'gamma'}
value = dictionary['gamma']

for key in range(len(dictionary)):
    value = dictionary[value]

print(value)

values = [i for i in range(-1, -3, -1)]


def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


#print(fun(0, 3))
#i = 0
#while i < i + 2 :
 #   i += 1
  #  print("*")
#else:
 #   print("*")
my_tuple = (10, 20, 30, 40, 50)
my_tuple = my_tuple[-3:-1]
my_tuple = my_tuple[-1]
print(my_tuple)

my_dict = {"apple": 1, "banana": 2, "cherry": 3}


dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")
 
print("\n")
def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

print("\n")
matrix = [[x for x in range(3)] for y in range(3)]

count = 0
for row in matrix:
    for element in row:
        if element % 2 != 0:
            count += 1
print(count)

print("\n")
try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")








