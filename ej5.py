import matplotlib.pyplot as plt
import matplotlib.image
import numpy as np
from skimage.color import rgb2gray
import skimage as ski
from scipy import linalg as lg
from turtle import Shape
#para ver las imagenes en escala de gris
plt.rcParams['image.cmap'] = 'gray'


def pgcd(a, b): #mcd pero en frances
    if a < b:
        a, b = b, a
    while b != 0:
        a ,b  = b, a % b
    return a

def dc(im): # devuelve los factores comunes de las dimenciones de la imagen
    a = im.shape
    a , b = a[0] , a[1]
    l = []
    mcd = pgcd(a,b)
    for i in range(1,mcd+1):
        if ((mcd % i )== 0):
            l.append(i)
    return l

def orden(M, b): #reordena los pixeles en el orden para minimizar distorciones
    # Calcular la cantidad de bloques que podemos crear en ambas dimensiones
    l, C = M.shape
    X = l // b
    Y = C // b
    # Crear una nueva imagen para almacenar los bloques reordenados
    Mt = np.array([[0.5]*b**2 for i in range(l*C//b**2)])
    # Iterar sobre cada bloque y reordenarlos en la nueva imagen
    for i in range(X):
        for j in range(Y):
            for k1 in range(b):
                for k2 in range(b):
                    Mt[i*Y+j,k1*b+k2] = M[i*b+k1,j*b+k2]
    return Mt


# b factor comun a l y C usado para comprimir
def reorden(Mt,b, l, C):#devuelve la imagen a su forma original para poder verla bien
    X = l // b
    Y = C // b
    M = np.array([[0.5]*C]*l)
    for i in range(X):
        for j in range(Y):
            for k1 in range(b):
                for k2 in range(b):
                    M[i*b+k1,j*b+k2] = Mt[i*Y+j,k1*b+k2]
    return M
# k numero de valores singulares usados
def CompresSVDkb(Im):
    print("los valores que puede elegir para b son:", dc(Im))
    b = int((input('ingrese b: ')))
    l , C = Im.shape
    M = orden(Im,b)
    U, S, V = lg.svd(Im, full_matrices=False)
   # imk = reorden(Mc,b,l,C)

    return U,S,V,b

I = plt.imread('quetzal.png')
I = ski.color.rgb2gray(I[:,:,:4])

#I = (I*255).astype(np.uint8)

U,S,V,k = CompresSVDkb(I)

x = [i for i in range(len(S))]
plt.plot(x,S)
plt.show()


Icom = U[0:10] @ np.diad(S)[0:10] @ V[:10]
