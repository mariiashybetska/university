from django.forms import ModelForm, ValidationError

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        email_exists = Teacher.objects \
            .filter(email__iexact=email) \
            .exclude(email__iexact=self.instance.email) \
            .exists()

        if email_exists:
            raise ValidationError(f'{email} is already used')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        telephone_exists = Teacher.objects \
            .filter(telephone__exact=telephone) \
            .exclude(telephone__exact=self.instance.telephone) \
            .exists()

        if telephone_exists:
            raise ValidationError(f'Telephone {telephone} ia already used')
        elif not telephone.isdigit():
            raise ValidationError(f'Telephone must contains only digits')
        return telephone


class TeachersAddForm(TeacherBaseForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(TeacherBaseForm):
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'email', 'telephone', 'faculty')
