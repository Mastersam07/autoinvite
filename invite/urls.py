"""autoinvite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from invite.views import HomePage, SuccessPage, output, ErrorPage

urlpatterns = [
    path('', HomePage, name='home'),
    path('success', SuccessPage.as_view(), name='success'),
    path('error', ErrorPage.as_view(), name='error'),
    path('output', output, name='output'),
    # path('add/', add_to_org(), name='invite'),
]
