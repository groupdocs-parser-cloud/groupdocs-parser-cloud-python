# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ParseOptions.py">
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

class ParseOptions(ParserOptions):
    """
    Parse options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'template': 'Template',
        'template_path': 'str'
    }

    attribute_map = {
        'template': 'Template',
        'template_path': 'TemplatePath'
    }

    def __init__(self, template=None, template_path=None, **kwargs):  # noqa: E501
        """Initializes new instance of ParseOptions"""  # noqa: E501

        self._template = None
        self._template_path = None

        if template is not None:
            self.template = template
        if template_path is not None:
            self.template_path = template_path

        base = super(ParseOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def template(self):
        """
        Gets the template.  # noqa: E501

        User-generated template to extract metadata from the document.  # noqa: E501

        :return: The template.  # noqa: E501
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template.

        User-generated template to extract metadata from the document.  # noqa: E501

        :param template: The template.  # noqa: E501
        :type: Template
        """
        self._template = template
    
    @property
    def template_path(self):
        """
        Gets the template_path.  # noqa: E501

        The path of the file, located in the storage, which contains a user-generated template to parse data. Is used when the Template parameter is not provided.  # noqa: E501

        :return: The template_path.  # noqa: E501
        :rtype: str
        """
        return self._template_path

    @template_path.setter
    def template_path(self, template_path):
        """
        Sets the template_path.

        The path of the file, located in the storage, which contains a user-generated template to parse data. Is used when the Template parameter is not provided.  # noqa: E501

        :param template_path: The template_path.  # noqa: E501
        :type: str
        """
        self._template_path = template_path

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
        if not isinstance(other, ParseOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
