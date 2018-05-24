#!/usr/bin/python
#coding: utf-8
#(c) 2017 Ramses Carbajal <@RamsesCarbajal>
from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_payee_create(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        payee = self.client.Payee.create(self.payee_object.copy())
        transfer_request_body = self.transfer_object.copy()
        transfer_request_body['payee_id'] = payee.id

        transfer = self.client.Transfer.create(transfer_request_body)

        assert transfer.status == 'pending'
