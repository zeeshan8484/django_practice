from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm


# rendering the home page (transferring the data to the template)
def homePage(request): 
    data = {
        'title': 'Home Page',
        # 'content': 'Welcome to the home page'
        'clist': ['Python', 'Django', 'JavaScript', 'React', 'Node.js'],
        'student_list': [
            {'name': 'John', 'age': 20},
            {'name': 'Jane', 'age': 22},
            {'name': 'Mike', 'age': 21},
        ],
        'number_list': [1, 2, 3, 4, 5],
        'table_data': [
            {'id': 1, 'name': 'John', 'age': 20},
            {'id': 2, 'name': 'Jane', 'age': 22},
            {'id': 3, 'name': 'Mike', 'age': 21},
        ]
    }
    return render(request, 'index.html', data)


def aboutUS(request):
    return HttpResponse("welcome to the page")

def course(request):
    return HttpResponse("welcome to the course")

def courseDetails(request, courseid):
    return HttpResponse(f"welcome to the course {courseid}")


# using get, post methods to get the data from the form and display it on the same page
def userForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # you can save data here before redirecting
        return redirect('formsuccess')

    return render(request, 'userform.html', {'title': 'User Form'})


def submitForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # you can save data here before redirecting
        return redirect('formsuccess')

    return render(request, 'submitform.html', {'title': 'Submit Form'})


def formSuccess(request):
    return render(request, 'formsuccess.html', {'title': 'Form Success'})

def userForm(request):
    fn = UserForm()
    if request.method == 'POST':
        fn = UserForm(request.POST)
        if fn.is_valid():
            name = fn.cleaned_data['name']
            email = fn.cleaned_data['email']
            # you can save data here before redirecting
            return redirect('formsuccess')
    return render(request, 'userform.html', {'title': 'User Form', 'form': fn})