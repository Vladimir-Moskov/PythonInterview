"""
    Run requests to test local applications
"""

import requests

# api-endpoint
URL = "http://127.0.0.1:5001/cashcogXCNT/api/v1/expense"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
data_json = {
    'created_at': '2019-12-03T16:35:04',
    'currency': 'NAD',
    'approve_state': 0,
    'uuid': '5e9c5b37-1944-4986-a089-4298fe68f387',
    'id': 2,
    'approved_by': None,
    'employee': 3,
    'amount': 9087.0,
    'approved_datetime': None,
    'description': 'Consectetur culpa qui repudiandae cum consequatur.'
}
URL = "http://127.0.0.1:5001/cashcogXCNT/api/v1/expense/1/approve"
data_json = {
    "user": 'user1',
    'approve': 'APPROVED'
}
# sending get request and saving the response as response object
request_self = requests.put(url=URL, json=data_json)
print(request_self)
