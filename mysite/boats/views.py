from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from boats.models import Boat, Type
# from cats.forms import CatForm, BreedForm
# from boats.forms import BreedForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Type.objects.count()
        al = Boat.objects.all()

        ctx = {'type_count': mc, 'boat_list': al}
        return render(request, 'boats/boat_list.html', ctx)

class TypeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Type.objects.all()
        ctx = {'type_list': ml}
        return render(request, 'boats/type_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
# class BreedCreate(LoginRequiredMixin, View):
#     template = 'cats/breed_form.html'
#     success_url = reverse_lazy('cats:all')

#     def get(self, request):
#         form = BreedForm()
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request):
#         form = BreedForm(request.POST)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         breed = form.save()
#         return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
# class BreedUpdate(LoginRequiredMixin, View):
#     model = Breed
#     success_url = reverse_lazy('cats:all')
#     template = 'cats/breed_form.html'

#     def get(self, request, pk):
#         breed = get_object_or_404(self.model, pk=pk)
#         form = BreedForm(instance=breed)
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         breed = get_object_or_404(self.model, pk=pk)
#         form = BreedForm(request.POST, instance=breed)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         form.save()
#         return redirect(self.success_url)


# class BreedDelete(LoginRequiredMixin, View):
#     model = Breed
#     success_url = reverse_lazy('autos:all')
#     template = 'cats/breed_confirm_delete.html'

#     def get(self, request, pk):
#         breed = get_object_or_404(self.model, pk=pk)
#         ctx = {'breed': breed}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         breed = get_object_or_404(self.model, pk=pk)
#         breed.delete()
#         return redirect(self.success_url)


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes


class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('boats:all')


class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('boats:all')


class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('boats:all')




class BoatCreate(LoginRequiredMixin, CreateView):
    model = Boat
    fields = '__all__'
    success_url = reverse_lazy('boats:all')


class BoatUpdate(LoginRequiredMixin, UpdateView):
    model = Boat
    fields = '__all__'
    success_url = reverse_lazy('boats:all')


class BoatDelete(LoginRequiredMixin, DeleteView):
    model = Boat
    fields = '__all__'
    success_url = reverse_lazy('boats:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#createview