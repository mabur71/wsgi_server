from django import forms

#from django.forms import ModelForm

from django.contrib.auth.models import User

from .models import Question

from .models import Answer



class AskForm(forms.Form):

    title = forms.CharField(max_length=100)

    text  = forms.CharField(widget=forms.Textarea)

    author = forms.IntegerField(widget=forms.HiddenInput())

    def clean_title(self):

        title = self.cleaned_data['title']

        #if not is_ethic(message):

        #    raise forms.ValidationError(

        #        u'Message not valid', code=12)

        return title

    def clean_text(self):

        text = self.cleaned_data['text']

        #if not is_ethic(message):

        #    raise forms.ValidationError(

        #        u'Message not valid', code=12)

        return text

    def clean_author(self):

        author = self.cleaned_data['author']

        return author

    #def clean(self):

    def save(self):

        user_id = self.cleaned_data['author'] 

        user = User.objects.get(id=user_id )

        question = Question()

        question.author = user

        question.title = self.cleaned_data['title']

        question.text = self.cleaned_data['text']

        question.save()

        return question



class AnswerForm(forms.Form):

    text = forms.CharField(max_length=100)

    question = forms.IntegerField(widget=forms.HiddenInput())

    #author = forms.IntegerField()

    author = forms.IntegerField(widget=forms.HiddenInput())

    def clean_text(self):

        text = self.cleaned_data['text']

        #if not is_ethic(message):

        #    raise forms.ValidationError(

        #        u'Message not valid', code=12)

        return text

    def clean_question(self):

        question = self.cleaned_data['question']

        #if not is_ethic(message):

        #    raise forms.ValidationError(

        #        u'Message not valid', code=12)

        return question

    def clean_author(self):

        author = self.cleaned_data['author']

        return author

    def save(self):

        user_obj = User.objects.get(id=self.cleaned_data['author'])

        cleaned_question_value = self.cleaned_data['question']

        question_obj = Question.objects.get(id=cleaned_question_value)

        answer_obj = Answer()

        answer_obj.author = user_obj

        answer_obj.question = question_obj

        answer_obj.text = self.cleaned_data['text']

        answer_obj.save()

        return answer_obj



    #def clean():



class SignupForm(forms.Form):

    username = forms.CharField(max_length=30)

    email = forms.EmailField()

    password = forms.CharField(widget = forms.PasswordInput())

    def clean_username(self):

        username = self.cleaned_data['username']

        return username

    def clean_email(self):

        email = self.cleaned_data['email']

        return email

    def clean_password(self):

        password = self.cleaned_data['password']

        return password

    #def save(self)

    #    return



class LoginForm(forms.Form):

    username = forms.CharField(max_length=30)

    password = forms.CharField(widget = forms.PasswordInput())

    def clean_username(self):

        username = self.cleaned_data['username']

        return username

    def clean_password(self):

        password = self.cleaned_data['password']

        return password
