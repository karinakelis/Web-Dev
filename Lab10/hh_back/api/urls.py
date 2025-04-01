from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailView,
    VacancyListCreateView,
    VacancyDetailView,
  
    company_vacancies,
    top_ten_vacancies
)

urlpatterns = [
    #class-based
    path('companies/', CompanyListCreateView.as_view(), name='companies-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('vacancies/', VacancyListCreateView.as_view(), name='vacancies-list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    
    #function-based
    path('companies/<int:pk>/vacancies/', company_vacancies, name='company-vacancies'),
    path('vacancies/top_ten/', top_ten_vacancies, name='top-ten-vacancies'),
]