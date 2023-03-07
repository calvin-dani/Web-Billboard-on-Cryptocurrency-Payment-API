from crud_server import app1, set_endpoint_metadata
import unittest as ut
from payload_utils import get_payload_attr


class TestIntegrations(ut.TestCase):

    def setUp(self):
        self.app1 = app1.test_client()

    #Test utility endpoint to retrieve transaction details 
    def test_endpoints(self):
        url, obj = set_endpoint_metadata("1234")
        self.assertEqual(
            url, "https://www.blockonomics.co/api/merchant_order/1234")

    #Test utility parser to retrieve transaction details 
    def test_payload_creator(self):
        
        important_attr = {
            "uuid", "address", "name", "emailid", "Message", "paid_satoshi",
            "timestamp"
        }

        attr_data_arr = {"name", "emailid", "Message"}

        data = {}
        payload = {"data": {}}
        for attr in important_attr:
            if not (attr in attr_data_arr):
                payload[attr] = ""
            elif (attr in attr_data_arr):
                payload["data"][attr] = ""

            data[attr] = get_payload_attr(payload, attr, attr in attr_data_arr)
            
        self.assertEqual(len(data) , len(important_attr))

    



if __name__ == '__main__':
    ut.main()