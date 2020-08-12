from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse

from .models import Profile

from .forms import profileForm
# Create your views here.

def index(request):
  all_profiles = Profile.objects.all().order_by('name')
  
  return render(request, 'profiles/list_profiles.html', context={'profiles':all_profiles})
  

def add_profiles(request):
    if request.method == 'GET':
        form = profileForm()
    else:
        form = profileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "profiles/add_profiles.html", {"form": form})

def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        
        return JsonResponse({"deleted": 'true'})
        


def profiles_detail(request, pk):
  profile = get_object_or_404(Profile, pk=pk)
  return render(request, "profiles/profiles_detail.html", {"profile": profile})





def edit_profiles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'GET':
        form = profileForm(instance=profile)
    else:
        form = profileForm(data=request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "profiles/edit_profiles.html", {
        "form": form, "profile": profile})

def token(request):
    fake = Factory.create()
    return generateToken(fake.user_name())

def generateToken(identity):
    # Get credentials from environment variables
    account_sid      = settings.TWILIO_ACCT_SID
    chat_service_sid = settings.TWILIO_CHAT_SID
    sync_service_sid = settings.TWILIO_SYNC_SID
    api_sid          = settings.TWILIO_API_SID
    api_secret       = settings.TWILIO_API_SECRET

    # Create access token with credentials
    token = AccessToken(account_sid, api_sid, api_secret, identity=identity)

    # Create a Sync grant and add to token
    if sync_service_sid:
        sync_grant = SyncGrant(service_sid=sync_service_sid)
        token.add_grant(sync_grant)

    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().decode('utf-8')})
def token(request):
    fake = Factory.create()
    return generateToken(fake.user_name())

def generateToken(identity):
    # Get credentials from environment variables
    account_sid      = settings.TWILIO_ACCT_SID
    chat_service_sid = settings.TWILIO_CHAT_SID
    sync_service_sid = settings.TWILIO_SYNC_SID
    api_sid          = settings.TWILIO_API_SID
    api_secret       = settings.TWILIO_API_SECRET

    # Create access token with credentials
    token = AccessToken(account_sid, api_sid, api_secret, identity=identity)

    # Create a Sync grant and add to token
    if sync_service_sid:
        sync_grant = SyncGrant(service_sid=sync_service_sid)
        token.add_grant(sync_grant)

    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().decode('utf-8')})