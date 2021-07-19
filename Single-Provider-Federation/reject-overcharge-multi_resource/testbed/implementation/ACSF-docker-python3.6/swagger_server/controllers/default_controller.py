import connexion
import six
import logging
import sys

from swagger_server.models.ac_request import ACRequest  # noqa: E501
from swagger_server.models.ac_response import ACResponse  # noqa: E501
from swagger_server import util

import swagger_server.core.learned_policy as learned_policy

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
   
    logging.debug("\n\nBody = %s", body)
    
    action = learned_policy.lookup(body)

    if action == "reject":
        return ACResponse(reject = True, domain = "null"), 200
    elif action == "accept":
        return ACResponse(reject = False, domain = "local"), 200
    elif action == "federate":
        return ACResponse(reject = False, domain = "Provider1"), 200
    else:
        logging.error("unknown action")
        sys.exit(-1)

