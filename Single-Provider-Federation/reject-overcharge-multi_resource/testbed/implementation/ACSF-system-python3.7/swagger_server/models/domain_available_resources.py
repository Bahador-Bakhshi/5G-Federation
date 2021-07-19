# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DomainAvailableResources(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, domainid: str=None, cpu: float=None, ram: float=None):  # noqa: E501
        """DomainAvailableResources - a model defined in Swagger

        :param domainid: The domainid of this DomainAvailableResources.  # noqa: E501
        :type domainid: str
        :param cpu: The cpu of this DomainAvailableResources.  # noqa: E501
        :type cpu: float
        :param ram: The ram of this DomainAvailableResources.  # noqa: E501
        :type ram: float
        """
        self.swagger_types = {
            'domainid': str,
            'cpu': float,
            'ram': float
        }

        self.attribute_map = {
            'domainid': 'domainid',
            'cpu': 'cpu',
            'ram': 'ram'
        }
        self._domainid = domainid
        self._cpu = cpu
        self._ram = ram

    @classmethod
    def from_dict(cls, dikt) -> 'DomainAvailableResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DomainAvailableResources of this DomainAvailableResources.  # noqa: E501
        :rtype: DomainAvailableResources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domainid(self) -> str:
        """Gets the domainid of this DomainAvailableResources.

        The id of the domain  # noqa: E501

        :return: The domainid of this DomainAvailableResources.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid: str):
        """Sets the domainid of this DomainAvailableResources.

        The id of the domain  # noqa: E501

        :param domainid: The domainid of this DomainAvailableResources.
        :type domainid: str
        """
        if domainid is None:
            raise ValueError("Invalid value for `domainid`, must not be `None`")  # noqa: E501

        self._domainid = domainid

    @property
    def cpu(self) -> float:
        """Gets the cpu of this DomainAvailableResources.

        The number of available CPUs  # noqa: E501

        :return: The cpu of this DomainAvailableResources.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu: float):
        """Sets the cpu of this DomainAvailableResources.

        The number of available CPUs  # noqa: E501

        :param cpu: The cpu of this DomainAvailableResources.
        :type cpu: float
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def ram(self) -> float:
        """Gets the ram of this DomainAvailableResources.

        The amount of available RAM  # noqa: E501

        :return: The ram of this DomainAvailableResources.
        :rtype: float
        """
        return self._ram

    @ram.setter
    def ram(self, ram: float):
        """Sets the ram of this DomainAvailableResources.

        The amount of available RAM  # noqa: E501

        :param ram: The ram of this DomainAvailableResources.
        :type ram: float
        """
        if ram is None:
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501

        self._ram = ram
