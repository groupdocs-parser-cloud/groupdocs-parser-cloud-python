# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd">
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

from __future__ import absolute_import

import unittest

from groupdocs_parser_cloud import *
from test.JsonUtils import get_error_message
from test.test_context import TestContext
from test.test_file import TestFile

class TestParserTemplateApi(TestContext):
    """TemplateApi unit tests"""

    def test_create_template(self):
        """
        Test case for test_create_template

        Create or update document template.
        """
        options = CreateTemplateOptions()
        options.template = self.get_template()
        options.template_path = "templates/template_2.json"
        request = CreateTemplateRequest(options)
        data = self.template_api.create_template(request)
        self.assertIsNotNone(data)
        self.assertIn("storage/file/templates/template_2.json", data.url)

    def test_get_template(self):
        """
        Test case for test_get_template

        Retrieve document template.
        """
        options = CreateTemplateOptions()
        options.template = self.get_template()
        options.template_path = "templates/template_1.json"
        request = CreateTemplateRequest(options)
        data = self.template_api.create_template(request)
        self.assertIsNotNone(data)

        get_options = TemplateOptions()
        get_options.template_path = "templates/template_1.json"
        get_request = GetTemplateRequest(get_options)
        get_data = self.template_api.get_template(get_request)
        self.assertIsNotNone(get_data)
        self.assertEqual(3, len(get_data.fields))
        self.assertEqual(1, len(get_data.tables))

    def test_delete_template(self):
        """
        Test case for test_delete_template

        Delete document template.
        """
        options = CreateTemplateOptions()
        options.template = self.get_template()
        options.template_path = "templates/template_1.json"
        request = CreateTemplateRequest(options)
        data = self.template_api.create_template(request)
        self.assertIsNotNone(data)

        delete_options = TemplateOptions()
        delete_options.template_path = "templates/template_1.json"
        delete_request = DeleteTemplateRequest(delete_options)
        delete_data = self.template_api.delete_template(delete_request)
    
    def test_template_file_not_found_result(self):
        delete_options = TemplateOptions()
        delete_options.template_path = "notExistTemplate.json"
        delete_request = DeleteTemplateRequest(delete_options)

        with self.assertRaises(ApiException) as context:
            self.template_api.delete_template(delete_request)
        self.assertEqual("Can't find file located at 'notExistTemplate.json'.", get_error_message(context.exception.message))

    def get_template(self):
        field1 = Field()
        field1.field_name = "Field1"
        field1.page_index = 4
        fieldPosition1 = FieldPosition()
        fieldPosition1.field_position_type = "Fixed"
        rect1 = Rectangle(position=Point(0, 0), size=Size(30, 140))
        fieldPosition1.rectangle = rect1
        field1.field_position = fieldPosition1

        field2 = Field()
        field2.field_name = "RelatedField2"
        fieldPosition2 = FieldPosition()
        fieldPosition2.field_position_type = "Linked"
        fieldPosition2.linked_field_name = "Field1"
        fieldPosition2.is_bottom_linked = True
        fieldPosition2.is_right_linked = True
        fieldPosition2.search_area = Size(24, 209)
        fieldPosition2.auto_scale = False
        field2.field_position = fieldPosition2

        field3 = Field()
        field3.field_name = "Regex"
        fieldPosition3 = FieldPosition()
        fieldPosition3.field_position_type = "Regex"
        fieldPosition3.regex = "REGEX TEXT 123"
        field3.field_position = fieldPosition3

        table = Table()
        table.table_name = "TableCells"
        table.page_index = 5
        detectorparams = DetectorParameters()
        rect = Rectangle(position=Point(0, 0), size=Size(400, 600))
        detectorparams.rectangle = rect
        table.detector_parameters = detectorparams

        fields = [field1, field2, field3]
        tables = [table]
        options = Template()
        options.fields = fields
        options.tables = tables
        return options

if __name__ == '__main__':
    unittest.main()
