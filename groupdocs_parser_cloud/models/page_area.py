# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PageArea.py">
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

class PageArea(object):
    """
    Class for document page area.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rectangle': 'Rectangle',
        'page': 'Page',
        'page_text_area': 'PageTextArea',
        'page_table_area': 'PageTableArea'
    }

    attribute_map = {
        'rectangle': 'Rectangle',
        'page': 'Page',
        'page_text_area': 'PageTextArea',
        'page_table_area': 'PageTableArea'
    }

    def __init__(self, rectangle=None, page=None, page_text_area=None, page_table_area=None, **kwargs):  # noqa: E501
        """Initializes new instance of PageArea"""  # noqa: E501

        self._rectangle = None
        self._page = None
        self._page_text_area = None
        self._page_table_area = None

        if rectangle is not None:
            self.rectangle = rectangle
        if page is not None:
            self.page = page
        if page_text_area is not None:
            self.page_text_area = page_text_area
        if page_table_area is not None:
            self.page_table_area = page_table_area
    
    @property
    def rectangle(self):
        """
        Gets the rectangle.  # noqa: E501

        Gets or sets the rectangular area.  # noqa: E501

        :return: The rectangle.  # noqa: E501
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle.

        Gets or sets the rectangular area.  # noqa: E501

        :param rectangle: The rectangle.  # noqa: E501
        :type: Rectangle
        """
        self._rectangle = rectangle
    
    @property
    def page(self):
        """
        Gets the page.  # noqa: E501

        Gets or sets the document page information such as page index and page size.  # noqa: E501

        :return: The page.  # noqa: E501
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page.

        Gets or sets the document page information such as page index and page size.  # noqa: E501

        :param page: The page.  # noqa: E501
        :type: Page
        """
        self._page = page
    
    @property
    def page_text_area(self):
        """
        Gets the page_text_area.  # noqa: E501

        Gets or sets the text area. Represents a page text area which is used to represent a text value in the parsing by template functionality.  # noqa: E501

        :return: The page_text_area.  # noqa: E501
        :rtype: PageTextArea
        """
        return self._page_text_area

    @page_text_area.setter
    def page_text_area(self, page_text_area):
        """
        Sets the page_text_area.

        Gets or sets the text area. Represents a page text area which is used to represent a text value in the parsing by template functionality.  # noqa: E501

        :param page_text_area: The page_text_area.  # noqa: E501
        :type: PageTextArea
        """
        self._page_text_area = page_text_area
    
    @property
    def page_table_area(self):
        """
        Gets the page_table_area.  # noqa: E501

        Gets or sets the table area. Represents a table page area which is used to represent a table in the parsing by template functionality.  # noqa: E501

        :return: The page_table_area.  # noqa: E501
        :rtype: PageTableArea
        """
        return self._page_table_area

    @page_table_area.setter
    def page_table_area(self, page_table_area):
        """
        Sets the page_table_area.

        Gets or sets the table area. Represents a table page area which is used to represent a table in the parsing by template functionality.  # noqa: E501

        :param page_table_area: The page_table_area.  # noqa: E501
        :type: PageTableArea
        """
        self._page_table_area = page_table_area

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
        if not isinstance(other, PageArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
