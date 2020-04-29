# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Coordinates.py">
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

class Coordinates(object):
    """
    Class for rectangle coordinates.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'top': 'float',
        'bottom': 'float',
        'left': 'float',
        'right': 'float'
    }

    attribute_map = {
        'top': 'Top',
        'bottom': 'Bottom',
        'left': 'Left',
        'right': 'Right'
    }

    def __init__(self, top=None, bottom=None, left=None, right=None, **kwargs):  # noqa: E501
        """Initializes new instance of Coordinates"""  # noqa: E501

        self._top = None
        self._bottom = None
        self._left = None
        self._right = None

        if top is not None:
            self.top = top
        if bottom is not None:
            self.bottom = bottom
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
    
    @property
    def top(self):
        """
        Gets the top.  # noqa: E501

        Gets or sets the y-coordinate of the top edge of the rectangular area.  # noqa: E501

        :return: The top.  # noqa: E501
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """
        Sets the top.

        Gets or sets the y-coordinate of the top edge of the rectangular area.  # noqa: E501

        :param top: The top.  # noqa: E501
        :type: float
        """
        if top is None:
            raise ValueError("Invalid value for `top`, must not be `None`")  # noqa: E501
        self._top = top
    
    @property
    def bottom(self):
        """
        Gets the bottom.  # noqa: E501

        Gets or sets the y-coordinate of the bottom edge of the rectangular area.  # noqa: E501

        :return: The bottom.  # noqa: E501
        :rtype: float
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """
        Sets the bottom.

        Gets or sets the y-coordinate of the bottom edge of the rectangular area.  # noqa: E501

        :param bottom: The bottom.  # noqa: E501
        :type: float
        """
        if bottom is None:
            raise ValueError("Invalid value for `bottom`, must not be `None`")  # noqa: E501
        self._bottom = bottom
    
    @property
    def left(self):
        """
        Gets the left.  # noqa: E501

        Gets or sets the x-coordinate of the left edge of the rectangular area.  # noqa: E501

        :return: The left.  # noqa: E501
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """
        Sets the left.

        Gets or sets the x-coordinate of the left edge of the rectangular area.  # noqa: E501

        :param left: The left.  # noqa: E501
        :type: float
        """
        if left is None:
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501
        self._left = left
    
    @property
    def right(self):
        """
        Gets the right.  # noqa: E501

        Gets or sets the x-coordinate of the right edge of the rectangular area.  # noqa: E501

        :return: The right.  # noqa: E501
        :rtype: float
        """
        return self._right

    @right.setter
    def right(self, right):
        """
        Sets the right.

        Gets or sets the x-coordinate of the right edge of the rectangular area.  # noqa: E501

        :param right: The right.  # noqa: E501
        :type: float
        """
        if right is None:
            raise ValueError("Invalid value for `right`, must not be `None`")  # noqa: E501
        self._right = right

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
        if not isinstance(other, Coordinates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
