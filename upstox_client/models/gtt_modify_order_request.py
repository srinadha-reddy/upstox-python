# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GttModifyOrderRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'quantity': 'int',
        'rules': 'list[GttRule]',
        'gtt_order_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'quantity': 'quantity',
        'rules': 'rules',
        'gtt_order_id': 'gtt_order_id'
    }

    def __init__(self, type=None, quantity=None, rules=None, gtt_order_id=None):  # noqa: E501
        """GttModifyOrderRequest - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._quantity = None
        self._rules = None
        self._gtt_order_id = None
        self.discriminator = None
        self.type = type
        self.quantity = quantity
        self.rules = rules
        self.gtt_order_id = gtt_order_id

    @property
    def type(self):
        """Gets the type of this GttModifyOrderRequest.  # noqa: E501

        Type of GTT order. It can be one of the following: SINGLE refers to a single-leg GTT order MULTIPLE refers to a multi-leg GTT order  # noqa: E501

        :return: The type of this GttModifyOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GttModifyOrderRequest.

        Type of GTT order. It can be one of the following: SINGLE refers to a single-leg GTT order MULTIPLE refers to a multi-leg GTT order  # noqa: E501

        :param type: The type of this GttModifyOrderRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["SINGLE", "MULTIPLE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def quantity(self):
        """Gets the quantity of this GttModifyOrderRequest.  # noqa: E501

        Quantity with which the order is to be placed  # noqa: E501

        :return: The quantity of this GttModifyOrderRequest.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GttModifyOrderRequest.

        Quantity with which the order is to be placed  # noqa: E501

        :param quantity: The quantity of this GttModifyOrderRequest.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def rules(self):
        """Gets the rules of this GttModifyOrderRequest.  # noqa: E501

        List of rules defining the conditions for each leg in the GTT order  # noqa: E501

        :return: The rules of this GttModifyOrderRequest.  # noqa: E501
        :rtype: list[GttRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this GttModifyOrderRequest.

        List of rules defining the conditions for each leg in the GTT order  # noqa: E501

        :param rules: The rules of this GttModifyOrderRequest.  # noqa: E501
        :type: list[GttRule]
        """
        if rules is None:
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

    @property
    def gtt_order_id(self):
        """Gets the gtt_order_id of this GttModifyOrderRequest.  # noqa: E501

        Unique identifier of the GTT order to be modified  # noqa: E501

        :return: The gtt_order_id of this GttModifyOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._gtt_order_id

    @gtt_order_id.setter
    def gtt_order_id(self, gtt_order_id):
        """Sets the gtt_order_id of this GttModifyOrderRequest.

        Unique identifier of the GTT order to be modified  # noqa: E501

        :param gtt_order_id: The gtt_order_id of this GttModifyOrderRequest.  # noqa: E501
        :type: str
        """
        if gtt_order_id is None:
            raise ValueError("Invalid value for `gtt_order_id`, must not be `None`")  # noqa: E501

        self._gtt_order_id = gtt_order_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GttModifyOrderRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GttModifyOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
