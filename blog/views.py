from django.shortcuts import render

projects_list = [
    {
        'id': 1,
        'title': 'Ecommerce Website',
        'description': 'fully functional ecommerce website',
    },
    {
        'id': 2,
        'title': 'Portfolio Website',
        'description': 'this was a project where i built my portfolio',
    },
    {
        'id': 3,
        'title': 'Social Network',
        'description': 'Awsome open source project I am still working on',
    }
]


def projects(request):
    context = {
        'projects': projects_list
    }

    return render(request, 'blog/projects.html', context)


def project(request, pk):
   project_obj = None
   for i in projects_list:
       if i['id'] == pk:
           project_obj = i
           break
   context = {
       'project': project_obj
   }
   return render(request, 'blog/project.html', context)