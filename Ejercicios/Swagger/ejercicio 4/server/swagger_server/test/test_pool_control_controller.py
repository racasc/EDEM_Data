# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPoolControlController(BaseTestCase):
    """PoolControlController integration test stubs"""

    def test_getinfo(self,id):
        """Test case for getinfo

        Get information of the pool
        """
        response = self.client.open(
            '/v2/getInfo',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
