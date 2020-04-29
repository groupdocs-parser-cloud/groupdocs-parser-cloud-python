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
from test.test_context import TestContext
from test.test_file import TestFile


class TestParserParseApi(TestContext):
    """ParseApi unit tests"""

    def test_parse_document(self):
        """
        Test case for test_parse_document

        Extract data fields and tables from document.
        """
        parse_options = ParseOptions()
        parse_options.file_info = TestFile.template_document_docx().ToFileInfo()
        parse_options.template = self.get_template()
        request = ParseRequest(parse_options)
        data = self.parse_api.parse(request)
        self.assertIsNotNone(data)
        self.assertEqual(4, data.count)

        fieldNames = ["FIELD1", "RELATEDFIELD2", "REGEX", "TABLECELLS"]
        for field in data.fields_data:
            self.assertTrue(field.name in fieldNames)
            if field.name == "TABLECELLS":
                self.assertEqual(
                    4, field.page_area.page_table_area.column_count)
                self.assertEqual(3, field.page_area.page_table_area.row_count)

    def test_parse_file_not_found_result(self):
        parse_options = ParseOptions()
        parse_options.file_info = TestFile.not_exist().ToFileInfo()
        parse_options.template = self.get_template()
        request = ParseRequest(parse_options)
        with self.assertRaises(ApiException) as context:
            self.parse_api.parse(request)
        self.assertEqual(
            "Can't find file located at 'folder\\file-not-exist.pdf'.", context.exception.message)

    def test_parse_incorrect_password(self):
        parse_options = ParseOptions()
        parse_options.file_info = TestFile.password_protected().ToFileInfo()
        parse_options.file_info.password = "123"
        parse_options.template = self.get_template()
        request = ParseRequest(parse_options)
        with self.assertRaises(ApiException) as context:
            self.parse_api.parse(request)
        self.assertEqual(
            "Password provided for file 'words\\docx\\password-protected.docx' is incorrect.", context.exception.message)

    def test_parse_not_supported_file(self):
        parse_options = ParseOptions()
        parse_options.file_info = TestFile.jpeg_file().ToFileInfo()
        parse_options.template = self.get_template()
        request = ParseRequest(parse_options)
        with self.assertRaises(ApiException) as context:
            self.parse_api.parse(request)
        self.assertEqual(
            "The specified file 'image\\jpeg\\document.jpeg' has type which is not currently supported.", context.exception.message)

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
