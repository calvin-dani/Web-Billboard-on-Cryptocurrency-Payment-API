

#Status of transaction and proceed map
status_order = {'2': True, '1': False, '0': False}

important_attr = {
    "uuid", "address", "name", "emailid", "Message", "paid_satoshi", "timestamp"
}

attr_data_arr = {"name", "emailid", "Message"}


def return_status(status):
    if status in status_order:
        return status_order[status]
    else:
        return False

def parse_transaction_payload(payload):
    data = {}
    for attr in important_attr:
        try:
            data[attr] = get_payload_attr(payload, attr, attr in attr_data_arr)
        except Exception as e:
            data[attr] = ""
            print(e)
        else:
            continue
    return data


def get_payload_attr(payload, attr, data_arr_req=False):
    if attr in payload and not data_arr_req:
        return payload[attr]
    elif "data"  in payload and data_arr_req:
        if attr in payload['data']:
            return payload["data"][attr]
        else:
            raise Exception("Attribute missing, Unable to view message")
    else:
        raise Exception("Attribute missing, Unable to view message")

