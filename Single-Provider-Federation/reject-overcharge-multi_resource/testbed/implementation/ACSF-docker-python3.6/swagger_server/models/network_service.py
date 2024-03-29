# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.sap import SAP  # noqa: F401,E501
from swagger_server.models.vnf import VNF  # noqa: F401,E501
from swagger_server.models.vnf_link import VNFLink  # noqa: F401,E501
from swagger_server import util


class NetworkService(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, vn_fs: List[VNF]=None, vnf_links: List[VNFLink]=None, sap: List[SAP]=None, max_latency: float=None, target_availability: float=None, max_cost: float=None):  # noqa: E501
        """NetworkService - a model defined in Swagger

        :param id: The id of this NetworkService.  # noqa: E501
        :type id: str
        :param name: The name of this NetworkService.  # noqa: E501
        :type name: str
        :param vn_fs: The vn_fs of this NetworkService.  # noqa: E501
        :type vn_fs: List[VNF]
        :param vnf_links: The vnf_links of this NetworkService.  # noqa: E501
        :type vnf_links: List[VNFLink]
        :param sap: The sap of this NetworkService.  # noqa: E501
        :type sap: List[SAP]
        :param max_latency: The max_latency of this NetworkService.  # noqa: E501
        :type max_latency: float
        :param target_availability: The target_availability of this NetworkService.  # noqa: E501
        :type target_availability: float
        :param max_cost: The max_cost of this NetworkService.  # noqa: E501
        :type max_cost: float
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'vn_fs': List[VNF],
            'vnf_links': List[VNFLink],
            'sap': List[SAP],
            'max_latency': float,
            'target_availability': float,
            'max_cost': float
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'vn_fs': 'VNFs',
            'vnf_links': 'VNFLinks',
            'sap': 'SAP',
            'max_latency': 'max_latency',
            'target_availability': 'target_availability',
            'max_cost': 'max_cost'
        }
        self._id = id
        self._name = name
        self._vn_fs = vn_fs
        self._vnf_links = vnf_links
        self._sap = sap
        self._max_latency = max_latency
        self._target_availability = target_availability
        self._max_cost = max_cost

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NetworkService of this NetworkService.  # noqa: E501
        :rtype: NetworkService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this NetworkService.

        Network service identifier  # noqa: E501

        :return: The id of this NetworkService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this NetworkService.

        Network service identifier  # noqa: E501

        :param id: The id of this NetworkService.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this NetworkService.

        Name of the network service  # noqa: E501

        :return: The name of this NetworkService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this NetworkService.

        Name of the network service  # noqa: E501

        :param name: The name of this NetworkService.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def vn_fs(self) -> List[VNF]:
        """Gets the vn_fs of this NetworkService.

        VNFs composing the service  # noqa: E501

        :return: The vn_fs of this NetworkService.
        :rtype: List[VNF]
        """
        return self._vn_fs

    @vn_fs.setter
    def vn_fs(self, vn_fs: List[VNF]):
        """Sets the vn_fs of this NetworkService.

        VNFs composing the service  # noqa: E501

        :param vn_fs: The vn_fs of this NetworkService.
        :type vn_fs: List[VNF]
        """

        self._vn_fs = vn_fs

    @property
    def vnf_links(self) -> List[VNFLink]:
        """Gets the vnf_links of this NetworkService.

        Edges of the VNFFG  # noqa: E501

        :return: The vnf_links of this NetworkService.
        :rtype: List[VNFLink]
        """
        return self._vnf_links

    @vnf_links.setter
    def vnf_links(self, vnf_links: List[VNFLink]):
        """Sets the vnf_links of this NetworkService.

        Edges of the VNFFG  # noqa: E501

        :param vnf_links: The vnf_links of this NetworkService.
        :type vnf_links: List[VNFLink]
        """

        self._vnf_links = vnf_links

    @property
    def sap(self) -> List[SAP]:
        """Gets the sap of this NetworkService.


        :return: The sap of this NetworkService.
        :rtype: List[SAP]
        """
        return self._sap

    @sap.setter
    def sap(self, sap: List[SAP]):
        """Sets the sap of this NetworkService.


        :param sap: The sap of this NetworkService.
        :type sap: List[SAP]
        """

        self._sap = sap

    @property
    def max_latency(self) -> float:
        """Gets the max_latency of this NetworkService.

        End-to-end latency constraint.  # noqa: E501

        :return: The max_latency of this NetworkService.
        :rtype: float
        """
        return self._max_latency

    @max_latency.setter
    def max_latency(self, max_latency: float):
        """Sets the max_latency of this NetworkService.

        End-to-end latency constraint.  # noqa: E501

        :param max_latency: The max_latency of this NetworkService.
        :type max_latency: float
        """

        self._max_latency = max_latency

    @property
    def target_availability(self) -> float:
        """Gets the target_availability of this NetworkService.

        Target service availability.  # noqa: E501

        :return: The target_availability of this NetworkService.
        :rtype: float
        """
        return self._target_availability

    @target_availability.setter
    def target_availability(self, target_availability: float):
        """Sets the target_availability of this NetworkService.

        Target service availability.  # noqa: E501

        :param target_availability: The target_availability of this NetworkService.
        :type target_availability: float
        """

        self._target_availability = target_availability

    @property
    def max_cost(self) -> float:
        """Gets the max_cost of this NetworkService.

        Cost/budget constraint  # noqa: E501

        :return: The max_cost of this NetworkService.
        :rtype: float
        """
        return self._max_cost

    @max_cost.setter
    def max_cost(self, max_cost: float):
        """Sets the max_cost of this NetworkService.

        Cost/budget constraint  # noqa: E501

        :param max_cost: The max_cost of this NetworkService.
        :type max_cost: float
        """

        self._max_cost = max_cost
