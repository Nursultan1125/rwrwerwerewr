from product.models import Category


def getting_category_info(request):
    categorys = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in categorys]
    category_chaild_not = [i for i in categorys for j in category_chaild if i == j.category_parent]
    return locals()