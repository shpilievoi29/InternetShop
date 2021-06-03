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
    model = Order
    template_name = "order/list.html"
    queryset = Order.objects.all()


class OrderDetailView(DetailView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    fields = "__all__"
    template_name = "order/order_form.html"


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = "__all__"
    queryset = Order.objects.get_queryset()


class OrderDeleteView(DeleteView):
    model = Order

