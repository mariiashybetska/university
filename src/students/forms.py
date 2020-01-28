from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings

from students.models import Student, Group


class BaseStudentForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        email_exists = Student.objects \
            .filter(email__iexact=email) \
            .exclude(email__iexact=self.instance.email) \
            .exists()

        if email_exists:
            raise ValidationError(f'{email} is already used')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data('telephone')
        telephone_exists = Student.objects \
            .filter(telephone__exact=telephone) \
            .exclude(telephone__exact=self.instance.telephone) \
            .exists()

        if telephone_exists:
            raise ValidationError(f'Telephone {telephone} ia already used')
        elif not telephone.isdigit():
            raise ValidationError(f'Telephone must contains only digits')
        return telephone


class StudentsAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentsAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'grade', 'email', 'first_name', 'last_name', 'birth_date', 'telephone')


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data  # valid data from form

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)



