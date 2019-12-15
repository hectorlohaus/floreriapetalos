from django.shortcuts import render, redirect
from .models import Flor,Ticket
from .clases import elemento
from django.contrib import messages
from .forms import FlorForm,CustomUserForm,UserCreationForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login, authenticate
# Create your views here.
def index(request):
    return render(request,'core/inicio.html')

def galeria(request):
    flores=Flor.objects.all()

    return render(request,'core/Productos.html',{
        'flores':flores
    })

def quienessomos(request):
    return render(request,'core/Quienes-Somos.html')

def contacto(request):
    return render(request,'core/Contacto.html')

def registro1(request):
    return render(request,'core/Registro.html')

def listar_flores(request):
    flores=Flor.objects.all()

    return render(request,'core/listar_flores.html',{
        'flores':flores
    }) 

@permission_required('floreria.add_flor')
def nuevopro(request):
    
    data= {
        'form':FlorForm()
    }
    if request.method=='POST':
        formulario=FlorForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Guardado correctamente"
        data['form']=formulario

    return render(request,'core/nuevopro.html', data)


def modificar_flor(request, nombre):

    flor=Flor.objects.get(nombre=nombre) 
   
    data={
        'form':FlorForm(instance=flor)
    }

    if request.method=='POST':
        formulario=FlorForm(data=request.POST,instance=flor , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Modificado correctamente"
            data['form']=FlorForm(instance=flor.objects.get(nombre=nombre))

    return render(request,'core/modificar_flor.html',data)

@login_required(login_url='/login/')
def eliminar_flor(request, nombre):
    
    flore = Flor.objects.get(nombre=nombre) 
    flore.delete()

    return redirect(to="LISTAR")

#@login_required(login_url='/login/')
#def eliminar_flor(request,nombre):
 #   flor=Flor.objects.get(nombre=nombre)
  #  mensaje=''
   # try:
    #    flor.delete()
     #   mensaje='Pelicula Eliminada'
    #except:
     #   mensaje='Problemas de Eliminacion Pelicula'

    #flores=Flor.objects.all()
    #return render(request,'core/galeria.html',{'florcitas':flores,'msg':mensaje})


def registro_usuario(request):
    data= {'form':CustomUserForm() }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='QUIENES')
    return render(request, 'registration/registro.html', data)



    
@login_required(login_url='/login/')
def carros(request):
    x=request.session["carritox"]
    suma=0
    for item in x:
        suma=suma+int(item["total"])           
    return render(request,'core/carro.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def grabar_carro(request):
    x=request.session["carritox"]    
    usuario=request.user.username
    suma=0 
    try:
        for item in x:        
            titulo=item["nombre"]
            precio=int(item["precio"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])        
            ticket=Ticket(
                usuario=usuario,
                titulo=titulo,
                precio=precio,
                cantidad=cantidad,
                total=total,
            )
            ticket.save()
            suma=suma+int(total)  
            print("reg grabado")                 
        mensaje="Grabado"
        request.session["carritox"] = []
    except:
        mensaje="error al grabar"            
    return render(request,'core/carro.html',{'x':x,'total':suma,'mensaje':mensaje})

@login_required(login_url='/login/')
def carro_compras(request,nombre):
    f=Flor.objects.get(nombre=nombre)
    x=request.session["carritox"]
    el=elemento(1,f.nombre,f.valor,1)
    sw=0
    suma=0
    clon=[]
    for item in x:       
        cantidad=item["cantidad"]
        if item["nombre"]==f.nombre:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(el.toString())
    x=clon    
    request.session["carritox"]=x
    flores=Flor.objects.all()    
    return render(request,'core/galeria.html',{'flores':flores,'total':suma})

@login_required(login_url='/login/')
def carro_compras_mas(request,nombre):
    f=Flor.objects.get(nombre=nombre)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.nombre:
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carro.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def carro_compras_menos(request,nombre):
    f=Flor.objects.get(nombre=nombre)
    x=request.session["carritox"]
    clon=[]
    suma=0
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.nombre:
            cantidad=int(cantidad)-1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total)
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]    
    return render(request,'core/carro.html',{'x':x,'total':suma})
