from src.models.pet_data_model import *

main_url = 'https://petstore.swagger.io/v2/pet/'


def test_create_pet(request_utility_post, pet_id):
    payload = {
          "id": pet_id,
          "category": {
            "id": 9999,
            "name": "dog"
          },
          "name": "Lucky",
          "photoUrls": [
            "url1",
            "url2"
          ],
          "tags": [
            {
              "id": 1234,
              "name": "black eyes"
            }
          ],
          "status": "sold"
            }
    result = request_utility_post(main_url, **payload)
    assert result.status_code == 200, 'Код ответа соответствует 200 ОК'
    assert len(result.json()) > 0
    NewPet(**result.json())


def test_check_pet(request_utility_get, pet_id):
    result = request_utility_get(main_url, pet_id)
    assert result.status_code == 200, 'Successfully, pet found'
    assert len(result.json()) > 0
    NewPet(**result.json())


def test_delete_pet(request_utility_delete, pet_id):
    result = request_utility_delete(main_url, pet_id)
    assert result.status_code == 200, 'Pet deleted'
    assert len(result.json()) > 0


def test_not_found_pet(request_utility_get, pet_id):
    result = request_utility_get(main_url, pet_id)
    assert result.status_code == 404, 'Pet not found'
