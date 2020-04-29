# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ContainerItem.py">
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

class ContainerItem(object):
    """
    Represents a container item like Zip archive entity, email attachment, PDF Portfolio item and so on.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'file_path': 'str',
        'directory': 'str',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'Name',
        'file_path': 'FilePath',
        'directory': 'Directory',
        'metadata': 'Metadata'
    }

    def __init__(self, name=None, file_path=None, directory=None, metadata=None, **kwargs):  # noqa: E501
        """Initializes new instance of ContainerItem"""  # noqa: E501

        self._name = None
        self._file_path = None
        self._directory = None
        self._metadata = None

        if name is not None:
            self.name = name
        if file_path is not None:
            self.file_path = file_path
        if directory is not None:
            self.directory = directory
        if metadata is not None:
            self.metadata = metadata
    
    @property
    def name(self):
        """
        Gets the name.  # noqa: E501

        Gets or sets the name of the item.  # noqa: E501

        :return: The name.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name.

        Gets or sets the name of the item.  # noqa: E501

        :param name: The name.  # noqa: E501
        :type: str
        """
        self._name = name
    
    @property
    def file_path(self):
        """
        Gets the file_path.  # noqa: E501

        Gets or sets the full path of the item.  # noqa: E501

        :return: The file_path.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """
        Sets the file_path.

        Gets or sets the full path of the item.  # noqa: E501

        :param file_path: The file_path.  # noqa: E501
        :type: str
        """
        self._file_path = file_path
    
    @property
    def directory(self):
        """
        Gets the directory.  # noqa: E501

        Gets or sets the directory of the item.  # noqa: E501

        :return: The directory.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """
        Sets the directory.

        Gets or sets the directory of the item.  # noqa: E501

        :param directory: The directory.  # noqa: E501
        :type: str
        """
        self._directory = directory
    
    @property
    def metadata(self):
        """
        Gets the metadata.  # noqa: E501

        Gets or sets the collection of metadata items.  # noqa: E501

        :return: The metadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata.

        Gets or sets the collection of metadata items.  # noqa: E501

        :param metadata: The metadata.  # noqa: E501
        :type: dict(str, str)
        """
        self._metadata = metadata

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
        if not isinstance(other, ContainerItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
