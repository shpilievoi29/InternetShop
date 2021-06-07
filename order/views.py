from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.list import MultipleObjectMixin

from order.forms import OrderForms
from order.models import Order


class OrderListView(ListView):
    http_method_names = ["head", "options", "get"]
    model = Order
    template_name = "order/list.html"

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()

        return queryset.filter(customer=self.request.user, is_deleted=False)


class OrderDetailView(DetailView):
    http_method_names = ["head", "options", "get"]
    model = Order

    def get(self, *args, **kwargs):
        order = self.get_object()
        if order.customer != self.request.user:
            redirect_url = reverse_lazy("order-list")
            return HttpResponseRedirect(redirect_url)

        return super(OrderDetailView, self).get(*args, **kwargs)


class OrderCreateView(CreateView):
    model = Order
    fields = ["product", "quantity", "address"]

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ["quantity", "address"]
    template_name = "order/order_form.html"

    def get(self, *args, **kwargs):
        order = self.get_object()
        if order.customer != self.request.user:
            redirect_url = reverse_lazy("order-list")
            return HttpResponseRedirect(redirect_url)

        return super(OrderUpdateView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        order = self.get_object()
        if order.status < Order.CONFIRMED:
            return super(OrderUpdateView, self).post(*args, **kwargs)

        redirect_url = order.get_absolute_url()
        return HttpResponseRedirect(redirect_url)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("order-list")

    def get(self, *args, **kwargs):
        order = self.get_object()

        if order.customer != self.request.user:
            redirect_url = reverse_lazy("order-list")
            return HttpResponseRedirect(redirect_url)

        return super(OrderDeleteView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        order = self.get_object()

        if order.status < Order.CONFIRMED:
            order.is_deleted = True
            order.save()
            redirect_url = reverse_lazy("order-list")

        else:
            redirect_url = order.get_absolute_url()

        return HttpResponseRedirect(redirect_url)
