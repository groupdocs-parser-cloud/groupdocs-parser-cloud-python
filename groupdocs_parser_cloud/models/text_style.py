# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="TextStyle.py">
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

class TextStyle(object):
    """
    The text style such as font size, font name an so on.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'font_name': 'str',
        'font_size': 'float',
        'is_bold': 'bool',
        'is_italic': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'font_name': 'FontName',
        'font_size': 'FontSize',
        'is_bold': 'IsBold',
        'is_italic': 'IsItalic',
        'name': 'Name'
    }

    def __init__(self, font_name=None, font_size=None, is_bold=None, is_italic=None, name=None, **kwargs):  # noqa: E501
        """Initializes new instance of TextStyle"""  # noqa: E501

        self._font_name = None
        self._font_size = None
        self._is_bold = None
        self._is_italic = None
        self._name = None

        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if is_bold is not None:
            self.is_bold = is_bold
        if is_italic is not None:
            self.is_italic = is_italic
        if name is not None:
            self.name = name
    
    @property
    def font_name(self):
        """
        Gets the font_name.  # noqa: E501

        Gets or sets the name of the font.  # noqa: E501

        :return: The font_name.  # noqa: E501
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """
        Sets the font_name.

        Gets or sets the name of the font.  # noqa: E501

        :param font_name: The font_name.  # noqa: E501
        :type: str
        """
        self._font_name = font_name
    
    @property
    def font_size(self):
        """
        Gets the font_size.  # noqa: E501

        Gets or sets the size of the font.  # noqa: E501

        :return: The font_size.  # noqa: E501
        :rtype: float
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """
        Sets the font_size.

        Gets or sets the size of the font.  # noqa: E501

        :param font_size: The font_size.  # noqa: E501
        :type: float
        """
        if font_size is None:
            raise ValueError("Invalid value for `font_size`, must not be `None`")  # noqa: E501
        self._font_size = font_size
    
    @property
    def is_bold(self):
        """
        Gets the is_bold.  # noqa: E501

        Gets or sets the value that indicates whether the font is bold.  # noqa: E501

        :return: The is_bold.  # noqa: E501
        :rtype: bool
        """
        return self._is_bold

    @is_bold.setter
    def is_bold(self, is_bold):
        """
        Sets the is_bold.

        Gets or sets the value that indicates whether the font is bold.  # noqa: E501

        :param is_bold: The is_bold.  # noqa: E501
        :type: bool
        """
        if is_bold is None:
            raise ValueError("Invalid value for `is_bold`, must not be `None`")  # noqa: E501
        self._is_bold = is_bold
    
    @property
    def is_italic(self):
        """
        Gets the is_italic.  # noqa: E501

        Gets or sets the value that indicates whether the font is italic.  # noqa: E501

        :return: The is_italic.  # noqa: E501
        :rtype: bool
        """
        return self._is_italic

    @is_italic.setter
    def is_italic(self, is_italic):
        """
        Sets the is_italic.

        Gets or sets the value that indicates whether the font is italic.  # noqa: E501

        :param is_italic: The is_italic.  # noqa: E501
        :type: bool
        """
        if is_italic is None:
            raise ValueError("Invalid value for `is_italic`, must not be `None`")  # noqa: E501
        self._is_italic = is_italic
    
    @property
    def name(self):
        """
        Gets the name.  # noqa: E501

        Gets or sets the style name.  # noqa: E501

        :return: The name.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name.

        Gets or sets the style name.  # noqa: E501

        :param name: The name.  # noqa: E501
        :type: str
        """
        self._name = name

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
        if not isinstance(other, TextStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
