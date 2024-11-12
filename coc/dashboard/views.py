from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from videos.models import Category


def accordion(request):
    template_name='dashboard/components-accordion.html'
    return render(request, template_name)


def components_alerts(request):
    template_name='dashboard/components-alerts.html'
    return render(request, template_name)







def colors(request):
    template_name='dashboard/utilities-color.html'
    return render(request, template_name)


def borders(request):
    template_name='dashboard/utilities-border.html'
    return render(request, template_name)


def animations(request):
    template_name='dashboard/utilities-animation.html'
    return render(request, template_name)


def all_alerts(request):
    template_name='dashboard/all_alerts'
    return render(request, template_name)


def components_cards(request):
    template_name='dashboard/components-card.html'
    return render(request, template_name)


def forms_layouts(request):
    template_name='dashboard/forms-layout.html'
    return render(request, template_name)

def icons(request):
    template_name='dashboard/bootstrap-icons.html'
    return render(request, template_name)


def forms_validation(request):
    template_name='dashboard/forms-validation.html'
    return render(request, template_name)


def bootstrap_icons(request):
    template_name='dashboard/.bootstrap-icons.html'
    return render(request, template_name)


def tables_basic(request):
    template_name='dashboard/tables-basic.html'
    return render(request, template_name)




def tables_accented(request):
    template_name='dashboard/tables-accented.html'
    return render(request, template_name)


def cards_stats(request):
    template_name='dashboard/cards-stats.html'
    return render(request, template_name)


def cards_tables(request):
    template_name='dashboard/cards-tables.html'
    return render(request, template_name)


def cards_timelines(request):
    template_name='dashboard/cards-timelines.html'
    return render(request, template_name)


def calendars_basic(request):
    template_name='dashboard/calendars-basic.html'
    return render(request, template_name)


def apex_charts(request):
    template_name='dashboard/apex-charts.html'
    return render(request, template_name)


def js_vecto_rmap_maps(request):
    template_name='dashboard/jsvectormap-maps.html'
    return render(request, template_name)


def pages_profile(request):
    template_name='dashboard/pages-profile.html'
    return render(request, template_name)


def pages_invoice(request):
    template_name='dashboard/pages-invoice.html'
    return render(request, template_name)


def pages_pricing(request):
    template_name='dashboard/pages-pricing.html'
    return render(request, template_name)


def pages_contact(request):
    template_name='dashboard/pages-contact.html'
    return render(request, template_name)


def pages_faqs(request):
    template_name='dashboard/pages-faqs.html'
    return render(request, template_name)


def pages_blank(request):
    template_name='dashboard/pages-blank.html'
    return render(request, template_name)


def auth_reset(request):
    template_name='dashboard/auth-reset.html'
    return render(request, template_name)


def other(request):
    template_name='dashboard/utilities-other.html'
    return render(request, template_name)


def blank(request):
    template_name = 'dashboard/blank.html'
    return render(request, template_name)


def messages(request):
    template_name ='dashboard/messages.html'
    return render(request, template_name)


def buttons(request):
    template_name='dashboard/buttons.html'
    return render(request, template_name)


def cards(request):
    template_name='dashboard/cards.html'
    return render(request, template_name)

def home(request):
    categories = Category.objects.prefetch_related('contents').all()  # Fetch all categories
    return render(request, 'dashboard/index.html', {'categories': categories})


def forgot_password(request):
    template_name = 'dashboard/forgot-password.html'
    return render(request, template_name)


def charts(request):
    template_name = 'dashboard/charts.html'
    return render(request, template_name)

def tables(request):
    template_name = 'dashboard/tables.html'
    return render(request, template_name)

def register(request):
    template_name = 'dashboard/auth-register.html'
    return render(request, template_name)


def index(request):
    template_name = 'dashboard/base_dashboard.html'
    return render(request, template_name)


def login_view(request):
    template_name = 'dashboard/auth-login.html'
    return render(request, template_name)


def utilities_animation(request):
    template_name = 'dashboard/utilities-animation.html'
    return render(request, template_name)


def utilities_border(request):
    template_name = 'dashboard/utilities-border.html'
    return render(request, template_name)


def utilities_color(request):
    template_name = 'dashboard/utilities-color.html'
    return render(request, template_name)


def utilities_other(request):
    template_name = 'dashboard/utilities-other.html'
    return render(request, template_name)


def error_404(request):
    template_name = 'dashboard/pages-error-404.html'
    return render(request, template_name)


