from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm, MarksheetForm


# rendering the home page (transferring the data to the template)
def homePage(request): 
    data = {
        'title': 'Home Page',
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


def userForm(request):
    fn = UserForm()
    if request.method == 'POST':
        fn = UserForm(request.POST)
        if fn.is_valid():
            name = fn.cleaned_data['name']
            email = fn.cleaned_data['email']
            return redirect('formsuccess')
    return render(request, 'userform.html', {'title': 'User Form', 'form': fn})


def submitForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return redirect('formsuccess')

    return render(request, 'submitform.html', {'title': 'Submit Form'})


def formSuccess(request):
    return render(request, 'formsuccess.html', {'title': 'Form Success'})


def marksheet_form(request):
    form = MarksheetForm()
    result = None

    if request.method == 'POST':
        form = MarksheetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            marks = {
                'Math': data['math'],
                'Science': data['science'],
                'English': data['english'],
                'Computer': data['computer'],
            }

            total = sum(marks.values())
            percentage = round((total / 400) * 100, 2)

            if percentage >= 90:
                grade = 'A+'
            elif percentage >= 80:
                grade = 'A'
            elif percentage >= 70:
                grade = 'B'
            elif percentage >= 60:
                grade = 'C'
            elif percentage >= 50:
                grade = 'D'
            else:
                grade = 'F'

            result = {
                'student_name': data['student_name'],
                'roll_number': data['roll_number'],
                'marks': marks,
                'total_marks': total,
                'percentage': percentage,
                'grade': grade,
            }

    return render(request, 'marksheet.html', {
        'form': form,
        'result': result,
    })