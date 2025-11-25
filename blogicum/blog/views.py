from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    reversed_posts = list(reversed(posts))
    context = {'posts': reversed_posts}  # передаем посты в контекст
    return render(request, template, context)


def post_detail(request, id):  # добавить параметр id
    template = 'blog/detail.html'
    # Найти пост по id
    post = next((post for post in posts if post['id'] == id), None)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):  # добавить параметр category_slug
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
