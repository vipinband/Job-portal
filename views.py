from django.shortcuts import render

from django.shortcuts import render

from jp.models import User, City, State, Jobs, UserProfile
from django.views.generic import UpdateView


def showHome(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})



#def openUserPage(request):
 #   type=request.GET.get("type")
#    return render(request,"user.html",{"type":type})

def openUserPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})


def showJobs(request):
    type=request.GET.get("type")
    jobres=Jobs.objects.all()
    print(jobres)
    return render(request,"index.html",{'type':type,'res':jobres})


def openNewRegister(request):
    type = request.GET.get("type")
    res = State.objects.values('name')
    states = ["State"]
    for x in res:
        states.append(x["name"])

    return render(request, "index.html", {"type": type,"states":states})




def userRegister(request):
    fname=request.POST.get("user_fname")
    lname=request.POST.get("user_lname")
    ustate=request.POST.get("user_state")
    ucity=request.POST.get("user_city")
    uemail=request.POST.get("user_email")
    upassword=request.POST.get("user_paswword")
    udor=request.POST.get("user_dor")
    res=City.objects.values("city_id").filter(city_name=ucity)  #getting city_id through city_name
    city_id=0
    for x in res:
        city_id=x["city_id"]  #[city_id:city_name] ,x["city_id]--getting city_id of city_name
        print('city_id')

    usr=User(first_name=fname,last_name=lname,city_name=City.objects.get(city_id=city_id),emailid=uemail,password=upassword,date=udor)
    usr.save()
    #type=request.GET.get("type")
    return render(request,"index.html",{"message":"user registered successfully","type":'h_user','res':res})



def getCityFromState(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('id').filter(name=sel_state)
    id = 0
    for x in res:
        id = x["id"]
    res1 = City.objects.values('city_name').filter(state_name=id)
    city_names = ["City"]
    if not res1:
        city_names = ["No City Available"]
    else:
        for x in res1:
            city_names.append(x['city_name'])

    res2 = State.objects.values('name')
    states = ["State"]
    for x in res2:
        states.append(x["name"])
        return render(request, "index.html",{"type": 'h_NewRegister', "city_names": city_names, "states": sel_state, "key": "one"})


def loginUser(request):
    global name,email
    username=request.POST.get("uname")
    password=request.POST.get("upass")

    res=User.objects.filter(emailid=username,password=password)
    print(res)
    if not res:
        type = "h_user"
        return render(request,"index.html",{"type":type,"message":"user not valid"})
    else:
        type = "u_home"
        for x in res:
            name=x.first_name
            email=x.emailid
            print("-----",name,email)
       #  #res=User.objects.all()
       # # for x in res:
         #   name=x["name"]
         #   email=x["emailid"]
        return render(request,"userHome.html",{"type":type,"name":name,"email":email})
 #       print("invalid details")
   # else:
        #type = 'h_user'
    #    res=User.objects.all()
     #   return render(request,"index.html",{"type":type,"details":res,"message":"logged in successfully"})


def openUserHome(request):
    type=request.GET.get("type")
    name=request.GET.get("name")
    email=request.GET.get("email")
    return render(request,"userHome.html",{"type":type,'name':name,'email':email})




def openAbout(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})


def showUserHome(request):
    type=request.GET.get("type")
    return render(request,"userHome.html",{"type":type})





def getCityFromState1(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('id').filter(name=sel_state)
    id = 0
    for x in res:
        id = x["id"]
    res1 = City.objects.values('city_name').filter(state_name=id)
    city_names = ["City"]
    if not res1:
        city_names = ["No City Available"]
    else:
        for x in res1:
            city_names.append(x['city_name'])

    res2 = State.objects.values('name')
    states = ["State"]
    for x in res2:
        states.append(x["name"])
        return render(request,"userHome.html",
                      {"type": 'u_home', "city_names": city_names, "states": sel_state, "key": "one"})


def update_user(request):
    type=request.GET.get("type")
   # name=request.GET.get("name")
    email=request.GET.get("email")
    print(email)
    res = State.objects.values('name')

    states = ["State"]
    for x in res:
        states.append(x["name"])
       # email1=User.objects.get(emailid=email)
        return render(request,"userHome.html",{'type':type,'email':email,'states':states,})


def userUpdate(request):
    firstname=request.POST.get("t1")
    lastname=request.POST.get("t2")
    city=request.POST.get("user_city")
    email=request.POST.get("t3")
    password=request.POST.get("t4")
    res = City.objects.values("city_id").filter(city_name=city)  # getting city_id through city_name
    city_id = 0
    for x in res:
        city_id = x["city_id"]  # [city_id:city_name] ,x["city_id]--getting city_id of city_name
        print('city_id')
        update= User(first_name=firstname, last_name=lastname, city_name=City.objects.get(city_id=city_id), emailid=email,
                   password=password)
        update.save()

        return render(request,"userHome.html",{'type':'u_update','name':firstname,'email':email,'message':'details are updated'})




def viewJobs(request):
    type=request.GET.get("type")
    name=request.GET.get("name")
    email=request.GET.get("email")
    result=Jobs.objects.all()
    print(result)
    print(email)
    print(name)
    return render(request,"userHome.html",{"type":type,"name":name,"email":email,"result":result})


def myProfile(request):
    type=request.GET.get("type")
    nametype=request.GET.get("name")
    emailtype=request.GET.get("email")
    name = request.POST.get("name")
    cno = request.POST.get("cno")
    email = request.POST.get("useremail")
    skills = request.POST.get("userskills")
    desig = request.POST.get("designation")
    exp = request.POST.get("experiance")
    cmp_name = request.POST.get("comp_name")
    profile = UserProfile(my_name=name, contact_no=cno, my_email=email, myskills=skills, designation=desig,
                          experiance=exp, company=cmp_name)
    profile.save()
    res2=User.objects.all()
    print(res2)
    return render(request,"userHome.html",{'type':'u_profile','email':emailtype,'name':nametype,'result':res2})


