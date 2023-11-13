from django.shortcuts import render


def contact_info(request):
    return render(request, 'catalog/contact_info.html')


def home_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/home_page.html')
