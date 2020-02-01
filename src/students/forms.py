from django.forms import ModelForm, Form, EmailField, CharField, ValidationError

from students.models import Student, Group
from students.tasks import send_email_async

from datetime import datetime


class BaseStudentForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        email_exists = Student.objects \
            .filter(email__iexact=email) \
            .exclude(id=self.instance.id) \
            .exists()

        if email_exists:
            raise ValidationError(f'{email} is already used')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']

        if not telephone.isdigit():
            raise ValidationError(f'Telephone must contains only digits')

        telephone_exists = Student.objects \
            .filter(telephone__exact=telephone) \
            .exclude(id=self.instance.id) \
            .exists()

        if telephone_exists:
            raise ValidationError(f'Telephone {telephone} ia already used')

        return telephone


class StudentsAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentsAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'grade', 'email', 'first_name', 'last_name', 'birth_date', 'telephone', 'active_user')


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
        # student = Student.objects.get_or_create(email=email_from)[0]
        # send_mail(subject, message, email_from, recipient_list)
        send_email_async.delay(subject, message, email_from)


class RegistrationForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'grade', 'email', 'first_name', 'last_name', 'telephone')

    def save(self):
        s = Student.objects.create(grade=self.instance.grade,
                                   first_name=self.instance.first_name,
                                   last_name=self.instance.last_name,
                                   birth_date=datetime.now().date(),
                                   email=self.instance.email,
                                   telephone=self.instance.telephone
                                   )

        subject = 'Confirm your registration'
        message = f'Please, confirm your email. The link is http://127.0.0.1:8000/students/registration/confirm/{s.id}'
        email_from = self.instance.email
        send_email_async.delay(subject, message, email_from)

