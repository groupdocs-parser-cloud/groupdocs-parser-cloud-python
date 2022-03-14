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

class TestParserTextApi(TestContext):
    """ParseApi unit tests"""

    def test_extract_txt(self):
        """
        Test case for test_extract_txt

        Extract text from document.
        """
        options = TextOptions()
        options.file_info = TestFile.one_page().ToFileInfo()
        request = TextRequest(options)     
        data = self.parse_api.text(request)
        self.assertIsNotNone(data)
        self.assertEqual("First Page\r\r\f", data.text)

    def test_extract_pages(self):
        """
        Test case for test_extract_pages

        Extract text from document.
        """
        options = TextOptions()
        options.file_info = TestFile.four_pages().ToFileInfo()
        options.start_page_number = 0
        options.count_pages_to_extract = 4
        text_options = FormattedTextOptions("PlainText")
        options.formatted_text_options = text_options
        request = TextRequest(options)     
        data = self.parse_api.text(request)
        self.assertIsNotNone(data)
        self.assertEqual(0, data.pages[0].page_index)
        self.assertEqual("Text inside bookmark 0\r\n\r\nPage 0 heading\r\n\r\nPage Text - Page 0\r\n\r\n\fText inside bookmark 1\r\n\r\n", data.pages[0].text)
        self.assertEqual(3, data.pages[3].page_index)
        self.assertEqual("\fText inside bookmark 3\r\n\r\nPage 3 heading\r\n\r\nPage Text - Page 3\r\n\r\n", data.pages[3].text)
    
    def test_extract_formatted(self):
        """
        Test case for test_extract_formatted

        Extract text from document.
        """
        options = TextOptions()
        options.file_info = TestFile.formatted_document().ToFileInfo()
        text_options = FormattedTextOptions("Html")
        options.formatted_text_options = text_options
        request = TextRequest(options)     
        data = self.parse_api.text(request)
        self.assertIsNotNone(data)
        self.assertIn("<b>Bold text</b>", data.text)
        self.assertIn("<i>Italic text</i>", data.text)
        self.assertIn("<h1>Heading 1</h1>", data.text)
        self.assertIn("<tr><td><p>table</p></td>", data.text)
        self.assertIn("<a href=\"http://targetwebsite.domain\">Hyperlink </a>", data.text)
        self.assertIn("<ol><li><i>First element</i>", data.text)

    
    def test_extract_text_file_not_found_result(self):
        options = TextOptions()
        options.file_info = TestFile.not_exist().ToFileInfo()
        request = TextRequest(options)     
        with self.assertRaises(ApiException) as context:
            self.parse_api.text(request)
        self.assertEqual("Can't find file located at 'folder\\file-not-exist.pdf'.", get_error_message(context.exception.message))

    def test_extract_text_incorrect_password(self):
        options = TextOptions()
        options.file_info = TestFile.password_protected().ToFileInfo()
        options.file_info.password = "123"
        request = TextRequest(options)     
        with self.assertRaises(ApiException) as context:
            self.parse_api.text(request)
        self.assertEqual("Password provided for file 'words\\docx\\password-protected.docx' is incorrect.", get_error_message(context.exception.message))

    def test_extract_txt_md(self):
            """
            Test case for test_extract_txt_md

            Extract text from document.
            """
            options = TextOptions()
            options.file_info = TestFile.md().ToFileInfo()
            request = TextRequest(options)
            data = self.parse_api.text(request)
            self.assertIsNotNone(data)
            self.assertEqual("# Test\r\rText for test:\r\r\tOne\r\tTwo\r\tSub1\rSub2\r\tThree\r\rBullets:\r\rA\rAA\rB\rC\f", data.text)


if __name__ == '__main__':
    unittest.main()
