from django.shortcuts import render
from cooking.models import * 
# Create your views here.

def display(request):
    return render(request, 'base.html')
def home(request):
    items = FoodItem.objects.all()
    list = ItemList.objects.all()
    return render(request, 'home.html',{'items': items,'list': list})

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname') 
        lname=request.POST.get('lname') 
        num= request.POST.get('number') 
        email =request.POST.get('email') 
        pws=request.POST.get('pass') 
        cpws=request.POST.get('cpass') 
    
    data=clientUser(First_Name=fname, Last_Name=lname, Number=num, Email=email, Password=pws)
    data.save()

    return render(request, 'demo.html')

def about(request):
    data = aboutTable.objects.all()
    return render(request, 'about.html',{'data':data})

def menu(request):
    items = FoodItem.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items,'list': list})
   

def book(request):
    if request.method=='POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date= request.POST.get('booking_date')
        
        if name != '' and len(phone_number) == 10 and email != '' and total_person != 0 and booking_date != '':
            data = BookTable(Name=name, Phone_number=phone_number,
                             Email=email,Total_person=total_person,
                             Booking_date=booking_date)
            data.save()
    return render(request, 'book.html')

    

def demo(request):
    return render(request, 'demo.html')