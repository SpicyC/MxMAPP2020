from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse

from .models import Profile

from .forms import profileForm
# Create your views here.

def index(request):
  all_profiles = Profile.objects.all().order_by('name')
  return render(request, 'myapp/list_profiles.html', context={'myapp':all_profiles})
  

def add_profiles(request):
    if request.method == 'GET':
        form = profileForm()
    else:
        form = profileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "myapp/add_profiles.html", {"form": form})

def delete_profiles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        # message for JS fetch
        return JsonResponse({"deleted": 'true'})
        # django commands
        # return redirect(to='list_albums')
    # return render(request, "albums/delete_albums.html", {"album": album})


def profiles_detail(request, pk):
  profile = get_object_or_404(Profile, pk=pk)
  return render(request, "myapp/profiles_detail.html", {"profile": profile})


# def add_details(request, pk):
#     albums = get_object_or_404(Album, pk=pk)
#     if request.method == 'GET':
#         form = DetailForm()
#     else:
#         form = DetailForm(data=request.POST)
#         if form.is_valid():
#             new_details = form.save(commit=False)
#             new_details.albums = albums
#             new_details.save()
#             return redirect(to='list_albums', pk=pk)

#     return render(request, "albums/add_details.html", {"form": form, "albums": albums})


def edit_profiles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'GET':
        form = profileForm(instance=profile)
    else:
        form = profileForm(data=request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "myapp/edit_profiles.html", {
        "form": form, "profile": profile})

