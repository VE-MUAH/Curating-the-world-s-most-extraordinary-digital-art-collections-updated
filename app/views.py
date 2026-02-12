from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.

class IndexView(generic.ListView):
    template_name = "app/apptemplate.html"
    context_object_name = "all_collection"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Collection.objects.filter(collection_name__icontains=query)
        return Collection.objects.all()


class DetailsView(generic.DetailView):
    model = Collection
    template_name = "app/detailtemplate.html"
    context_object_name = "citem"


class UserFormView(View):
    form_class = UserForm
    template_name = 'app/formtemplate.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            newuser = authenticate(username=username, password=password)

            if newuser is not None:
                if newuser.is_active:
                    login(request, newuser)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})

from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth import logout

class LoginView(DjangoLoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return '/app/' # Redirect to home page after login

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

from .forms import PieceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PieceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Piece
    form_class = PieceForm
    template_name = 'app/add_piece.html'
    success_url = reverse_lazy('index') # Redirect to home after adding
    
    # Optional: Automatically set some fields or handle logic
    def form_valid(self, form):
        # We could auto-assign user if specific models had user field
        return super().form_valid(form)

class PieceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Piece
    form_class = PieceForm
    template_name = 'app/add_piece.html' # Reuse the form template
    success_url = reverse_lazy('index')

class PieceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Piece
    template_name = 'app/confirm_delete.html'
    success_url = reverse_lazy('index')

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.db.models import Count
import json

@method_decorator(staff_member_required, name='dispatch')
class DashboardView(View):
    template_name = 'app/dashboard.html'
    
    def get(self, request):
        # Basic stats
        total_collections = Collection.objects.count()
        total_pieces = Piece.objects.count()
        total_artists = Piece.objects.values('artist').distinct().count()
        
        # Pieces per collection for pie chart
        collection_data = Collection.objects.annotate(
            piece_count=Count('piece')
        ).values('collection_name', 'piece_count')
        
        collection_labels = [item['collection_name'] for item in collection_data]
        collection_counts = [item['piece_count'] for item in collection_data]
        
        # Pieces per year for bar chart
        year_data = Piece.objects.values('year').annotate(
            count=Count('id')
        ).order_by('year')
        
        year_labels = [str(item['year']) for item in year_data]
        year_counts = [item['count'] for item in year_data]
        
        # Top artists
        top_artists = Piece.objects.values('artist').annotate(
            count=Count('id')
        ).order_by('-count')[:5]
        
        context = {
            'total_collections': total_collections,
            'total_pieces': total_pieces,
            'total_artists': total_artists,
            'collection_labels': json.dumps(collection_labels),
            'collection_counts': json.dumps(collection_counts),
            'year_labels': json.dumps(year_labels),
            'year_counts': json.dumps(year_counts),
            'top_artists': top_artists,
        }
        return render(request, self.template_name, context)
