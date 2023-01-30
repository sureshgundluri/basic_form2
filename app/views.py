from django.shortcuts import render

def html_form(request):
    if request.method=='POST':
        user=request.POST['user']
        password=request.POST['password']
        print(user)
        print(password)
    return render (request,'html_form.html')
