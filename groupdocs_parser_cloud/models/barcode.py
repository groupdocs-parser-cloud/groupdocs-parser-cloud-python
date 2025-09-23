# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Barcode.py">
#   Copyright (c) Aspose Pty Ltd
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

class Barcode(object):
    """
    Represents an barcode.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code_type_name': 'str',
        'page': 'BarcodePage',
        'rectangle': 'Rectangle',
        'value': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'code_type_name': 'CodeTypeName',
        'page': 'Page',
        'rectangle': 'Rectangle',
        'value': 'Value',
        'download_url': 'DownloadUrl'
    }

    def __init__(self, code_type_name=None, page=None, rectangle=None, value=None, download_url=None, **kwargs):  # noqa: E501
        """Initializes new instance of Barcode"""  # noqa: E501

        self._code_type_name = None
        self._page = None
        self._rectangle = None
        self._value = None
        self._download_url = None

        if code_type_name is not None:
            self.code_type_name = code_type_name
        if page is not None:
            self.page = page
        if rectangle is not None:
            self.rectangle = rectangle
        if value is not None:
            self.value = value
        if download_url is not None:
            self.download_url = download_url
    
    @property
    def code_type_name(self):
        """
        Gets the code_type_name.  # noqa: E501

        Gets the name of the barcode type.  # noqa: E501

        :return: The code_type_name.  # noqa: E501
        :rtype: str
        """
        return self._code_type_name

    @code_type_name.setter
    def code_type_name(self, code_type_name):
        """
        Sets the code_type_name.

        Gets the name of the barcode type.  # noqa: E501

        :param code_type_name: The code_type_name.  # noqa: E501
        :type: str
        """
        self._code_type_name = code_type_name
    
    @property
    def page(self):
        """
        Gets the page.  # noqa: E501

        Gets the document page information such as page index and page size.  # noqa: E501

        :return: The page.  # noqa: E501
        :rtype: BarcodePage
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page.

        Gets the document page information such as page index and page size.  # noqa: E501

        :param page: The page.  # noqa: E501
        :type: BarcodePage
        """
        self._page = page
    
    @property
    def rectangle(self):
        """
        Gets the rectangle.  # noqa: E501

        Gets the rectangular area.  # noqa: E501

        :return: The rectangle.  # noqa: E501
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle.

        Gets the rectangular area.  # noqa: E501

        :param rectangle: The rectangle.  # noqa: E501
        :type: Rectangle
        """
        self._rectangle = rectangle
    
    @property
    def value(self):
        """
        Gets the value.  # noqa: E501

        Gets the barcode value.  # noqa: E501

        :return: The value.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value.

        Gets the barcode value.  # noqa: E501

        :param value: The value.  # noqa: E501
        :type: str
        """
        self._value = value
    
    @property
    def download_url(self):
        """
        Gets the download_url.  # noqa: E501

        Gets or sets the barcode download URL.  # noqa: E501

        :return: The download_url.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url.

        Gets or sets the barcode download URL.  # noqa: E501

        :param download_url: The download_url.  # noqa: E501
        :type: str
        """
        self._download_url = download_url

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
        if not isinstance(other, Barcode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
