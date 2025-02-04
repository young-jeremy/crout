from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('forms_validation/', views.forms_validation,name='forms_validation'),
    path('forms_layouts/', views.forms_layouts,name='forms_layouts'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('tables_accented/', views.tables_accented,name='table_accented'),
    path('colors/', views.utilities_color, name='colors'),
    path('borders/', views.borders, name='borders'),
    path('animations/', views.animations, name='animations'),
    path('other/', views.other, name='other'),
    path('404/', views.error_404, name='404'),
    path('blank/', views.blank, name='blank'),
    path('messages/', views.messages, name='messages'),
    path('components_buttons/', views.buttons, name='components_buttons'),
    path('cards/', views.cards, name='cards'),
    path('all_alerts/', views.all_alerts, name='all_alerts'),
    path('accordion/', views.accordion,name='accordion'),
    path('components_alerts/', views.components_alerts,name='components_alerts'),
    path('components_cards/', views.components_cards,name='components_cards'),
    path('cards_stats/', views.cards_stats,name='cards_stats'),
    path('cards_tables/', views.cards_tables,name='cards_tables'),
    path('cards_timelines/', views.cards_timelines,name='cards_timelines'),
    path('calendars_basic/', views.calendars_basic,name='calendars_basic'),
    path('apex_charts/', views.apex_charts,name='apex_charts'),
    path('js_vecto_rmap_maps/', views.js_vecto_rmap_maps,name='js_vecto_rmap_maps'),
    path('accounts_profile/', views.pages_profile,name='accounts_profile'),
    path('pages_invoice/', views.pages_invoice,name='pages_invoice'),
    path('pages_pricing/', views.pages_pricing,name='pages_pricing'),
    path('pages_contact/', views.pages_contact,name='pages_contact'),
    path('pages_faqs/', views.pages_faqs,name='pages_faqs'),
    path('pages_blank/', views.pages_blank,name='pages_blank'),
    path('auth_reset/', views.auth_reset,name='auth_reset'),
    path('icons/', views.icons,name='icons'),
    path('contact/success/', views.success_view, name='contact_success'),  # Success page

]