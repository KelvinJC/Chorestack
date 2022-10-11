"""chorestack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bugstack.views import home, all_bugs, create_bug, search_all_bugs, all_dead_bugs, squash_bug, update_bug
from projects.views import add_project, all_projects, update_project, delete_project, search_projects, click_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('list_bugs/', all_bugs, name='list-bugs'),   
    path('bugs', create_bug, name='create-bug'),
    path('search_bugs/', search_all_bugs, name='search-bugs'),
    path('dead_bugs/', all_dead_bugs, name='list-dead-bugs'),
    #path('list_bugs/page<int:num>', views.all_bugs, name='after-squash-bug'),
    #path('squash_bug/', views.all_bugs, name='after-squash-bug'),
    path('squash_bug/<bug_id>', squash_bug, name='squash-bug'),
    path('update_bug/<bug_id>', update_bug, name='update-bug'),
    #path('search_dead_bugs/', views.search_dead_bugs, name='search-dead-bugs'),

    path('add_project', add_project, name='add-project'),
    path('list_projects/', all_projects, name='all-projects'),
    path('update_project/<project_id>', update_project, name='update-project'),
    path('click_delete/<project_id>', click_delete, name='clicked-delete'),
    path('delete_project/<project_id>', delete_project, name='delete-project'),

    path('search_projects/', search_projects, name='search-projects'),


]
