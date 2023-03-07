from crud_server import app1, set_endpoint_metadata
import unittest as ut
from payload_utils import get_payload_attr,parse_transaction_payload


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

        IMPORTANT_ATTR = {
            "uuid", "address", "name", "emailid", "Message", "paid_satoshi",
            "timestamp"
        }
        ARRE_DATA_ARR = {"name", "emailid", "Message"}
        
        data = {}
        payload = self.create_payload_util(IMPORTANT_ATTR,ARRE_DATA_ARR)
        try:
            data = parse_transaction_payload(payload)
        finally:
            self.assertEqual(len(data), len(IMPORTANT_ATTR))

       

    def create_payload_util(self,IMPORTANT_ATTR,ARRE_DATA_ARR):
        
        payload = {"data": {}}
        for attr in IMPORTANT_ATTR:
            if (attr not in ARRE_DATA_ARR):
                payload[attr] = ""
            elif (attr in ARRE_DATA_ARR):
                payload["data"][attr] = ""
        return payload

if __name__ == '__main__':
    ut.main()