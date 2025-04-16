from django.shortcuts import render
from .models import Slide, Article, Counter, CompanyInfo
from ckeditor.fields import RichTextField
# from .models import HomeSection
from .models import HomeSection, Logo

def home(request):
    slides = Slide.objects.filter(is_active=True)
    counters = Counter.objects.all()
    company_info = CompanyInfo.objects.first()
    articles = Article.objects.all()[:3]

    context = {
        'slides': slides,
        'counters': counters,
        'company_info': company_info,
        'articles': articles,
        'section2': HomeSection.objects.filter(section_type='section2', is_active=True).first(),
        'section4': HomeSection.objects.filter(section_type='section4', is_active=True).first(),
        'section6': HomeSection.objects.filter(section_type='section6', is_active=True).first(),
        'site_logo': Logo.objects.filter(is_active=True).first()
    }
    return render(request, 'main/home.html', context)


def articles(request):
    articles_list = Article.objects.all()
    company_info = CompanyInfo.objects.first()

    context = {
        'articles': articles_list,
        'company_info': company_info,
    }
    return render(request, 'main/articles.html', context)


def about(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'main/about.html', {'company_info': company_info})


def contact(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'main/contact.html', {'company_info': company_info})


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'main/article_detail.html', {'article': article})


# from django.shortcuts import render
# from .models import HomeSection
#
# def home(request):
#     context = {
#         'section2': HomeSection.objects.filter(section_type='section2', is_active=True).first(),
#         'section4': HomeSection.objects.filter(section_type='section4', is_active=True).first(),
#     }
#     return render(request, 'home.html', context)



