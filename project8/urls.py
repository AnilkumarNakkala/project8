"""
URL configuration for project8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from modelapp.views import HomeView,InsertInput,InsertViews,DisplayView,DeleteInputView,DeleteView,UpdateInputView,UpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modelapp/',HomeView.as_view()),
    path('modelapp/insertinput/',InsertInput.as_view()),
    path('modelapp/insertinput/insert',InsertViews.as_view()),
    path('modelapp/display/',DisplayView.as_view()),
    path('modelapp/deleteinput/',DeleteInputView.as_view()),
    path('modelapp/deleteinput/delete/',DeleteView.as_view()),
    path('modelapp/updateinput/',UpdateInputView.as_view()),
    path('modelapp/updateinput/update/',UpdateView.as_view()),
]
