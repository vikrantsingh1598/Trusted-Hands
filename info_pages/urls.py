from django.urls import path, include
from info_pages.views import *

app_name = 'info_pages'

urlpatterns = [
    path('about-us', AboutUsView.as_view(), name='about_us'),   #abouts us view
    path('privacy-policy', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('contact-us', ContactUsView.as_view(), name='contact_us'),
    path('terms-and-conditions', TermsAndConditionsView.as_view(), name='terms_n_conditions'),
]
