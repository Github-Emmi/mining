from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('logout/', LogoutView.as_view(), name="logout"),

    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('started', views.started, name='started'),
    path('faq', views.faq, name='faq'),
    path('affiliate', views.affiliate, name='affiliate'),
    path('contact', views.contact, name='contact'),
    path('sent/', views.sent, name='sent'),
    path('terms-and-conditions/', views.terms, name='terms'),
    

    # dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    path('settings', views.profileUpdate, name='profileUpdate'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('depositHistory', views.depositHistory, name='depositHistory'),
    path('earnings', views.earnings, name='earnings'),
    path('fundAccount', views.fundAccount, name='fundAccount'),
    path('investments', views.investments, name='investments'),
    path('purchasePlan', views.purchasePlan, name='purchasePlan'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]