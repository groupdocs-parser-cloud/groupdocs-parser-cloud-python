# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Field.py">
#   Copyright (c) 2003-2019 Aspose Pty Ltd
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

import pprint
import re  # noqa: F401

import six

class Field(object):
    """
    Field of document template
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field_name': 'str',
        'page_index': 'int',
        'field_position': 'FieldPosition'
    }

    attribute_map = {
        'field_name': 'FieldName',
        'page_index': 'PageIndex',
        'field_position': 'FieldPosition'
    }

    def __init__(self, field_name=None, page_index=None, field_position=None, **kwargs):  # noqa: E501
        """Initializes new instance of Field"""  # noqa: E501

        self._field_name = None
        self._page_index = None
        self._field_position = None

        if field_name is not None:
            self.field_name = field_name
        if page_index is not None:
            self.page_index = page_index
        if field_position is not None:
            self.field_position = field_position
    
    @property
    def field_name(self):
        """
        Gets the field_name.  # noqa: E501

        A unique template field name.  # noqa: E501

        :return: The field_name.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name.

        A unique template field name.  # noqa: E501

        :param field_name: The field_name.  # noqa: E501
        :type: str
        """
        self._field_name = field_name
    
    @property
    def page_index(self):
        """
        Gets the page_index.  # noqa: E501

        The page index. An integer value that represents the index of the page where the template item is located; null if the template item is located on any page.  # noqa: E501

        :return: The page_index.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index.

        The page index. An integer value that represents the index of the page where the template item is located; null if the template item is located on any page.  # noqa: E501

        :param page_index: The page_index.  # noqa: E501
        :type: int
        """
        self._page_index = page_index
    
    @property
    def field_position(self):
        """
        Gets the field_position.  # noqa: E501

        Defines the way how to find the field on a page.  # noqa: E501

        :return: The field_position.  # noqa: E501
        :rtype: FieldPosition
        """
        return self._field_position

    @field_position.setter
    def field_position(self, field_position):
        """
        Sets the field_position.

        Defines the way how to find the field on a page.  # noqa: E501

        :param field_position: The field_position.  # noqa: E501
        :type: FieldPosition
        """
        self._field_position = field_position

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
