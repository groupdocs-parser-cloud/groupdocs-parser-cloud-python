# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="DetectorParameters.py">
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

class DetectorParameters(object):
    """
    Provides parameters for the table detection algorithms. 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'min_row_count': 'int',
        'min_column_count': 'int',
        'min_vertical_space': 'int',
        'has_merged_cells': 'bool',
        'rectangle': 'Rectangle',
        'vertical_separators': 'list[float]'
    }

    attribute_map = {
        'min_row_count': 'MinRowCount',
        'min_column_count': 'MinColumnCount',
        'min_vertical_space': 'MinVerticalSpace',
        'has_merged_cells': 'HasMergedCells',
        'rectangle': 'Rectangle',
        'vertical_separators': 'VerticalSeparators'
    }

    def __init__(self, min_row_count=None, min_column_count=None, min_vertical_space=None, has_merged_cells=None, rectangle=None, vertical_separators=None, **kwargs):  # noqa: E501
        """Initializes new instance of DetectorParameters"""  # noqa: E501

        self._min_row_count = None
        self._min_column_count = None
        self._min_vertical_space = None
        self._has_merged_cells = None
        self._rectangle = None
        self._vertical_separators = None

        if min_row_count is not None:
            self.min_row_count = min_row_count
        if min_column_count is not None:
            self.min_column_count = min_column_count
        if min_vertical_space is not None:
            self.min_vertical_space = min_vertical_space
        if has_merged_cells is not None:
            self.has_merged_cells = has_merged_cells
        if rectangle is not None:
            self.rectangle = rectangle
        if vertical_separators is not None:
            self.vertical_separators = vertical_separators
    
    @property
    def min_row_count(self):
        """
        Gets the min_row_count.  # noqa: E501

        Gets or sets the minimum number of the table rows.  # noqa: E501

        :return: The min_row_count.  # noqa: E501
        :rtype: int
        """
        return self._min_row_count

    @min_row_count.setter
    def min_row_count(self, min_row_count):
        """
        Sets the min_row_count.

        Gets or sets the minimum number of the table rows.  # noqa: E501

        :param min_row_count: The min_row_count.  # noqa: E501
        :type: int
        """
        self._min_row_count = min_row_count
    
    @property
    def min_column_count(self):
        """
        Gets the min_column_count.  # noqa: E501

        Gets or sets the minimum number of the table columns.  # noqa: E501

        :return: The min_column_count.  # noqa: E501
        :rtype: int
        """
        return self._min_column_count

    @min_column_count.setter
    def min_column_count(self, min_column_count):
        """
        Sets the min_column_count.

        Gets or sets the minimum number of the table columns.  # noqa: E501

        :param min_column_count: The min_column_count.  # noqa: E501
        :type: int
        """
        self._min_column_count = min_column_count
    
    @property
    def min_vertical_space(self):
        """
        Gets the min_vertical_space.  # noqa: E501

        Gets or sets the minimum space between the table columns.  # noqa: E501

        :return: The min_vertical_space.  # noqa: E501
        :rtype: int
        """
        return self._min_vertical_space

    @min_vertical_space.setter
    def min_vertical_space(self, min_vertical_space):
        """
        Sets the min_vertical_space.

        Gets or sets the minimum space between the table columns.  # noqa: E501

        :param min_vertical_space: The min_vertical_space.  # noqa: E501
        :type: int
        """
        self._min_vertical_space = min_vertical_space
    
    @property
    def has_merged_cells(self):
        """
        Gets the has_merged_cells.  # noqa: E501

        Gets or sets the value that indicates whether the table has merged cells.  # noqa: E501

        :return: The has_merged_cells.  # noqa: E501
        :rtype: bool
        """
        return self._has_merged_cells

    @has_merged_cells.setter
    def has_merged_cells(self, has_merged_cells):
        """
        Sets the has_merged_cells.

        Gets or sets the value that indicates whether the table has merged cells.  # noqa: E501

        :param has_merged_cells: The has_merged_cells.  # noqa: E501
        :type: bool
        """
        self._has_merged_cells = has_merged_cells
    
    @property
    def rectangle(self):
        """
        Gets the rectangle.  # noqa: E501

        Gets or sets the rectangular area that contains the table.  # noqa: E501

        :return: The rectangle.  # noqa: E501
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle.

        Gets or sets the rectangular area that contains the table.  # noqa: E501

        :param rectangle: The rectangle.  # noqa: E501
        :type: Rectangle
        """
        self._rectangle = rectangle
    
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
        if not isinstance(other, DetectorParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
