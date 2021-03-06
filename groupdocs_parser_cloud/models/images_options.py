# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ImagesOptions.py">
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

from groupdocs_parser_cloud.models import ParserOptions

class ImagesOptions(ParserOptions):
    """
    Image options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'output_path': 'str',
        'start_page_number': 'int',
        'count_pages_to_extract': 'int'
    }

    attribute_map = {
        'output_path': 'OutputPath',
        'start_page_number': 'StartPageNumber',
        'count_pages_to_extract': 'CountPagesToExtract'
    }

    def __init__(self, output_path=None, start_page_number=None, count_pages_to_extract=None, **kwargs):  # noqa: E501
        """Initializes new instance of ImagesOptions"""  # noqa: E501

        self._output_path = None
        self._start_page_number = None
        self._count_pages_to_extract = None

        if output_path is not None:
            self.output_path = output_path
        if start_page_number is not None:
            self.start_page_number = start_page_number
        if count_pages_to_extract is not None:
            self.count_pages_to_extract = count_pages_to_extract

        base = super(ImagesOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def output_path(self):
        """
        Gets the output_path.  # noqa: E501

        Gets or sets the output path for extracted images.  # noqa: E501

        :return: The output_path.  # noqa: E501
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """
        Sets the output_path.

        Gets or sets the output path for extracted images.  # noqa: E501

        :param output_path: The output_path.  # noqa: E501
        :type: str
        """
        self._output_path = output_path
    
    @property
    def start_page_number(self):
        """
        Gets the start_page_number.  # noqa: E501

        Gets or sets the zero-based start page index.  # noqa: E501

        :return: The start_page_number.  # noqa: E501
        :rtype: int
        """
        return self._start_page_number

    @start_page_number.setter
    def start_page_number(self, start_page_number):
        """
        Sets the start_page_number.

        Gets or sets the zero-based start page index.  # noqa: E501

        :param start_page_number: The start_page_number.  # noqa: E501
        :type: int
        """
        self._start_page_number = start_page_number
    
    @property
    def count_pages_to_extract(self):
        """
        Gets the count_pages_to_extract.  # noqa: E501

        Gets or sets the number of pages to extract.  # noqa: E501

        :return: The count_pages_to_extract.  # noqa: E501
        :rtype: int
        """
        return self._count_pages_to_extract

    @count_pages_to_extract.setter
    def count_pages_to_extract(self, count_pages_to_extract):
        """
        Sets the count_pages_to_extract.

        Gets or sets the number of pages to extract.  # noqa: E501

        :param count_pages_to_extract: The count_pages_to_extract.  # noqa: E501
        :type: int
        """
        self._count_pages_to_extract = count_pages_to_extract

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
        if not isinstance(other, ImagesOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
