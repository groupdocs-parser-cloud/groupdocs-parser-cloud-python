# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PageTableAreaCell.py">
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

class PageTableAreaCell(object):
    """
    Represents a table cell.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'column_index': 'int',
        'column_span': 'int',
        'page_area': 'PageArea',
        'row_index': 'int',
        'row_span': 'int'
    }

    attribute_map = {
        'column_index': 'ColumnIndex',
        'column_span': 'ColumnSpan',
        'page_area': 'PageArea',
        'row_index': 'RowIndex',
        'row_span': 'RowSpan'
    }

    def __init__(self, column_index=None, column_span=None, page_area=None, row_index=None, row_span=None, **kwargs):  # noqa: E501
        """Initializes new instance of PageTableAreaCell"""  # noqa: E501

        self._column_index = None
        self._column_span = None
        self._page_area = None
        self._row_index = None
        self._row_span = None

        if column_index is not None:
            self.column_index = column_index
        if column_span is not None:
            self.column_span = column_span
        if page_area is not None:
            self.page_area = page_area
        if row_index is not None:
            self.row_index = row_index
        if row_span is not None:
            self.row_span = row_span
    
    @property
    def column_index(self):
        """
        Gets the column_index.  # noqa: E501

        Gets or sets the index of the column.  # noqa: E501

        :return: The column_index.  # noqa: E501
        :rtype: int
        """
        return self._column_index

    @column_index.setter
    def column_index(self, column_index):
        """
        Sets the column_index.

        Gets or sets the index of the column.  # noqa: E501

        :param column_index: The column_index.  # noqa: E501
        :type: int
        """
        if column_index is None:
            raise ValueError("Invalid value for `column_index`, must not be `None`")  # noqa: E501
        self._column_index = column_index
    
    @property
    def column_span(self):
        """
        Gets the column_span.  # noqa: E501

        Gets or sets the total number of columns that contain the table cell.  # noqa: E501

        :return: The column_span.  # noqa: E501
        :rtype: int
        """
        return self._column_span

    @column_span.setter
    def column_span(self, column_span):
        """
        Sets the column_span.

        Gets or sets the total number of columns that contain the table cell.  # noqa: E501

        :param column_span: The column_span.  # noqa: E501
        :type: int
        """
        if column_span is None:
            raise ValueError("Invalid value for `column_span`, must not be `None`")  # noqa: E501
        self._column_span = column_span
    
    @property
    def page_area(self):
        """
        Gets the page_area.  # noqa: E501

        Gets or sets the table cell value.  # noqa: E501

        :return: The page_area.  # noqa: E501
        :rtype: PageArea
        """
        return self._page_area

    @page_area.setter
    def page_area(self, page_area):
        """
        Sets the page_area.

        Gets or sets the table cell value.  # noqa: E501

        :param page_area: The page_area.  # noqa: E501
        :type: PageArea
        """
        self._page_area = page_area
    
    @property
    def row_index(self):
        """
        Gets the row_index.  # noqa: E501

        Gets or sets the index of the row.  # noqa: E501

        :return: The row_index.  # noqa: E501
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """
        Sets the row_index.

        Gets or sets the index of the row.  # noqa: E501

        :param row_index: The row_index.  # noqa: E501
        :type: int
        """
        if row_index is None:
            raise ValueError("Invalid value for `row_index`, must not be `None`")  # noqa: E501
        self._row_index = row_index
    
    @property
    def row_span(self):
        """
        Gets the row_span.  # noqa: E501

        Gets or sets the total number of rows that contain the table cell.  # noqa: E501

        :return: The row_span.  # noqa: E501
        :rtype: int
        """
        return self._row_span

    @row_span.setter
    def row_span(self, row_span):
        """
        Sets the row_span.

        Gets or sets the total number of rows that contain the table cell.  # noqa: E501

        :param row_span: The row_span.  # noqa: E501
        :type: int
        """
        if row_span is None:
            raise ValueError("Invalid value for `row_span`, must not be `None`")  # noqa: E501
        self._row_span = row_span

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
        if not isinstance(other, PageTableAreaCell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
