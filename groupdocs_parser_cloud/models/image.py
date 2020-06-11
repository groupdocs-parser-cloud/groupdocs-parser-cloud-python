# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Image.py">
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

class Image(object):
    """
    Represents an image.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'path': 'str',
        'download_url': 'str',
        'page_index': 'int',
        'rotation': 'float',
        'file_format': 'str',
        'rectangle': 'Rectangle'
    }

    attribute_map = {
        'path': 'Path',
        'download_url': 'DownloadUrl',
        'page_index': 'PageIndex',
        'rotation': 'Rotation',
        'file_format': 'FileFormat',
        'rectangle': 'Rectangle'
    }

    def __init__(self, path=None, download_url=None, page_index=None, rotation=None, file_format=None, rectangle=None, **kwargs):  # noqa: E501
        """Initializes new instance of Image"""  # noqa: E501

        self._path = None
        self._download_url = None
        self._page_index = None
        self._rotation = None
        self._file_format = None
        self._rectangle = None

        if path is not None:
            self.path = path
        if download_url is not None:
            self.download_url = download_url
        if page_index is not None:
            self.page_index = page_index
        if rotation is not None:
            self.rotation = rotation
        if file_format is not None:
            self.file_format = file_format
        if rectangle is not None:
            self.rectangle = rectangle
    
    @property
    def path(self):
        """
        Gets the path.  # noqa: E501

        Gets or sets The path of the image, located in the storage.  # noqa: E501

        :return: The path.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path.

        Gets or sets The path of the image, located in the storage.  # noqa: E501

        :param path: The path.  # noqa: E501
        :type: str
        """
        self._path = path
    
    @property
    def download_url(self):
        """
        Gets the download_url.  # noqa: E501

        Gets or sets the image download URL.  # noqa: E501

        :return: The download_url.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url.

        Gets or sets the image download URL.  # noqa: E501

        :param download_url: The download_url.  # noqa: E501
        :type: str
        """
        self._download_url = download_url
    
    @property
    def page_index(self):
        """
        Gets the page_index.  # noqa: E501

        Gets or sets the index of the page.  # noqa: E501

        :return: The page_index.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index.

        Gets or sets the index of the page.  # noqa: E501

        :param page_index: The page_index.  # noqa: E501
        :type: int
        """
        self._page_index = page_index
    
    @property
    def rotation(self):
        """
        Gets the rotation.  # noqa: E501

        Gets or sets the rotation of the image in degrees.  # noqa: E501

        :return: The rotation.  # noqa: E501
        :rtype: float
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """
        Sets the rotation.

        Gets or sets the rotation of the image in degrees.  # noqa: E501

        :param rotation: The rotation.  # noqa: E501
        :type: float
        """
        self._rotation = rotation
    
    @property
    def file_format(self):
        """
        Gets the file_format.  # noqa: E501

        Gets or sets the image file format.  # noqa: E501

        :return: The file_format.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """
        Sets the file_format.

        Gets or sets the image file format.  # noqa: E501

        :param file_format: The file_format.  # noqa: E501
        :type: str
        """
        self._file_format = file_format
    
    @property
    def rectangle(self):
        """
        Gets the rectangle.  # noqa: E501

        Gets or sets the rectangle area of the image.  # noqa: E501

        :return: The rectangle.  # noqa: E501
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle.

        Gets or sets the rectangle area of the image.  # noqa: E501

        :param rectangle: The rectangle.  # noqa: E501
        :type: Rectangle
        """
        self._rectangle = rectangle

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
