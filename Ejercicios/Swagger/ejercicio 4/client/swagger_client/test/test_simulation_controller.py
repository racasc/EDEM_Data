# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_client.models.pool import Pool  # noqa: E501
from swagger_client.models.simulation import Simulation  # noqa: E501
from swagger_client.test import BaseTestCase


class TestSimulationController(BaseTestCase):
    """SimulationController integration test stubs"""

    def test_addpool(self):
        """Test case for addpool

        Add Pool to simulation
        """
        body = Pool()
        response = self.client.open(
            '/v2/addpool',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start(self):
        """Test case for start

        Start a simulation
        """
        body = Simulation()
        response = self.client.open(
            '/v2/start',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop(self):
        """Test case for stop

        Stop a simulation
        """
        response = self.client.open(
            '/v2/stop',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
