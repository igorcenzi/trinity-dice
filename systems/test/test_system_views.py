from rest_framework.test import APITestCase
from rest_framework.views import status

from users.models import User


class AdminSystemViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.master_username = "Adminho"
        cls.master_email = "adminho_bane_geral@gmail.com"
        cls.master_password = "tobanindogeral"
        cls.master_phone = "+55212354137"
        cls.master_is_master = True

        cls.master_user = User.objects.create_user(
            username=cls.master_username,
            email=cls.master_email,
            password=cls.master_password,
            phone=cls.master_phone,
            is_master=cls.master_is_master,
        )

        cls.system_request_body = {    
            "name": "Dungeons & Dragons",
            "dice": 20,
            "version": 3.5,
            "classes": [
                { "name": "Warrior" },
                { "name": "Ranger" },
                { "name": "Archer" },
                { "name": "Mage" }
            ]
        }


    def setUp(self):
        response = self.client.post(
            "/login/",
            { "email": self.master_email, "password": self.master_password },
        ).json()

        self.assertTrue(response["access"])
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response['access']}"
        )

    def test_should_create_system(self):
        system_request = self.system_request_body
        response = self.client.post(
            "/systems/", system_request, format="json")

        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("id" in response.data)
        self.assertTrue("name" in response.data)
        self.assertTrue("dice" in response.data)
        self.assertTrue("version" in response.data)
        self.assertTrue("classes" in response.data)
        self.assertTrue("items" in response.data)
        self.assertTrue("journeys_amount" in response.data)
        self.assertTrue("is_active" in response.data)
        self.assertTrue("created_at" in response.data)

    def test_should_create_empty_system(self):
        response = self.client.post("/systems/", {}, format="json")

        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        for field in ["name", "dice", "version", "classes"]:
            self.assertTrue(response.data[field], "This field is required.")

    def test_should_list_all_systems(self):
        for _ in range(1,6):
            response = self.client.post(
                "/systems/", self.system_request_body, format="json")
            self.assertTrue(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get("/systems/")
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertTrue("count" in response.data)
        self.assertTrue("next" in response.data)
        self.assertTrue("previous" in response.data)
        self.assertTrue("results" in response.data)
        self.assertTrue(len(response.data["results"]), 5)

    def test_should_list_specific_system(self):
        response_post = self.client.post(
            "/systems/", self.system_request_body, format="json")
        self.assertTrue(response_post.status_code, status.HTTP_201_CREATED)

        system_id = response_post.data["id"]
        response = self.client.get(f"/systems/{system_id}/")

        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in response.data)
        self.assertTrue("name" in response.data)
        self.assertTrue("dice" in response.data)
        self.assertTrue("version" in response.data)
        self.assertTrue("classes" in response.data)
        self.assertTrue("items" in response.data)
        self.assertTrue("journeys_amount" in response.data)
        self.assertTrue("is_active" in response.data)
        self.assertTrue("created_at" in response.data)

    def test_should_not_list_invalid_system_id(self):
        response = self.client.get("/systems/1/")
        self.assertTrue(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_deactivate_system(self):
        response_post = self.client.post(
            "/systems/", self.system_request_body, format="json")
        self.assertTrue(response_post.status_code, status.HTTP_201_CREATED)

        system_id = response_post.data["id"]
        response = self.client.delete(f"/systems/{system_id}/")

        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['detail'], 'System deactivated!')

    def test_should_not_deactivate_invalid_system_id(self):
        response = self.client.delete(f"/systems/1/")

        self.assertTrue(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(response.data['detail'], 'System not found!')

