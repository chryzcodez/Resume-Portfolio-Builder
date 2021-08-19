from django import forms
from .models import Person, Languages, Awards, Education, Experience, Skills, Project

class PersonForm(forms.ModelForm):
    class Meta:
        model= Person
        fields=['name', 'address', 'email', 'mobile_number']

        widgets={
                'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'My name'}),
                'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Home address'}),
                'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email address'}),
                'mobile_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile Number'}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model= Languages
        fields=['language']

        widgets={
                'language':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Languages understood  English, French'}),
        }

class SkillsForm(forms.ModelForm):
    class Meta:
        model= Skills
        fields=['name']

        widgets={
                'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'My Skills  Python, Django, Laravel'}),
        }

class AwardForm(forms.ModelForm):
    class Meta:
        model= Awards
        fields=['award']

        widgets={
                'award':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Awards received'}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model= Experience
        fields=['company_name', 'company_address', 'post_held', 'year_from', 'year_to', 'info']

        widgets={
                'company_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company name'}),
                'company_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company address'}),
                'post_held':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Position held'}),
                'year_from':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year started    July 20th 2007'}),
                'year_to':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year ended  Ongoing'}),
                'info':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More information'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model= Project
        fields=['name', 'source_code', 'live', 'info']

        widgets={
                'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project name'}),
                'source_code':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Github, Gitlab, BitBucket source code'}),
                'live':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Github Pages, Netlify, Heroku hosted link'}),
                'info':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More information'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model= Education
        fields=['school_name', 'school_address', 'degree', 'year_from', 'year_to', 'info']

        widgets={
                'school_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'School name'}),
                'school_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'School Address or Location'}),
                'degree':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Degree SSCE Neco Bsc'}),
                'year_from':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year started    July 20th 2007'}),
                'year_to':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year ended  Ongoing'}),
                'info':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More information'}),
        }