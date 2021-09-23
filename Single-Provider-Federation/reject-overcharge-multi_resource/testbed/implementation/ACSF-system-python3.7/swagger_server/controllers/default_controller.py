import connexion
import six

from swagger_server.models.ac_request import ACRequest  # noqa: E501
from swagger_server.models.ac_response import ACResponse  # noqa: E501
from swagger_server import util

from swagger_server.core.lookup import random_valid_action

def a_c_comp_get():  # noqa: E501
    """ping the algorithm

    Check the alive status of the algorithm # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def a_c_comp_post(body):  # noqa: E501
    """Request for execution of the admission controller algorithm.

    By this API, the caller provides all the required information for the admission controller algorithm. # noqa: E501

    :param body: Admission control request information.
    :type body: dict | bytes

    :rtype: ACResponse
    """
    if connexion.request.is_json:
        body = ACRequest.from_dict(connexion.request.get_json())  # noqa: E501
        #print("\n\nBody = \n", body)

    action = random_valid_action(body.nsd, body.actives, body.available)
    print("action = ", action)
    
    if action["domainid"] == "null":
        return ACResponse(reject = True, domain = "null"), 200
    else:
        return ACResponse(reject = False, domain = action["domainid"]), 200
