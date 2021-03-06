from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, RedirectView
from rest_framework.response import Response
from rest_framework import status

from product.forms import ReviewForms
from product.models import Product, Category, Review, Cart, CartItem
from rest_framework.views import APIView

from rest_framework.decorators import api_view

from product.serializers import ProductSerializer


class ProductListView(ListView):
    model = Product
    http_method_names = ["get", "head", "options", "trace"]
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


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["form"] = ReviewForms()
        return context


class ReviewCreateView(CreateView):
    template_name = "product_detail.html"
    http_method_names = ["post", "head", "options", ]
    model = Review
    form_class = ReviewForms

    def get_success_url(self):
        return reverse_lazy("products:product_detail", kwargs={"slug": self.kwargs.get("slug")})

    def form_valid(self, form):
        slug = self.kwargs.get("slug")
        response = HttpResponseRedirect(self.get_success_url())

        if self.request.session.get(slug) is not None:
            return response

        try:
            product = Product.objects.get(slug=slug)
            form.instance.product = product

            super(ReviewCreateView, self).form_valid(form)

            max_age = 300
            self.request.session.set_expiry(max_age)

            self.request.session[slug] = slug
            return response

        except Product.DoesNotExist:
            return Http404()


class AddToCartView(RedirectView):
    def get(self, *args, **kwargs):
        cart = self.request.session.get("cart", {})
        product_slug = self.kwargs.get("slug")
        if product_slug in cart:
            cart[product_slug] += 1
        else:
            cart[product_slug] = 1
        self.request.session["cart"] = cart
        redirect_url = self.request.headers.get('referer') or reverse_lazy(
            "product:product_list")
        return HttpResponseRedirect(redirect_url)


class PurchaseView(View):
    def get(self, request, *args, **kwargs):
        session_cart = request.session.get('cart')
        if session_cart is None:
            redirect_url = self.request.headers.get('referer') or reverse_lazy(
                "product:product_list")
            return HttpResponseRedirect(redirect_url)
        user = self.request.user
        cart = Cart.objects.get_or_create(user=user, is_active=True)
        for product_slug in session_cart:
            product = Product.objects.get(slug=product_slug)
            quantity = session_cart[product_slug]
            cart_item = CartItem(product=product, quantity=quantity, cart=cart)
            cart_item.save()
            self.request.session["cart"] = {}
        redirect_url = self.request.headers.get('referer') or reverse_lazy(
            "product:product_list")
        return HttpResponseRedirect(redirect_url)


