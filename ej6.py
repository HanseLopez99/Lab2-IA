import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
from scipy import linalg as lg
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
    U, S, V = lg.svd(M, full_matrices=False)
   # imk = reorden(Mc,b,l,C)

    return U,S,V,b,l,C




############### ejemplos de uso #########################
Imágenes = ["arbol.png",'quetzal.png','Cayala.JPG']

for dirIm in Imágenes:
    I = plt.imread(dirIm)
    if I.shape[-1] >= 3:
        I = I[:, :, :3]
    I = ski.color.rgb2gray(I[:,:,:])

    U, S, V, b, l, C = CompresSVDkb(I)

    x = np.arange(len(S))

    #
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, S / np.sum(S), marker='o', markersize=4, markevery=5)
    plt.title("Tamaño de los valores singulares")
    plt.xlabel("Índice de valores singulares")
    plt.ylabel("Valor normalizado")


    plt.subplot(1, 2, 2)
    plt.plot(x, np.cumsum(S) / np.sum(S), marker='o', markersize=4, markevery=5)
    plt.title("Cercanía con la imagen original")
    plt.xlabel("Número de valores singulares")
    plt.ylabel("Cercanía con la imágen original")

    plt.tight_layout()
    plt.show()

    k = int(input("Elija el número de valores singulares a usar: k = "))
    Icom = U[:, :k] @ np.diag(S[:k]) @ V[:k, :]

    Icom = reorden(Icom, b, l, C)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(I, cmap="gray")
    ax[0].set_title("Imagen Original")
    ax[1].imshow(Icom, cmap="gray")
    ax[1].set_title(f"Aproximación con k={k}")
    plt.show()
