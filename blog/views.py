from django.shortcuts import render


def projects(request):
    projectsList = [
        {
            'id': '1',
            'title': 'Ecommerce Website',
            'description': 'fully functional ecommerce website',
        },
        {
            'id': '2',
            'title': 'Portfolio Website',
            'description': 'this was a project where i built my portfolio',
        },
        {
            'id': '3',
            'title': 'Social Network',
            'description': 'Awsome open source project I am still working on',
        }
    ]

    context = {
        'projects': projectsList
    }

    return render(request, 'blog/projects.html', context)


def project(request):
    pass
