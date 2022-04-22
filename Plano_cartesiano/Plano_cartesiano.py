"""Programa para ubicar una coordenada (x, y) en un plano cartesiano, segun su cuadrante"""


#Input
x = int(input("Digite el valor de la coordenada x: "))
y = int(input("Digite el valor de la coordenada y: "))
xy= (x,y)

#Processing
if ((x>0) & (y>0)):
    msj = "La coordenada:" + str(xy) + " Se encuentra en el cuadrante 1"
if ((x<0) & (y<0)):
    msj = "La coordenada:" + str(xy) + " Se encuentra en el cuadrante 3"
if ((x>0 & y<0)):
    msj = "La coordenada:" + str(xy) + " Se encuentra en el cuadrante 4"
if ((x<0) & (y>0)):
    msj = "La coordenada:" + str(xy) + " Se encuentra en el cuadrante 2"
if ((x==0) & (y==0)):
    msj = "La coordenada:" + str(xy) + " Se encuentra en el origen"
if ((x==0) & (y!=0)):
    msj = "La coordenada:" + str(xy) + " Se encuentra sobre el eje y"
if ((x!=0) & (y==0)):
    msj = "La coordenada:" + str(xy) + " Se encuentra sobre el eje x"


#Output
print(msj)