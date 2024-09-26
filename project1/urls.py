"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from project1 import views 

urlpatterns = [
    path('', views.homePage),
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutUs),
    path('test-page/', views.testPage),
    path('archetype', views.archetype),

#dynamic routing/url: where we can give details of different subpages from a page using  single page eg. we don't have different page for each of the thousands of products on shopping websit, instesad we follow dynamic url

#it can take three types of values, int, string and slug(this-is-an-example-of-slug)

    path('archetype/<int:archetypeId>', views.archetypeDetails),    #only if we know the type of data that will be coming our way, otherwise just put 'archetype/<archetypeId>'

]
