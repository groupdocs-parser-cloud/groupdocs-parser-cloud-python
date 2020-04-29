# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="FieldData.py">
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

class FieldData(object):
    """
    Class for document field data.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'page_index': 'int',
        'page_area': 'PageArea',
        'linked_field': 'FieldData'
    }

    attribute_map = {
        'name': 'Name',
        'page_index': 'PageIndex',
        'page_area': 'PageArea',
        'linked_field': 'LinkedField'
    }

    def __init__(self, name=None, page_index=None, page_area=None, linked_field=None, **kwargs):  # noqa: E501
        """Initializes new instance of FieldData"""  # noqa: E501

        self._name = None
        self._page_index = None
        self._page_area = None
        self._linked_field = None

        if name is not None:
            self.name = name
        if page_index is not None:
            self.page_index = page_index
        if page_area is not None:
            self.page_area = page_area
        if linked_field is not None:
            self.linked_field = linked_field
    
    @property
    def name(self):
        """
        Gets the name.  # noqa: E501

        Gets or sets the field name.  # noqa: E501

        :return: The name.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name.

        Gets or sets the field name.  # noqa: E501

        :param name: The name.  # noqa: E501
        :type: str
        """
        self._name = name
    
    @property
    def page_index(self):
        """
        Gets the page_index.  # noqa: E501

        Gets or sets the index of the page.  # noqa: E501

        :return: The page_index.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index.

        Gets or sets the index of the page.  # noqa: E501

        :param page_index: The page_index.  # noqa: E501
        :type: int
        """
        if page_index is None:
            raise ValueError("Invalid value for `page_index`, must not be `None`")  # noqa: E501
        self._page_index = page_index
    
    @property
    def page_area(self):
        """
        Gets the page_area.  # noqa: E501

        Gets or sets the value of the field.  # noqa: E501

        :return: The page_area.  # noqa: E501
        :rtype: PageArea
        """
        return self._page_area

    @page_area.setter
    def page_area(self, page_area):
        """
        Sets the page_area.

        Gets or sets the value of the field.  # noqa: E501

        :param page_area: The page_area.  # noqa: E501
        :type: PageArea
        """
        self._page_area = page_area
    
    @property
    def linked_field(self):
        """
        Gets the linked_field.  # noqa: E501

        Gets or sets the linked data field.  # noqa: E501

        :return: The linked_field.  # noqa: E501
        :rtype: FieldData
        """
        return self._linked_field

    @linked_field.setter
    def linked_field(self, linked_field):
        """
        Sets the linked_field.

        Gets or sets the linked data field.  # noqa: E501

        :param linked_field: The linked_field.  # noqa: E501
        :type: FieldData
        """
        self._linked_field = linked_field

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
        if not isinstance(other, FieldData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
