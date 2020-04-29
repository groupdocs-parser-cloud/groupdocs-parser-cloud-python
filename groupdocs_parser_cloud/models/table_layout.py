# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="TableLayout.py">
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

class TableLayout(object):
    """
    Provides the template table layout which is used by Table to define table position.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'vertical_separators': 'list[float]',
        'horizontal_separators': 'list[float]'
    }

    attribute_map = {
        'vertical_separators': 'VerticalSeparators',
        'horizontal_separators': 'HorizontalSeparators'
    }

    def __init__(self, vertical_separators=None, horizontal_separators=None, **kwargs):  # noqa: E501
        """Initializes new instance of TableLayout"""  # noqa: E501

        self._vertical_separators = None
        self._horizontal_separators = None

        if vertical_separators is not None:
            self.vertical_separators = vertical_separators
        if horizontal_separators is not None:
            self.horizontal_separators = horizontal_separators
    
    @property
    def vertical_separators(self):
        """
        Gets the vertical_separators.  # noqa: E501

        Gets or sets the table columns separators.  # noqa: E501

        :return: The vertical_separators.  # noqa: E501
        :rtype: list[float]
        """
        return self._vertical_separators

    @vertical_separators.setter
    def vertical_separators(self, vertical_separators):
        """
        Sets the vertical_separators.

        Gets or sets the table columns separators.  # noqa: E501

        :param vertical_separators: The vertical_separators.  # noqa: E501
        :type: list[float]
        """
        self._vertical_separators = vertical_separators
    
    @property
    def horizontal_separators(self):
        """
        Gets the horizontal_separators.  # noqa: E501

        Gets or sets the table rows separators.  # noqa: E501

        :return: The horizontal_separators.  # noqa: E501
        :rtype: list[float]
        """
        return self._horizontal_separators

    @horizontal_separators.setter
    def horizontal_separators(self, horizontal_separators):
        """
        Sets the horizontal_separators.

        Gets or sets the table rows separators.  # noqa: E501

        :param horizontal_separators: The horizontal_separators.  # noqa: E501
        :type: list[float]
        """
        self._horizontal_separators = horizontal_separators

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
        if not isinstance(other, TableLayout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
