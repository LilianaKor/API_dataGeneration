
import allure
import pytest

from data import get_pet_endpoints
from data.data import PetData
from src import CreatePetShem
from src.assertions import Assertions
from src.http_methods import MyRequests
from http import HTTPStatus
from src.prepare_data.prepare_pet_data import PreparePetData
from src.validator import Validator
import json
from generator.pet_generator import PetGenerator


@allure.epic("Testing create pet")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()
    validator = Validator()
    pet_data = PreparePetData()
    pet_generator = PetGenerator()

    @allure.title("Create pet")
    def test_create(self, get_test_name):
        info = next(self.pet_generator.generate_pet())
        data = self.pet_data.prepare_pet_json(info=info)
        print(data)
        response = self.request.post(url=self.url.create_pet, data=data)

        self.assertions.assert_status_code(
            response=response,
            actual_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response, model=CreatePetShem.create_pet)
        print(response.text)

    @allure.title("Create pet with status")
    @pytest.mark.parametrize("status", PetData.status)
    def test_create_pet_with_status(self, get_test_name, status):
        info = next(self.pet_generator.generate_pet(status=status))
        data = self.pet_data.prepare_pet_json(info=info)
        print(data)
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(
            response=response,
            actual_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response, model=CreatePetShem.create_pet)
        print(response.text)

    @allure.title("Create pet with wrong status")
    def test_create_pet_with_wrong_status(self, get_test_name):
        info = next(self.pet_generator.generate_pet(status="wrong_status"))
        data = self.pet_data.prepare_pet_json(info=info)
        print(data)
        response = self.request.post(url=self.url.create_pet, data=data)

        self.assertions.assert_status_code(
            response=response,
            actual_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response, model=CreatePetShem.create_pet)
        print(response.text)




    # def test_create_pet(self, get_test_name):
    #     info = next(self.pet_generator.generate_pet())
    #     print(info)

        # data = self.pet_data.get_pet_json()
        # response = self.request.post(url=self.url.create_pet, data=data)
        # print(response.text)
        # self.assertions.assert_status_code(
        #     response=response,
        #     actual_status_code=HTTPStatus.OK,
        #     test_name=get_test_name
        #)
        # self.validator.validate_response(response=response, model=CreatePetShem.create_pet)







