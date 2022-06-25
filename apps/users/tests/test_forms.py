import pytest
from apps.users.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .tests import app_user_factory, app_user_group

pytestmark = pytest.mark.django_db


class TestCustomUserCreationForm:

    @pytest.fixture
    def create_test_user(self, db, app_user_factory) -> User:
        return app_user_factory(username="TestUser", password="", email="test")

    def test_custom_user_creation_form_invalid(self):
        form_data = {'something': 'something'}
        form = CustomUserCreationForm(data=form_data)
        assert form.is_valid() is False
        assert form.errors
        assert "This field is required." in form.errors['username']

    def test_custom_user_creation_form_valid(self):
        form_data = {'username': 'testuser',
                     'email': 'testuser@wp.pl',
                     'password1': 'testuser',
                     'password2': 'testuser'}
        form = CustomUserCreationForm(data=form_data)
        assert form.is_valid() is True

    def test_bad_email(self):
        form_data = {'username': 'testuser',
                     'email': 'testuser',
                     'password1': 'testuser',
                     'password2': 'testuser'}
        form = CustomUserCreationForm(data=form_data)
        assert form.is_valid() is False
        assert "Enter a valid email address." in form.errors['email']

    def test_username_already_exists(self, create_test_user: User):
        user = create_test_user
        form_data = {'username': user.username,
                     'email': user.email,
                     'password1': user.password,
                     'password2': user.password}
        form = CustomUserCreationForm(data=form_data)
        assert form.is_valid() is False
        assert "The username is taken, please try another one" in form.errors['username']

    def test_email_already_exists(self, create_test_user: User):
        user = create_test_user
        form_data = {'username': 'testuser',
                     'email': user.email,
                     'password1': user.password,
                     'password2': user.password}
        form = CustomUserCreationForm(data=form_data)
        assert form.is_valid() is False
        assert "Enter a valid email address." in form.errors['email']
