# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PageTableArea.py">
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

class PageTableArea(object):
    """
    Represents a table page area which is used to represent a table in the parsing by template functionality.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'row_count': 'int',
        'column_count': 'int',
        'page_table_area_cells': 'list[PageTableAreaCell]'
    }

    attribute_map = {
        'row_count': 'RowCount',
        'column_count': 'ColumnCount',
        'page_table_area_cells': 'PageTableAreaCells'
    }

    def __init__(self, row_count=None, column_count=None, page_table_area_cells=None, **kwargs):  # noqa: E501
        """Initializes new instance of PageTableArea"""  # noqa: E501

        self._row_count = None
        self._column_count = None
        self._page_table_area_cells = None

        if row_count is not None:
            self.row_count = row_count
        if column_count is not None:
            self.column_count = column_count
        if page_table_area_cells is not None:
            self.page_table_area_cells = page_table_area_cells
    
    @property
    def row_count(self):
        """
        Gets the row_count.  # noqa: E501

        Gets or sets the total number of the table rows.  # noqa: E501

        :return: The row_count.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """
        Sets the row_count.

        Gets or sets the total number of the table rows.  # noqa: E501

        :param row_count: The row_count.  # noqa: E501
        :type: int
        """
        if row_count is None:
            raise ValueError("Invalid value for `row_count`, must not be `None`")  # noqa: E501
        self._row_count = row_count
    
    @property
    def column_count(self):
        """
        Gets the column_count.  # noqa: E501

        Gets or sets the total number of the table columns.  # noqa: E501

        :return: The column_count.  # noqa: E501
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        """
        Sets the column_count.

        Gets or sets the total number of the table columns.  # noqa: E501

        :param column_count: The column_count.  # noqa: E501
        :type: int
        """
        if column_count is None:
            raise ValueError("Invalid value for `column_count`, must not be `None`")  # noqa: E501
        self._column_count = column_count
    
    @property
    def page_table_area_cells(self):
        """
        Gets the page_table_area_cells.  # noqa: E501

        Gets or sets the collection of table area cell.  # noqa: E501

        :return: The page_table_area_cells.  # noqa: E501
        :rtype: list[PageTableAreaCell]
        """
        return self._page_table_area_cells

    @page_table_area_cells.setter
    def page_table_area_cells(self, page_table_area_cells):
        """
        Sets the page_table_area_cells.

        Gets or sets the collection of table area cell.  # noqa: E501

        :param page_table_area_cells: The page_table_area_cells.  # noqa: E501
        :type: list[PageTableAreaCell]
        """
        self._page_table_area_cells = page_table_area_cells

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
        if not isinstance(other, PageTableArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
