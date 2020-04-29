# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="FieldPosition.py">
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

class FieldPosition(object):
    """
    Field position class.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field_position_type': 'str',
        'rectangle': 'Rectangle',
        'regex': 'str',
        'match_case': 'bool',
        'linked_field_name': 'str',
        'is_left_linked': 'bool',
        'is_right_linked': 'bool',
        'is_top_linked': 'bool',
        'is_bottom_linked': 'bool',
        'search_area': 'Size',
        'auto_scale': 'bool'
    }

    attribute_map = {
        'field_position_type': 'FieldPositionType',
        'rectangle': 'Rectangle',
        'regex': 'Regex',
        'match_case': 'MatchCase',
        'linked_field_name': 'LinkedFieldName',
        'is_left_linked': 'IsLeftLinked',
        'is_right_linked': 'IsRightLinked',
        'is_top_linked': 'IsTopLinked',
        'is_bottom_linked': 'IsBottomLinked',
        'search_area': 'SearchArea',
        'auto_scale': 'AutoScale'
    }

    def __init__(self, field_position_type=None, rectangle=None, regex=None, match_case=None, linked_field_name=None, is_left_linked=None, is_right_linked=None, is_top_linked=None, is_bottom_linked=None, search_area=None, auto_scale=None, **kwargs):  # noqa: E501
        """Initializes new instance of FieldPosition"""  # noqa: E501

        self._field_position_type = None
        self._rectangle = None
        self._regex = None
        self._match_case = None
        self._linked_field_name = None
        self._is_left_linked = None
        self._is_right_linked = None
        self._is_top_linked = None
        self._is_bottom_linked = None
        self._search_area = None
        self._auto_scale = None

        if field_position_type is not None:
            self.field_position_type = field_position_type
        if rectangle is not None:
            self.rectangle = rectangle
        if regex is not None:
            self.regex = regex
        if match_case is not None:
            self.match_case = match_case
        if linked_field_name is not None:
            self.linked_field_name = linked_field_name
        if is_left_linked is not None:
            self.is_left_linked = is_left_linked
        if is_right_linked is not None:
            self.is_right_linked = is_right_linked
        if is_top_linked is not None:
            self.is_top_linked = is_top_linked
        if is_bottom_linked is not None:
            self.is_bottom_linked = is_bottom_linked
        if search_area is not None:
            self.search_area = search_area
        if auto_scale is not None:
            self.auto_scale = auto_scale
    
    @property
    def field_position_type(self):
        """
        Gets the field_position_type.  # noqa: E501

        Provides a template field position.  # noqa: E501

        :return: The field_position_type.  # noqa: E501
        :rtype: str
        """
        return self._field_position_type

    @field_position_type.setter
    def field_position_type(self, field_position_type):
        """
        Sets the field_position_type.

        Provides a template field position.  # noqa: E501

        :param field_position_type: The field_position_type.  # noqa: E501
        :type: str
        """
        self._field_position_type = field_position_type
    
    @property
    def rectangle(self):
        """
        Gets the rectangle.  # noqa: E501

        Rectangular area on the page that bounds the field value.  # noqa: E501

        :return: The rectangle.  # noqa: E501
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle.

        Rectangular area on the page that bounds the field value.  # noqa: E501

        :param rectangle: The rectangle.  # noqa: E501
        :type: Rectangle
        """
        self._rectangle = rectangle
    
    @property
    def regex(self):
        """
        Gets the regex.  # noqa: E501

        Gets or sets the regular expression.  # noqa: E501

        :return: The regex.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """
        Sets the regex.

        Gets or sets the regular expression.  # noqa: E501

        :param regex: The regex.  # noqa: E501
        :type: str
        """
        self._regex = regex
    
    @property
    def match_case(self):
        """
        Gets the match_case.  # noqa: E501

        Gets or sets the value that indicates whether a text case isn't ignored.  # noqa: E501

        :return: The match_case.  # noqa: E501
        :rtype: bool
        """
        return self._match_case

    @match_case.setter
    def match_case(self, match_case):
        """
        Sets the match_case.

        Gets or sets the value that indicates whether a text case isn't ignored.  # noqa: E501

        :param match_case: The match_case.  # noqa: E501
        :type: bool
        """
        if match_case is None:
            raise ValueError("Invalid value for `match_case`, must not be `None`")  # noqa: E501
        self._match_case = match_case
    
    @property
    def linked_field_name(self):
        """
        Gets the linked_field_name.  # noqa: E501

        Gets or sets the name of the linked field.  # noqa: E501

        :return: The linked_field_name.  # noqa: E501
        :rtype: str
        """
        return self._linked_field_name

    @linked_field_name.setter
    def linked_field_name(self, linked_field_name):
        """
        Sets the linked_field_name.

        Gets or sets the name of the linked field.  # noqa: E501

        :param linked_field_name: The linked_field_name.  # noqa: E501
        :type: str
        """
        self._linked_field_name = linked_field_name
    
    @property
    def is_left_linked(self):
        """
        Gets the is_left_linked.  # noqa: E501

        Gets or sets the value that indicates whether a field is searched by the left from the linked field.  # noqa: E501

        :return: The is_left_linked.  # noqa: E501
        :rtype: bool
        """
        return self._is_left_linked

    @is_left_linked.setter
    def is_left_linked(self, is_left_linked):
        """
        Sets the is_left_linked.

        Gets or sets the value that indicates whether a field is searched by the left from the linked field.  # noqa: E501

        :param is_left_linked: The is_left_linked.  # noqa: E501
        :type: bool
        """
        if is_left_linked is None:
            raise ValueError("Invalid value for `is_left_linked`, must not be `None`")  # noqa: E501
        self._is_left_linked = is_left_linked
    
    @property
    def is_right_linked(self):
        """
        Gets the is_right_linked.  # noqa: E501

        Gets or sets a value indicating whether this instance is right linked.  # noqa: E501

        :return: The is_right_linked.  # noqa: E501
        :rtype: bool
        """
        return self._is_right_linked

    @is_right_linked.setter
    def is_right_linked(self, is_right_linked):
        """
        Sets the is_right_linked.

        Gets or sets a value indicating whether this instance is right linked.  # noqa: E501

        :param is_right_linked: The is_right_linked.  # noqa: E501
        :type: bool
        """
        if is_right_linked is None:
            raise ValueError("Invalid value for `is_right_linked`, must not be `None`")  # noqa: E501
        self._is_right_linked = is_right_linked
    
    @property
    def is_top_linked(self):
        """
        Gets the is_top_linked.  # noqa: E501

        Gets or sets a value indicating whether this instance is top linked.  # noqa: E501

        :return: The is_top_linked.  # noqa: E501
        :rtype: bool
        """
        return self._is_top_linked

    @is_top_linked.setter
    def is_top_linked(self, is_top_linked):
        """
        Sets the is_top_linked.

        Gets or sets a value indicating whether this instance is top linked.  # noqa: E501

        :param is_top_linked: The is_top_linked.  # noqa: E501
        :type: bool
        """
        if is_top_linked is None:
            raise ValueError("Invalid value for `is_top_linked`, must not be `None`")  # noqa: E501
        self._is_top_linked = is_top_linked
    
    @property
    def is_bottom_linked(self):
        """
        Gets the is_bottom_linked.  # noqa: E501

        Gets or sets a value indicating whether this instance is bottom linked.  # noqa: E501

        :return: The is_bottom_linked.  # noqa: E501
        :rtype: bool
        """
        return self._is_bottom_linked

    @is_bottom_linked.setter
    def is_bottom_linked(self, is_bottom_linked):
        """
        Sets the is_bottom_linked.

        Gets or sets a value indicating whether this instance is bottom linked.  # noqa: E501

        :param is_bottom_linked: The is_bottom_linked.  # noqa: E501
        :type: bool
        """
        if is_bottom_linked is None:
            raise ValueError("Invalid value for `is_bottom_linked`, must not be `None`")  # noqa: E501
        self._is_bottom_linked = is_bottom_linked
    
    @property
    def search_area(self):
        """
        Gets the search_area.  # noqa: E501

        Gets or sets the size of the area where a field is searched.  # noqa: E501

        :return: The search_area.  # noqa: E501
        :rtype: Size
        """
        return self._search_area

    @search_area.setter
    def search_area(self, search_area):
        """
        Sets the search_area.

        Gets or sets the size of the area where a field is searched.  # noqa: E501

        :param search_area: The search_area.  # noqa: E501
        :type: Size
        """
        self._search_area = search_area
    
    @property
    def auto_scale(self):
        """
        Gets the auto_scale.  # noqa: E501

        Gets or sets Gets the value that indicates whether SearchArea is scaled by the linked field size.  # noqa: E501

        :return: The auto_scale.  # noqa: E501
        :rtype: bool
        """
        return self._auto_scale

    @auto_scale.setter
    def auto_scale(self, auto_scale):
        """
        Sets the auto_scale.

        Gets or sets Gets the value that indicates whether SearchArea is scaled by the linked field size.  # noqa: E501

        :param auto_scale: The auto_scale.  # noqa: E501
        :type: bool
        """
        if auto_scale is None:
            raise ValueError("Invalid value for `auto_scale`, must not be `None`")  # noqa: E501
        self._auto_scale = auto_scale

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
        if not isinstance(other, FieldPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
