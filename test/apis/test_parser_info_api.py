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

class TestParserInfoApi(TestContext):
    """InfoApi unit tests"""

    def test_get_info_txt(self):
        """
        Test case for test_get_info_txt

        Retrieve information about document.
        """
        info_options = InfoOptions()
        info_options.file_info = TestFile.encoding_detection().ToFileInfo()
        request = GetInfoRequest(info_options)     
        data = self.info_api.get_info(request)
        self.assertIsNotNone(data)
        self.assertEqual("PLAIN TEXT FILE", data.file_type.file_format.upper())
        self.assertEqual(1, data.page_count)

    def test_get_info_container_item(self):
        """
        Test case for test_get_info_container_item

        Retrieve information about document.
        """
        info_options = InfoOptions()
        info_options.file_info = TestFile.zip().ToFileInfo()
        info_options.container_item_info = ContainerItemInfo("one-page.docx")
        request = GetInfoRequest(info_options)     
        data = self.info_api.get_info(request)
        self.assertIsNotNone(data)
        self.assertEqual("MICROSOFT WORD OPEN XML DOCUMENT", data.file_type.file_format.upper())
        self.assertEqual(1, data.page_count)
    
    def test_get_info_file_not_found_result(self):
        info_options = InfoOptions()
        info_options.file_info = TestFile.not_exist().ToFileInfo()
        request = GetInfoRequest(info_options)
        with self.assertRaises(ApiException) as context:
            self.info_api.get_info(request)
        self.assertEqual("Can't find file located at 'folder\\file-not-exist.pdf'.", get_error_message(context.exception.message))

    def test_get_info_incorrect_password(self):
        info_options = InfoOptions()
        info_options.file_info = TestFile.password_protected().ToFileInfo()
        info_options.file_info.password = "123"
        request = GetInfoRequest(info_options)
        with self.assertRaises(ApiException) as context:
            self.info_api.get_info(request)
        self.assertEqual("Password provided for file 'words\\docx\\password-protected.docx' is incorrect.", get_error_message(context.exception.message))


if __name__ == '__main__':
    unittest.main()
