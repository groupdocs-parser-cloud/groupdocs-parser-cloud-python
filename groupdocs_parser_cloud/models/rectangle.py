# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Rectangle.py">
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

class Rectangle(object):
    """
    Rectangular area on the page.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'position': 'Point',
        'size': 'Size',
        'coordinates': 'Coordinates'
    }

    attribute_map = {
        'position': 'Position',
        'size': 'Size',
        'coordinates': 'Coordinates'
    }

    def __init__(self, position=None, size=None, coordinates=None, **kwargs):  # noqa: E501
        """Initializes new instance of Rectangle"""  # noqa: E501

        self._position = None
        self._size = None
        self._coordinates = None

        if position is not None:
            self.position = position
        if size is not None:
            self.size = size
        if coordinates is not None:
            self.coordinates = coordinates
    
    @property
    def position(self):
        """
        Gets the position.  # noqa: E501

        Gets the coordinates of the upper-left corner of the rectangular area.  # noqa: E501

        :return: The position.  # noqa: E501
        :rtype: Point
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position.

        Gets the coordinates of the upper-left corner of the rectangular area.  # noqa: E501

        :param position: The position.  # noqa: E501
        :type: Point
        """
        self._position = position
    
    @property
    def size(self):
        """
        Gets the size.  # noqa: E501

        Gets or sets the size of the rectangle.  # noqa: E501

        :return: The size.  # noqa: E501
        :rtype: Size
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size.

        Gets or sets the size of the rectangle.  # noqa: E501

        :param size: The size.  # noqa: E501
        :type: Size
        """
        self._size = size
    
    @property
    def coordinates(self):
        """
        Gets the coordinates.  # noqa: E501

        Gets or sets the coordinates.  # noqa: E501

        :return: The coordinates.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates.

        Gets or sets the coordinates.  # noqa: E501

        :param coordinates: The coordinates.  # noqa: E501
        :type: Coordinates
        """
        self._coordinates = coordinates

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
        if not isinstance(other, Rectangle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
