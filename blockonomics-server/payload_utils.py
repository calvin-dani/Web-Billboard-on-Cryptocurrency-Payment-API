

#Status of transaction and proceed map
STATUS_ORDER = {'2': True, '1': False, '0': False}

IMPORTANT_ATTR = {
    "uuid", "address", "name", "emailid", "Message", "paid_satoshi", "timestamp"
}

ARRE_DATA_ARR = {"name", "emailid", "Message"}

# Returns boolean based on webhooks transaction status
def return_status(status):
    if status in STATUS_ORDER:
        return STATUS_ORDER[status]
    else:
        return False

# Parses from blockonomics
def parse_transaction_payload(payload):
    data = {}
    for attr in IMPORTANT_ATTR:
        try:
            data[attr] = get_payload_attr(payload, attr, attr in ARRE_DATA_ARR)
        except Exception as e:
            data[attr] = ""
            print(e)
        else:
            continue
    return data

# Flattens the response with the transaction details from bloconomics
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

