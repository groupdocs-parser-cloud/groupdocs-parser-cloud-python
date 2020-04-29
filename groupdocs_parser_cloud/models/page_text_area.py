# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PageTextArea.py">
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

class PageTextArea(object):
    """
    Represents a page text area which is used to represent a text value in the parsing by template functionality.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text': 'str',
        'base_line': 'float',
        'areas': 'list[PageTextArea]',
        'text_style': 'TextStyle'
    }

    attribute_map = {
        'text': 'Text',
        'base_line': 'BaseLine',
        'areas': 'Areas',
        'text_style': 'TextStyle'
    }

    def __init__(self, text=None, base_line=None, areas=None, text_style=None, **kwargs):  # noqa: E501
        """Initializes new instance of PageTextArea"""  # noqa: E501

        self._text = None
        self._base_line = None
        self._areas = None
        self._text_style = None

        if text is not None:
            self.text = text
        if base_line is not None:
            self.base_line = base_line
        if areas is not None:
            self.areas = areas
        if text_style is not None:
            self.text_style = text_style
    
    @property
    def text(self):
        """
        Gets the text.  # noqa: E501

        Gets or sets the text.  # noqa: E501

        :return: The text.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text.

        Gets or sets the text.  # noqa: E501

        :param text: The text.  # noqa: E501
        :type: str
        """
        self._text = text
    
    @property
    def base_line(self):
        """
        Gets the base_line.  # noqa: E501

        Gets or sets the base line.  # noqa: E501

        :return: The base_line.  # noqa: E501
        :rtype: float
        """
        return self._base_line

    @base_line.setter
    def base_line(self, base_line):
        """
        Sets the base_line.

        Gets or sets the base line.  # noqa: E501

        :param base_line: The base_line.  # noqa: E501
        :type: float
        """
        if base_line is None:
            raise ValueError("Invalid value for `base_line`, must not be `None`")  # noqa: E501
        self._base_line = base_line
    
    @property
    def areas(self):
        """
        Gets the areas.  # noqa: E501

        Gets or sets the collection of child text page areas.  # noqa: E501

        :return: The areas.  # noqa: E501
        :rtype: list[PageTextArea]
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """
        Sets the areas.

        Gets or sets the collection of child text page areas.  # noqa: E501

        :param areas: The areas.  # noqa: E501
        :type: list[PageTextArea]
        """
        self._areas = areas
    
    @property
    def text_style(self):
        """
        Gets the text_style.  # noqa: E501

        Gets or sets the text style such as font size, font name an so on.  # noqa: E501

        :return: The text_style.  # noqa: E501
        :rtype: TextStyle
        """
        return self._text_style

    @text_style.setter
    def text_style(self, text_style):
        """
        Sets the text_style.

        Gets or sets the text style such as font size, font name an so on.  # noqa: E501

        :param text_style: The text_style.  # noqa: E501
        :type: TextStyle
        """
        self._text_style = text_style

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
        if not isinstance(other, PageTextArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
