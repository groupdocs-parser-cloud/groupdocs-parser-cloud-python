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

class TestParserContainerApi(TestContext):
    """InfoApi unit tests"""

    def test_get_container_item_info(self):
        """
        Test case for test_get_container_item_info

        Retrieve information about document.
        """
        container_options = ContainerOptions()
        container_options.file_info = TestFile.zip().ToFileInfo()
        request = ContainerRequest(container_options)     
        data = self.info_api.container(request)
        self.assertIsNotNone(data)
        self.assertEqual(2, len(data.container_items))
        self.assertTrue(any(x.name == "one-page.docx" for x in data.container_items))
    
    def test_get_container_item_info_file_not_found_result(self):
        container_options = ContainerOptions()
        container_options.file_info = TestFile.not_exist().ToFileInfo()
        request = ContainerRequest(container_options)
        with self.assertRaises(ApiException) as context:
            self.info_api.container(request)
        self.assertEqual("Can't find file located at 'folder\\file-not-exist.pdf'.", get_error_message(context.exception.message))

    def test_get_container_item_info_unsupported_file(self):
        container_options = ContainerOptions()
        container_options.file_info = TestFile.four_pages().ToFileInfo()
        request = ContainerRequest(container_options)
        with self.assertRaises(ApiException) as context:
            self.info_api.container(request)
        self.assertEqual("The specified file 'words\\docx\\four-pages.docx' has type which is not currently supported.", get_error_message(context.exception.message))

    def test_get_container_item_info_rar(self):
            """
            Test case for test_get_container_item_info_rar

            Retrieve information about document.
            """
            container_options = ContainerOptions()
            container_options.file_info = TestFile.rar().ToFileInfo()
            request = ContainerRequest(container_options)
            data = self.info_api.container(request)
            self.assertIsNotNone(data)
            self.assertEqual(2, len(data.container_items))
            self.assertTrue(any(x.name == "sample.pdf" for x in data.container_items))

    def test_get_container_item_info_tar(self):
        """
        Test case for test_get_container_item_info_tar

        Retrieve information about document.
        """
        container_options = ContainerOptions()
        container_options.file_info = TestFile.rar().ToFileInfo()
        request = ContainerRequest(container_options)
        data = self.info_api.container(request)
        self.assertIsNotNone(data)
        self.assertEqual(2, len(data.container_items))
        self.assertTrue(any(x.name == "sample.pdf" for x in data.container_items))

if __name__ == '__main__':
    unittest.main()
