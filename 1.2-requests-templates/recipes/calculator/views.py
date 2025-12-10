from django.shortcuts import render
from django.http import HttpResponse

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
}

def recipe_view(request, dish):
    recipe_data = DATA.get(dish)

    if not recipe_data:
        return HttpResponse("Рецепт не найден", status=404)

    servings = request.GET.get('servings')
    if servings:
        try:
            servings = int(servings)
            if servings <= 0:
                return HttpResponse("Количество порций должно быть положительным числом", status=400)
        except ValueError:
            return HttpResponse("Параметр servings должен быть числом", status=400)

        new_recipe = {}
        for ingredient, amount in recipe_data.items():
            new_recipe[ingredient] = amount * servings
        context = {'recipe': new_recipe}
    else:
        context = {'recipe': recipe_data}

    return render(request, 'calculator/index.html', context)