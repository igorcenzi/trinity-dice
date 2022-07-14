from rest_framework.test import APITestCase
from rest_framework.views import status

from users.models import User


class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.username = "Jorginho"
        cls.email = "jorginho_joga_10@gmail.com"
        cls.password = "123@456"
        cls.phone = "+55212345678"
        cls.is_master = False

        cls.superusername = "Adminho"
        cls.superemail = "adminho_bane_geral@gmail.com"
        cls.superpassword = "tobanindogeral"
        cls.superphone = "+55212354137"
        cls.superis_master = False

        cls.user = User.objects.create_user(
            username=cls.username,
            email=cls.email,
            password=cls.password,
            phone=cls.phone,
            is_master=cls.is_master,
        )

        cls.superuser = User.objects.create_superuser(
            username=cls.superusername,
            email=cls.superemail,
            password=cls.superpassword,
            phone=cls.superphone,
            is_master=cls.superis_master,
        )

    def test_should_create_user(self):
        response = self.client.post(
            "/users/",
            {
                "username": "novo_user",
                "email": "novo_user@email.com",
                "password": "12345678",
                "phone": "+5519999994512",
                "is_master": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["id"])

    def test_should_not_return_password(self):
        response = self.client.post(
            "/users/",
            {
                "username": "novo_user",
                "email": "novo_user@email.com",
                "password": "12345678",
                "phone": "+5519999994512",
                "is_master": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(hasattr(response.data, "password"))

    def test_should_login_as_user(self):
        response = self.client.post(
            "/login/", {"email": self.email, "password": self.password}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = response.data
        self.assertTrue(user["refresh"])
        self.assertTrue(user["access"])

    def test_should_login_as_superuser(self):
        response = self.client.post(
            "/login/", {"email": self.superemail, "password": self.superpassword}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = response.data
        self.assertTrue(user["refresh"])
        self.assertTrue(user["access"])

    def test_should_update_user_with_own_token(self):
        response_login = self.client.post(
            "/login/", {"email": self.email, "password": self.password}
        )
        token = response_login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response_update = self.client.patch(
            "/users/" + str(self.user.id) + "/",
            {"username": "Updated_Username", "password": "1234"},
        )
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)

    def test_should_update_user_with_superuser_token(self):
        response_login = self.client.post(
            "/login/", {"email": self.superemail, "password": self.superpassword}
        )
        token = response_login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response_update = self.client.patch(
            "/users/" + str(self.user.id) + "/",
            {"username": "Updated_Username", "password": "1234"},
        )
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)

    def test_should_not_update_is_master(self):
        response_login = self.client.post(
            "/login/", {"email": self.email, "password": self.password}
        )
        token = response_login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response_update = self.client.patch(
            "/users/" + str(self.user.id) + "/", {"is_master": True}
        )
        self.assertEqual(response_update.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_not_update_without_token(self):
        response_update = self.client.patch(
            "/users/" + str(self.user.id) + "/", {"is_master": True}
        )
        self.assertEqual(response_update.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_delete_user_with_superuser_token(self):
        response_login = self.client.post(
            "/login/", {"email": self.superemail, "password": self.superpassword}
        )
        token = response_login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response_update = self.client.delete("/users/" + str(self.user.id) + "/")
        self.assertEqual(response_update.status_code, status.HTTP_204_NO_CONTENT)

    def test_should_not_delete_without_token(self):
        response_update = self.client.delete("/users/" + str(self.user.id) + "/")
        self.assertEqual(response_update.status_code, status.HTTP_401_UNAUTHORIZED)
