# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.ac_request import ACRequest  # noqa: E501
from swagger_server.models.ac_response import ACResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_a_c_comp_get(self):
        """Test case for a_c_comp_get

        ping the algorithm
        """
        response = self.client.open(
            '/AC',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_a_c_comp_post(self):
        """Test case for a_c_comp_post

        Request for execution of the admission controller algorithm.
        """
        body = ACRequest()
        response = self.client.open(
            '/AC',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
