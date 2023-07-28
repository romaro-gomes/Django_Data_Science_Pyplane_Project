from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password=forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    def clean(self):
        data = self.cleaned_data
        
        username = data.get('username')
        password = data.get('password')
        
        
        # if len(username) < 5:
        #     raise forms.ValidationError("O nome de usuário deve ter pelo menos 5 caracteres.")

        
        # if len(password) < 8:
        #     raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")

        
        
        return data