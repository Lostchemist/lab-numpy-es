#1. Importa el paquete NUMPY bajo el nombre np.
import numpy as np



#2. Imprime la versión de NUMPY y la configuración.
print ("Version is: ", np.__version__)
print("configuration is: ",np.show_config())


#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

a = np.random.randint(0, 100, size=(2, 3, 5))
# Define the 3 dimensions
x = 2
y = 3
z = 5
# Using the np.empty function:
# Create an empty 3D numpy array with dimensions (x, y, z)
a1 = np.empty((x, y, z))

# Fill the array with random values between 0 and 1
a1 = np.random.rand(*a1.shape)
# 2. Using the np.zeros function:
# Create a 3D numpy array filled with zeros
a2 = np.zeros((x, y, z))

# Add random values between 0 and 1 to the array
a2 += np.random.rand(*a2.shape)

# 3. Using the np.random.random_sample function:
# Create a 3D numpy array and fill it with random values between 0 and 1
a3 = np.random.random_sample((x, y, z))

#4. Imprime a.

print(a)
print("Example 1: ",a1)
print ("Example 2: ",a2)
print("Example 3: ",a3)
#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

b =np.ones((5, 2, 3))

#6. Imprime b.

print(b)

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

print(b.shape)
print(a.shape)
print(a.shape==b.shape)

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

# "Answer: Para que la suma sea posible, las formas de los dos arrays deben ser compatibles.
# Esto significa que, para cada dimensión, las longitudes de las dimensiones deben ser iguales o una de
# ellas debe ser 1. En este caso, ninguna de las dimensiones de a y b cumple con esta condición, por lo que
# la suma no es posible."



#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

c = np.transpose(b, (1, 2, 0))
print(c.shape)

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

d = a + c
#Funcciona por que a y c tienen misma forma
print(d.shape)


#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

print("This is array a")
print(a)
print("This is array d")
print(d)
print("Answer: each element in array d is a sum of elements in a and d occupying the same position.")


#12. Multiplica a y c. Asigna el resultado a e.

e = a*c
if np.array_equal(a,e):
    print("Arrays a and e are the same ")
else:
    print("They are different")

#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

if np.array_equal(a,e):
    print("Arrays a and e are the same, because it multuplies each element of a by each element in c occupying the same position, everything by 1 in this case")
else:
    print("They are different")




#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

d_max = np.amax(d)
d_min = np.amin(d)
d_mean = np.median(d)

print("Max values in d are: ", d_max )
print("Min values in d are: ", d_min)
print("Mean values in d are: ", d_mean)




#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

f = np.empty((2, 3, 5))


"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100
print(f)
print("The shape of f is: ", f.shape)




"""
#17. Imprime d y f. ¿Tienes el f esperado?
Por ejemplo, si tu d es:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Tu f debería ser:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print("\n\n\nThe f array is: \n\n\n",f)
print("\n\n\nThe d array is: \n\n\n",d)



"""
#18. Pregunta de bonificación: en lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena 
("A", "B", "C", "D" y "E") para etiquetar los elementos del array? Esperas el resultado sea:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
De nuevo, no necesitas Numpy en esta pregunta.
"""
f2 = np.empty_like(d, dtype=str)
f2[(d > d_min) & (d < d_mean)] = "B"
f2[(d > d_mean) & (d < d_max)] = "D"
f2[d == d_mean] = "C"
f2[d == d_min] = "A"
f2[d == d_max] = "E"

print("\n\n\nThe f2 array is: \n\n\n",f2)
print("The shape of f2 is:", f.shape)