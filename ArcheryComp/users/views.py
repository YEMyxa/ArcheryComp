from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin



class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('tasks:index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    

class MyProfile(LoginRequiredMixin, View):

    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'users/profile.html', context)
    
    def post(self,request):
        user_form = UserUpdateForm(
            request.POST, 
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            # messages.success(request,'Your profile has been updated successfully')
            
            return redirect('tasks:index')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            # messages.error(request,'Error updating you profile')
            
            return render(request, 'users/profile.html', context)