from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from validate_email import validate_email



class UserRegisterform(UserCreationForm):
    first_name = forms.CharField(max_length=10,min_length=5)
    last_name = forms.CharField(max_length=10,min_length=5)
    email = forms.EmailField()

    def clean_username(self):
        data = self.cleaned_data.get('username')

        if len(data) < 8:
            raise forms.ValidationError("username mustnot be less than eight character")
        elif data.isdigit():
            raise forms.ValidationError("only numeric characters")
        else:
            return data
    
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        
        if len(data) > 10:
            raise forms.ValidationError("firstname can be of only 10 charaacters")
        elif len(data) < 5:
            raise forms.ValidationError("firstname can't be less than 5 charaacters")
        elif data.isdigit():
            raise forms.ValidationError("only numeric characters")
        else:
            return data
    
    def clean_email(self):   
        email = self.cleaned_data.get('email')
        if validate_email(email):
            return email
        else:
            raise forms.ValidationError("Domain of this email is incorrect")    
          
            
    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if len(data) > 10:
            raise forms.ValidationError("firstname can be of only 10 charaacters")
        elif len(data) < 5:
            raise forms.ValidationError("firstname can't be less than 5 charaacters")
        elif data.isdigit():
            raise forms.ValidationError("only numeric characters")
        else:
            return data        

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        help_texts = {
            'username': None,
        }



class userloginform(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']        




class SellerRegisterform(UserCreationForm):
    first_name = forms.CharField(max_length=10,min_length=5)
    last_name = forms.CharField(max_length=10,min_length=5)
    address = forms.CharField(max_length=10,min_length=5)
    phone = forms.IntegerField()
    email = forms.EmailField()
    
    def clean_username(self):
        data = self.cleaned_data.get('username')
        if len(data) < 8:
            raise forms.ValidationError("username mustnot be less than eight character")
        elif data.isdigit():
            raise forms.ValidationError("only numeric characters")
        else:
            return data
    
    def clean_phone(self):
          data = self.cleaned_data.get('phone')
          if len(str(data)) <10 :
            raise forms.ValidationError("phone must be equal to 10 digit")
          elif len(str(data)) > 10:
            raise forms.ValidationError("phone must be equal to 10 digit")
          else:
              return data  

    def clean_email(self):   
        email = self.cleaned_data.get('email')
        if validate_email(email):
            return email
        else:
            raise forms.ValidationError("Domain of this email is incorrect")    
          
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if len(data) > 10:
            raise forms.ValidationError("firstname can be of only 10 charaacters")
        elif len(data) < 5:
            raise forms.ValidationError("firstname can't be less than 5 charaacters")
        elif data.isdigit():
            raise forms.ValidationError("only numeric characters")
        else:
            return data

    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if len(data) > 10:
            raise forms.ValidationError("firstname can be of only 10 charaacters")
        elif len(data) < 5:
            raise forms.ValidationError("firstname can't be less than 5 charaacters")
        elif data.isdigit():
            raise forms.ValidationError("only numeric characters")
        else:
            return data        

    class Meta:
        model = User
        fields = ['username','first_name','last_name','address','phone','email','password1','password2']
        help_texts = {
            'username': None,
        }

