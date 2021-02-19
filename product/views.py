from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from product.models import Category, Product


def homepage(request):
    categories = Category.objects.all()
    #SELECT * FROM product_category;
    return render(request, 'product/index.html', {'categories': categories})

def products_list(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('Нет такой категории')
    products = Product.objects.filter(category_id = category_slug)
    return render(request, 'product/products_list.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product': product})






#products/category
# def products_list(request,category_slug):
#     #products = Product.objects.all()
#     # if Category.object.filter(slug = category_slug).exist():
#     #     raise Http4
#     # products = Product.objects.filter(category_id=category_slug)
#     # category = get_object_or_404(Category, slug=category_slug)
#     # products = Product.objects.filter(category=category)
#     products = get_list_or_404(Product, category_id=category_slug)
#     #SELECT * FROM product WHERE category_id = category_slug;
#     return render(request, 'product/products_list.html', {'products': products})

#TODO: переписать вбюшку product list +
#TODO: подключить картинки для товаров +
#TODO: Добавить детали продукта +
#TODO: сделать переход из категории в листинг продуктов +
#TODO:  переписать вьюшки на CBV

#products/?category=slug
# def products_list2(request):
#     category_slug = request.GET.get('category')
#     products = Product.object.all()
#     if category_slug is not None:
#         products = products.filter(category_id=category_slug)
#     return render(request, '', {'products': products})


#all() - выводит все обьекты модели
#SELECT * FROM table;

# Category.objects.filter(...).all()

#filter() - фильтрует результат запроса
# SELECT * FROM table WHERE ...;

#exclude(category_id=1) - исключает из результатов обьекты, отвечающие условию;
# SELECT * FROM table WHERE category !=1;

# exclude(title__startswith='Apple')
# SELECT * FROM product WHERE title NOT LIKE 'Apple%';

#order_by() - сортировка результатов запроса
# Product.objects.order_by('price')
# SELECT * FROM product ORDER BY pice ASC;

# Product.objects.order_by('-price')
# SELECT * FROM product ORDER BT price DESC;

# Product.objects.order_by('price', 'popularity')
# SELECT * FROM product ORDER BY price ASC, popularity ASC;

# Product.objects.order_by('?') -> произвольная сортировка(рандомная)

# Products.objects.reverse() - all() - в обратном порядке

# distinct() - исключает повторения
# Product.objects.values_list('category', flat=True).distinct() -> список

# values()
# Product.objects.values() -> список из словарей
# Product.objects.values('id', 'title')


# values_list()
# Product.objects.values_list() -> список с кортежами
# Product.objects.values_list('id', 'title')

# none() - пустой queryset
# Product.objects.none()

# select_related()
# prod = Product.objects.select_related('category').get(id=1)


# prefetch_related()
# categories = Category.objects.prefetch_related('products').filter(...)
# for cat in categories:
#     cat.product_set.all()
# SELECT * FROM catrgory WHERE category_id IN (5,6,8,9,10);

# defer()
# Product.objects.defer('price', 'category_id') -> Выводит все кроме price , category_id

# only()
# Product.objects.only(price,category_id) -> выводит только price, category_id


# get() - возвращает обьект
#Product.objects.get(id=2);
# Если нет обекта по условию:
# Product.objects.get(id=100) -> Product.DoesNotExist


# Если get находит несколько обьектов:
# Ошибка Product.MultipleObjectsReterned

# create() - позволяет создавать новые обьекты модели
# Product.objects.create(title='Пшено', description='...', price= 100)
#
# prod = Product(title='Пшено', description='...', price= 100)
# prod.save()

# get_or_create(условие) - выбирает обьект, отвечающий условию , если нет обьекта тогда создает

# update_or_create() - обновляет или создает обьекты

# bulk_create() - позволяет создавать одновременно несколько обектов
# obj1 = Product()
# obj2 = Product
# Product.objects.bulk_create([obj1,obj2])

#
# bulk_update() - обновляет несколько обьектов

# count() - возращает количество результатов в queryset

# first(), last()
# Product.objects.fierst() - первое значение
#
# earlies, latest()
# Product.objects.earliest('price') - первое значение по цене

# exist() - проверяет есть ли в queryset хоть один результат
# Product,objects.filter(price__gt=2000).exists()  -True/False

# delete() - удаляет результаты queryset
# Product.objects.filter(category_id=2).delete()

# explain() - возввращает SQL запрос queryset
#Product.objects.all().explain() -> SELECT * FROM product;


# Field lookups:
# сравнение:
# gt -> ">"
# lt -> "<"
# gte -> ">="
# lte -> "<="
# = -> '='

# startswith='A' -> LIKE 'A%'
# istartswith='A' -> ILIKE 'A%'

# contains="day" -> LIKE "%day%"
# icontains="day" -> iLIKE "%day%"

# endswith='j'
# iendswith='j'

# title__exact="Milk" -> WHERE title = "Milk"
# title__iexact="Milk" -> WHERE title ILIKE "Milk"

# category__isnull=True -> WHERE category IS NULL;
# category__isnull=False -> WHERE category IS NOT NULL;

# id__in=[1,2,3,4] -> WHERE id IN (1,2,3,4);

# Order.objects.filter(date__range=(start_date, stop_date)) -> WHERE date BETWWEN start_date AND stop_date




