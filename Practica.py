import os
import sys
import re
import copy
import webbrowser
from tkinter import *
from tkinter import filedialog
raiz=" "
arch=" "
todas=list()
todasNombres=list()
nombreOrdenados=list()
ordenados=list()
nombresBuscados=list()
posiciones=list()
numerosBuscar=list()
pintarOrdenador=list()
pintarBuscador=list()
imprimir=list()
imprimirC=list()


def main():
  print("LENGUAJES DE PROGRAMACION")
  print("NOMBRE: ROXANA MADAHÍ CARÍAS PAREDES, CARNÉ: 201800672")
  menu()

def menu():
    print("SELECCIONE UNA OPCION")
    print("1. Cargar archivo de entrada")
    print("2. Desplegar listas ordenadas")
    print("3. Desplegar búsquedas")
    print("4. Desplegar todas")
    print("5. Desplegar todas a archivo")
    print("6. Salir")
    numOpcion=input()
    numeroOpcion(numOpcion)

def numeroOpcion(numOpcion):
   if(numOpcion=="1"):
     cargarArchivo()
   elif(numOpcion=="2"):
      listasOrdenadas()
      pintarO()
      menu()
   elif(numOpcion=="3"):
       listasBusqueda()
       pintarB()
       menu()
   elif(numOpcion=="4"):
       despTodas()
       pintarImprimir()
       menu()
   elif(numOpcion=="5"): 
       despTodas()
       generarHtml()
       menu()
   elif(numOpcion=="6"):
       print("usted ha salido del programa")
       sys.exit()
   else:
       print("No es valido el numero de la opcion, introduzcalo de nuevo") 
       menu()    

def despTodas():
  global imprimir  
  imprimir=list()
  global imprimirC
  imprimirC=list()  
  listasBusqueda()
  listasOrdenadas()  
  ordenar=""
  buscar=""   
  z=0
  for  t in todasNombres:#solo el nombre de toda la fila
      y=todas[z]#toda la fila
      y=y.replace(" ","")#quitando los espacios de toda la fila
      t=t.strip()#quitando los espacios de solo el nombre 
      ordenar=""
      buscar=""
      if z<len(todasNombres):  
        for u in pintarOrdenador:# verificando si en los nombres ordenados estan
            b=re.findall(t,u)
           # print("la t:"+t+"en u: "+u)
            #print("la b es: "+ str(len(b)))
            if len(b)!=0:
                ordenar=u
        for p in pintarBuscador:
            #print("la t:"+t+"en p: "+p)
            d=re.findall(t,p)
            #print("la d es: "+ str(len(d)))
            if len(d)!=0:
                buscar=p   
        x=re.findall("ORDENAR,",y)
        n="________________________________" 
        if ordenar!="" and buscar!="" and len(x)!=0:
            imprimir.append(buscar)
            imprimir.append(ordenar)
            imprimirC.append(buscar)
            imprimirC.append(ordenar)
            imprimirC.append(n)
        elif ordenar!="" and buscar!="" and len(x)==0:    
            imprimir.append(ordenar)
            imprimir.append(buscar)
            imprimirC.append(ordenar)
            imprimirC.append(buscar)
            imprimirC.append(n)
        elif ordenar!="" and buscar=="":
            imprimir.append(ordenar)
            imprimirC.append(ordenar)
            imprimirC.append(n)
        elif ordenar=="" and buscar!="": 
            imprimir.append(buscar)
            imprimirC.append(buscar)
            imprimirC.append(n)
      z=z+1
      

def pintarImprimir():
    print("")
    print("__________________________________TODAS LAS LISTAS*****")
    for j in imprimirC:
        print(j)
    print("")    

def listasBusqueda():
    global pintarBuscador  
    pintarBuscador=list()
    a=""
    z=0
    t=0
    s=0
    for l in nombresBuscados:
      a=""    
      a=a+l+": "
      c=posiciones[z]
      f=numerosBuscar[z]
      t=0
      for r in f:
        t=t+1   
        if len(f)==t: 
         a=a+str(r)
        else:
         a=a+str(r)+","
      a=a+" BUSQUEDA DE POSICIONES= "   
      s=0
      if len(c)!=0 and c[0]!=0:
        for u in c:
          s=s+1     
          if len(c)==s:
            a=a+str(u)
          else: 
            a=a+str(u)+","   
      elif len(c)!=0 and c[0]==0:
          a=a+" NO ENCONTRADO"
      pintarBuscador.append(a)  
      z=z+1         
       
def pintarB():
    print("")
    for i in pintarBuscador:
        print(i)
    print("")    

def listasOrdenadas():
    global pintarOrdenador  
    pintarOrdenador=list()
    a=""
    b=""
    z=0
    u=0
    for l in ordenados:
        if u<len(ordenados):
            a=""
            a=nombreOrdenados[u]
            a=a+": ORDENADOS= "
            z=0
            for k in l:
                z=z+1
                if z==len(l):
                 a=a+str(k)
                else:
                 a=a+str(k)+","
        u=u+1  
        pintarOrdenador.append(a)   
        

def pintarO():
    print("")
    for i in pintarOrdenador:
        print(i)
    print("")
       
    
def leerArchivo():
   y= open(arch, "r")
   lines = y.readlines()
   for linea in lines:
    todas.append(linea) #se guarda toda la lista 
   print("*****¡ARCHIVO CARGADO!*******") 
   clasificar()
   menu()
   
def clasificar():
   for la in todas:
    la = la.replace(" ","")
    li=la
    orde=re.findall("ORDENAR",li)
    bus=re.findall("BUSCAR",li)
    #SACANDO LOS NUMEROS
    li=re.sub("ORDENAR,","",li)
    li=re.sub("ORDENAR","",li)
    li=re.sub(",ORDENAR","",li)
    patron="[a-zA-Z]+[0-9]*[=]"
    a=re.sub(patron,"",li) 
    patro="BUSCAR[0-9]+[,0-9]*"
    p=re.sub(patro,"",a)
    p=p.strip()
    numerosA=re.split(",",p)
    nu=copy.deepcopy(numerosA)
    #SACANDO EL NOMBRE DE LA LISTA
    le=la
    le=re.sub("ORDENAR,","",le)
    le=re.sub("ORDENAR","",le)
    le=re.sub(",ORDENAR","",le)
    patro="BUSCAR[0-9]+[,]*[0-9]*"
    p=re.sub(patro,"",le)
    patron2="[=][0-9]+[,0-9]*"
    r=re.sub(patron2,"",p)
    y=re.sub("[,]","",r)
    y=y.strip()
    todasNombres.append(y)
    #REALIZANDO OPERACIONES
    if len(bus)>0:
        lo=la
        lo=re.sub("ORDENAR,","",lo)
        lo=re.sub("ORDENAR","",lo)
        lo=re.sub(",ORDENAR","",lo)
        patron="[a-zA-Z]+[0-9]*[=][0-9]+[,0-9]*"
        lo=re.sub(patron,"",lo)      
        lo=re.sub("BUSCAR","",lo)
        lo=re.sub(",","",lo) 
        buscarNumero(lo,numerosA)
        nombresBuscados.append(y)
    if len(orde) > 0:
      ordena(nu)   
      nombreOrdenados.append(y)  
   menu()
      

def buscarNumero(lo,numeros):
    a=int(lo)
    j=1
    pos=list()
    numerosBuscar.append(numeros)
    y=0
    for i in numeros:
        if int(i)==a:
            pos.append(j)
            y=y+1
        j=j+1   
    if y!=0:       
      posiciones.append(pos)    
    else:
      pos.append(0)  
      posiciones.append(pos)     
    

def ordena(numerosA):
    #print("NIM:"+ str(numerosA))
    numeros=numerosA
    aux=0
    i=0
    j=0
    b=len(numeros)
    for num in numeros:
      if j<b:  
       i=0   
       for nu in numeros:
          if i<(b-1):  
           if int(numeros[i])>int(numeros[i+1]):
               aux=int(numeros[i])
               numeros[i]=int(numeros[i+1])
               numeros[i+1]=aux
           i=i+1
      j=j+1 
    #print("LOS O :"+str(numeros))   
    ordenados.append(numeros)


def cargarArchivo():
    global raiz
    raiz=Tk() 
    global arch 
    arch=filedialog.askopenfilename(title="Seleccione Archivo")
    raiz.withdraw()
    leerArchivo()
    raiz.mainloop()
def ejmplo(): 
    html=open("Reporte.txt",'w')   
 
def generarHtml():
    mi_ruta = os.path.abspath(os.path.dirname(__file__))
    k = 1
    #print("mi ruta: " +mi_ruta)
    html=open("Reporte.html","w")
    html.write('<!DOCTYPE html> \n')
    html.write('<html lang="en"> \n')
    html.write('<html>\n')
    html.write('<head>\n')
    html.write('	<title>\n')
    html.write('	   REPORTE\n')
    html.write('	</title>\n')
    html.write('	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">\n')
    html.write('    <script type="text/javascript" src="js/bootstrap.min.js"></script>\n')
    html.write('    <script type="text/javascript" src="js/jquery-migrate-1.4.1.min.js"></script>\n')
    html.write('    <meta charset="utf-8">\n')
    html.write('</head>\n')
    html.write('<body>\n')
    html.write('<center>\n')
    html.write('     <h1 class="bg-primary text-white">\n')
    html.write('         VISTA DE LISTAS\n')
    html.write('     </h1>\n')
    html.write('</center>\n')
    html.write('<table class="table table-striped">')
    html.write('  <thead>')
    html.write('    <tr>')
    html.write('      <th scope="col">#</th>')
    html.write('      <th scope="col"  href="#" class="text-info" >LISTAS</th>')
    html.write('    </tr>')
    html.write('  </thead>')
    html.write('  <tbody>')
    for j in imprimir:
        html.write('    <tr>')
        html.write('      <th scope="row">'+str(k)+'</th>')
        html.write('      <td href="#" class="text-danger">'+j+'</td>')
        html.write('    </tr>')
        k=k+1
    html.write('  </tbody>')
    html.write('</table>')
    html.write('</body>\n')
    html.write('</html>\n')
    html.close
    rut=os.path.join(mi_ruta,"Reporte.html")
    #print("la rut: "+ rut)
    webbrowser.open(rut)



main()    