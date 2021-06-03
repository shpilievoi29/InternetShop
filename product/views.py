from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from product.forms import ReviewForms
from product.models import Product, Category, Review


class ProductListView(ListView):
    model = Product
    template_name = "product/product.html"

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.request.GET.get("category_id")
        if category_id is not None:
            queryset.filter(category_id=category_id)
        return queryset.exclude(id=0)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


def product_list(request):
    context = {
        "product_list": Product.objects.all(),

    }
    return render(request, "product/product.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["form"] = ReviewForms()
        return context


# def product_detail(request, slug):
#
#     try:
#         product = Product.objects.get(slug=slug)
#     except Product.DoesNotExist:
#         raise Http404("Page not found")
#     if request.method == "POST":
#         review_form = ReviewForms(request.POST)
#         if review_form.is_valid():
#             review = Review(product=product, **review_form.cleaned_data)
#             review.save()
#             redirect_url = reverse_lazy("product_detail", kwargs={"slug": product.slug})
#             return HttpResponseRedirect(redirect_url)
#         else:
#             review_form = ReviewForms()
#         context = {
#             "product": product,
#             "form": review_form,
#
#         }
#         return render(request, "product/product_detail.html", context)


def review(request):
    return render(request, "product/review.html")
