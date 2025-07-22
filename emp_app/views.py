from django.shortcuts import render,HttpResponse
from.models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request,"1_index.html")

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
  
    return render(request,"2_all_emp.html",context)

def add_emp(request):
    if request.method=="POST":
     First_name=request.POST['First_name']
     last_name=request.POST['last_name']
     salary=int(request.POST['salary'])
     bonus=int(request.POST['bonus'])
     phone=int(request.POST['phone'])
     dept=int(request.POST['dept'])
     role=int(request.POST['role'])
     
     new_emp=Employee(First_name=First_name, last_name=last_name, salary=salary,bonus=bonus,phone=phone, dept_id=dept,role_id=role,hire_date=datetime.now())
     new_emp.save()
     return HttpResponse("Employee Added SuccessFully")
    elif request.method=="GET":
     return render(request,"3_add_emp.html")
    else:
        return HttpResponse("An Exception Occured! ")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Remove SuccessFully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")    
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"4_remove_emp.html",context)

def filter_emp(request):
   
    if request.method == "POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        
        if name: #i = case insensitive (chhoti ya badi letters ka farak nahi karega)
                 # contains = string ke andar match hona chahiye
            emps=emps.filter(Q(first_name__icontains=name) | Q (last_name__icontains=name))
            
        if dept:
            emps=emps.filter(dept__name_=dept)
        
        if role:
            emps=emps.filter(role__name_=role)
            
        context={
            "emps":emps
        }       
        
        return render(request,'2_all_emp.html',context)
    elif request.method == "GET":
        return render(request,'5_filter_emp.html')
    else:
        return HttpResponse("An Exception Occured") 


#  Jab Q ka use karte hain?
# Jab aapko multiple conditions ek query me apply karni hoti hai — especially OR conditions, tab Q object ka use hota hai

