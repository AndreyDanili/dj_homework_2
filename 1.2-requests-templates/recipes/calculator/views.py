from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def handler(request, recipe):
    servings = request.GET.get('servings')
    context = {
        'recipe': DATA[recipe].copy(),
    }
    if servings:
        for ingredient, quantity in context['recipe'].items():
            context['recipe'][ingredient] = quantity * int(servings)
    return context


def recipes(request, item):
    context = handler(request, item)
    return render(request, 'calculator/index.html', context)


# def pasta(request):
#     context = handler(request, 'pasta')
#     return render(request, 'calculator/index.html', context)
#
#
# def buter(request):
#     context = handler(request, 'buter')
#     return render(request, 'calculator/index.html', context)
