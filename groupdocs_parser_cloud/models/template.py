# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Template.py">
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

class Template(object):
    """
    User-generated template to extract metadata from the document.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fields': 'list[Field]',
        'tables': 'list[Table]'
    }

    attribute_map = {
        'fields': 'Fields',
        'tables': 'Tables'
    }

    def __init__(self, fields=None, tables=None, **kwargs):  # noqa: E501
        """Initializes new instance of Template"""  # noqa: E501

        self._fields = None
        self._tables = None

        if fields is not None:
            self.fields = fields
        if tables is not None:
            self.tables = tables
    
    @property
    def fields(self):
        """
        Gets the fields.  # noqa: E501

        Template fields.  # noqa: E501

        :return: The fields.  # noqa: E501
        :rtype: list[Field]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields.

        Template fields.  # noqa: E501

        :param fields: The fields.  # noqa: E501
        :type: list[Field]
        """
        self._fields = fields
    
    @property
    def tables(self):
        """
        Gets the tables.  # noqa: E501

        Template tables.  # noqa: E501

        :return: The tables.  # noqa: E501
        :rtype: list[Table]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """
        Sets the tables.

        Template tables.  # noqa: E501

        :param tables: The tables.  # noqa: E501
        :type: list[Table]
        """
        self._tables = tables

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
        if not isinstance(other, Template):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
