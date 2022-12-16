from django.shortcuts import render
from django.core.paginator import Paginator
from .models import CountryModel, LanguagesModel

alphabet = {chr(i): (i - 65) for i in range(65, 91)}


def index(request):
    all_countries = CountryModel.objects.all()
    contex = {
        "all_countries": all_countries,
    }
    return render(request, 'MainApp/index.html', contex)


def countries_list(request):
    data = CountryModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contex = {'page_obj': page_obj, 'data': data, 'alphabet': alphabet}
    return render(request, 'MainApp/countries_list.html', contex)


def countries_detail(request, country_id):
    country = CountryModel.objects.filter(id=country_id)[0]
    languages = country.languages.all()
    contex = {
        "country": country,
        "languages": languages,
    }
    return render(request, 'MainApp/countries_detail.html', contex)


def alphabet_search(request, alphabet_id):
    letter = ""
    for key, item in alphabet.items():
        if item == alphabet_id:
            letter = key
            break

    search = CountryModel.objects.filter(country__istartswith=letter)
    contex = {
        "search": search,
        "alphabet": alphabet,
    }

    return render(request, 'MainApp/alphabet_search.html', contex)


def languages(request):
    languages = LanguagesModel.objects.all()

    contex = {
        "languages": languages,
    }

    return render(request, 'MainApp/languages.html', contex)


def languages_country(request, languages_id):
    languages = LanguagesModel.objects.filter(id=languages_id)
    countries = CountryModel.objects.filter(languages=languages[0])

    contex = {
        "countries": countries,
    }

    return render(request, 'MainApp/languages_country.html', contex)