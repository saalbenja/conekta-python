#!/usr/bin/python
#coding: utf-8
#(c) 2017 Ramses Carbajal <@RamsesCarbajal>
from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_payee_create(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        payee = self.client.Payee.create(self.payee_object.copy())
        destination = payee.destinations[0]

        assert payee.name  == 'Graydon Creed'
        assert payee.email == 'graydon@friendsofhumanity.com'
        assert payee.phone == '5555555555'
        assert destination.last4 == self.payee_object['destinations'][0]['account_number'][-4:]
        assert destination.account_holder_name == self.payee_object['destinations'][0]['account_holder_name']

    def test_02_payee_add_token(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        payee_params = self.payee_object.copy()
        del payee_params["destinations"]
        payee = self.client.Payee.create(payee_params)
        destination = payee.createDestination(self.destination_object.copy())

        assert destination.last4 == self.destination_object['account_number'][-4:]
        assert destination.account_holder_name == self.destination_object['account_holder_name']

    def test_03_payee_update_destination(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        payee = self.client.Payee.create(self.payee_object.copy())
        destination = payee.destinations[0]
        destination.update(self.destination_object.copy())
        destination = payee.destinations[0]

        assert destination.last4 == self.destination_object['account_number'][-4:]
        assert destination.account_holder_name == self.destination_object['account_holder_name']

    def test_04_payee_delete_destination(self):
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        payee = self.client.Payee.create(self.payee_object.copy())
        destination = payee.destinations[0]

        destination_deleted = destination.delete()

        assert destination_deleted.deleted == True
