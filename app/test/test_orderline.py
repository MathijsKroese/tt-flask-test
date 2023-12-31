import unittest
from app.test.base import BaseTestCase


def get_all_orderlines(self):
    return self.client.get('/')


def add_new_orderline(self):
    return self.client.post(
        "/",
        data={
            "brand_id": 1,
            "contractual_partner_id": 2,
            "completed": False
        },
        content_type="application/json"
    )


class TestGetAllOrderlines(BaseTestCase):
    def test_get_all_orderlines(self):
        with self.client:
            response = get_all_orderlines(self)
            print(response.data)
            self.assertTrue(response is not None)
            self.assertEqual(response.status_code, 200)


class TestAddNewOrderline(BaseTestCase):
    def test_add_new_orderline(self):
        with self.client:
            response = add_new_orderline(self)
            self.assertEqual(response.status_code, 201)
            # data = json.loads(response.data.decode())
            # self.assertTrue(data["status"] == "success")
            # self.assertTrue(data["message"] == "new orderline created")
            # self.assertTrue(response.content_type == "application/json")
            # self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
