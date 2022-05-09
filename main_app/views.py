from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from .models import Liveable, Listing
from django.contrib.auth import login
###from .filters import ListingFilter
###from .forms import AffordabilityForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def liveables_index(request):
    liveables = Liveable.objects.filter(user = request.user)
    return render(request, 'liveables/index.html', {'liveables': liveables})


def liveables_detail(request, liveable_id):
    liveable = Liveable.objects.get(id=liveable_id)
    affordability_form = AffordabilityForm()
    listings_liveable_doesnt_have = Listing.objects.exclude(id__in = liveable.listings.all().values_list('id'))

    return render(request, 'liveables/detail.html', {
        'liveable': liveable,
        'listings': listings_liveable_doesnt_have,
        'affordability_form': affordability_form
    })

class LiveableCreate(LoginRequiredMixin, CreateView):
    model = Liveable
    fields = ('name', 'description', 'listings')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LiveableUpdate(LoginRequiredMixin, UpdateView):
    model = Liveable
    fields = ('name', 'description')

class LiveableDelete(LoginRequiredMixin, DeleteView):
    model = Liveable
    success_url = '/liveables/'

@login_required
def assoc_listing(request, liveable_id, listing_id):
    Liveable.objects.get(id=liveable_id).listings.add(listing_id)
    return redirect('liveables_detail', liveable_id=liveable_id)

def add_affordability(request, liveable_id):
    form = AffordabilityForm(request.POST)
    if form.is_valid():
        new_affordability = form.save(commit=False)
        new_affordability.liveable_id = liveable_id
        new_affordability.save()
    return redirect('detail', liveable_id=liveable_id)



def signup(request):
    # we'll need this for our context dictionary, in case there are no errors
    error_message = ''
    # check for a POST request (as opposed to a GET request)
    if request.method == 'POST':
        # capture form inputs
        user_form = UserCreationForm(request.POST)
       
        # validate form inputs (make sure everything we need is there)
        if user_form.is_valid():
            # save the new user to the database
            user = user_form.save()
                      # log the new user in
            login(request, user)
         
            # redirect to the liveables index page
            return redirect('liveables_index')
        # if form is NOT valid
        else:
            error_message = 'invalid sign up - please try again'
            # redirect to signup page (/accounts/signup) and display error message
    # If GET request
        # render a signup page with a blank user creation form
    user_form = UserCreationForm() 
    

    context = {
        'user_form': user_form,
        'error': error_message,
      
    }    
    return render(request, 'registration/signup.html', context)

class ListingCreate(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ('community', 'neighborhood', 'price', 'beds', 'baths', 'sqft', 'main_photo')

class ListingUpdate(LoginRequiredMixin, UpdateView):
    model = Listing
    fields = ('community', 'neighborhood', 'price', 'beds', 'baths', 'sqft')

class ListingDelete(LoginRequiredMixin, DeleteView):
    model = Listing
    success_url = '/liveables/'

class ListingList(LoginRequiredMixin, ListView):
    model = Listing
    template_name = 'listings/index.html'
    context_object_name = 'listings'

class ListingDetail(LoginRequiredMixin, DetailView):
    model = Listing
    template_name = 'listings/detail.html'


class ListingList(LoginRequiredMixin, ListView):
    model = Listing
    template_name = 'listings/search.html'
    context_object_name = 'listings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ListingFilter(self.request.GET, queryset=self.get_queryset())
        return context


