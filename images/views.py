from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from images.forms import CommentForm, ImageForm

from images.models import Img


def images_views(request):
    context = {'imgs': Img.objects.all()}
    return render(request, 'images/page_1.html', context)


def images_detail_view(request, img_id):
    detail = get_object_or_404(Img, id=img_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            comment = form.save(commit=False)
            comment.img = detail
            comment.save()
            form = CommentForm

    comment = detail.comments.all()
    context = {'img_detail': detail, 'comment': comment, 'form': form}
    return render(request, "images/details.html", context)


def save_image_view(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        print(form.fields)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:img'))  # слева пространство имён, справа  название ссылки
    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'images/save_image.html', context)
