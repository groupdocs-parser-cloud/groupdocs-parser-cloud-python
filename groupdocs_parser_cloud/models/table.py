# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Table.py">
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

class Table(object):
    """
    Document template table
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'table_name': 'str',
        'page_index': 'int',
        'detector_parameters': 'DetectorParameters',
        'table_layout': 'TableLayout'
    }

    attribute_map = {
        'table_name': 'TableName',
        'page_index': 'PageIndex',
        'detector_parameters': 'DetectorParameters',
        'table_layout': 'TableLayout'
    }

    def __init__(self, table_name=None, page_index=None, detector_parameters=None, table_layout=None, **kwargs):  # noqa: E501
        """Initializes new instance of Table"""  # noqa: E501

        self._table_name = None
        self._page_index = None
        self._detector_parameters = None
        self._table_layout = None

        if table_name is not None:
            self.table_name = table_name
        if page_index is not None:
            self.page_index = page_index
        if detector_parameters is not None:
            self.detector_parameters = detector_parameters
        if table_layout is not None:
            self.table_layout = table_layout
    
    @property
    def table_name(self):
        """
        Gets the table_name.  # noqa: E501

        Gets or sets a unique template table name.  # noqa: E501

        :return: The table_name.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name.

        Gets or sets a unique template table name.  # noqa: E501

        :param table_name: The table_name.  # noqa: E501
        :type: str
        """
        self._table_name = table_name
    
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
    def detector_parameters(self):
        """
        Gets the detector_parameters.  # noqa: E501

        Gets or sets the detector parameters. Provides parameters for the table detection algorithms.   # noqa: E501

        :return: The detector_parameters.  # noqa: E501
        :rtype: DetectorParameters
        """
        return self._detector_parameters

    @detector_parameters.setter
    def detector_parameters(self, detector_parameters):
        """
        Sets the detector_parameters.

        Gets or sets the detector parameters. Provides parameters for the table detection algorithms.   # noqa: E501

        :param detector_parameters: The detector_parameters.  # noqa: E501
        :type: DetectorParameters
        """
        self._detector_parameters = detector_parameters
    
    @property
    def table_layout(self):
        """
        Gets the table_layout.  # noqa: E501

        Gets or sets the table layout. Provides the template table layout which is used by Table to define table position.  # noqa: E501

        :return: The table_layout.  # noqa: E501
        :rtype: TableLayout
        """
        return self._table_layout

    @table_layout.setter
    def table_layout(self, table_layout):
        """
        Sets the table_layout.

        Gets or sets the table layout. Provides the template table layout which is used by Table to define table position.  # noqa: E501

        :param table_layout: The table_layout.  # noqa: E501
        :type: TableLayout
        """
        self._table_layout = table_layout

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
        if not isinstance(other, Table):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
