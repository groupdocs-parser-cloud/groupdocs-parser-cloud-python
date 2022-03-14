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

class TestParserImageApi(TestContext):
    """ParseApi unit tests"""

    def test_get_image_docx(self):
        """
        Test case for test_get_image_docx

        Extract images from documents.
        """
        image_options = ImagesOptions()
        image_options.file_info = TestFile.password_protected().ToFileInfo()
        request = ImagesRequest(image_options)     
        data = self.parse_api.images(request)
        self.assertIsNotNone(data)
        for image in data.images:
            self.assertIn(image.path, "parser/images/words/docx/four-pages_docx/image")
            self.assertIsNotNone(image.download_url)

    def test_get_images_pdf_from_pages(self):
        """
        Test case for test_get_images_pdf_from_pages

        Extract images from documents.
        """
        image_options = ImagesOptions()
        image_options.file_info = TestFile.pdf().ToFileInfo()
        image_options.start_page_number = 1
        image_options.count_pages_to_extract = 2
        request = ImagesRequest(image_options)     
        data = self.parse_api.images(request)
        self.assertIsNotNone(data)
        self.assertIsNotNone(data.pages)
        self.assertEqual(2, len(data.pages))
        self.assertEqual("parser/images/pdf/template-document_pdf/page_1/image_0.jpeg", data.pages[0].images[0].path)
        self.assertEqual("parser/images/pdf/template-document_pdf/page_2/image_0.jpeg", data.pages[1].images[0].path)
    
    def test_get_images_pdf_container_item_from_pages(self):
        """
        Test case for test_get_images_pdf_container_item_from_pages

        Extract images from documents.
        """
        image_options = ImagesOptions()
        image_options.file_info = TestFile.pdf_container().ToFileInfo()
        container_info = ContainerItemInfo()
        container_info.relative_path = "template-document.pdf"
        image_options.container_item_info = container_info
        image_options.start_page_number = 1
        image_options.count_pages_to_extract = 2
        request = ImagesRequest(image_options)     
        data = self.parse_api.images(request)
        self.assertIsNotNone(data)
        self.assertIsNotNone(data.pages)
        self.assertEqual(2, len(data.pages))
        self.assertEqual("parser/images/template-document_pdf/page_1/image_0.jpeg", data.pages[0].images[0].path)
        self.assertEqual("parser/images/template-document_pdf/page_2/image_0.jpeg", data.pages[1].images[0].path)

    def test_get_image_out_of_the_range(self):
        image_options = ImagesOptions()
        image_options.file_info = TestFile.pdf().ToFileInfo()
        image_options.start_page_number = 3
        image_options.count_pages_to_extract = 5
        request = ImagesRequest(image_options)     
        with self.assertRaises(ApiException) as context:
            self.parse_api.images(request)
        self.assertEqual("Request parameters missing or have incorrect format", get_error_message(context.exception.message))
    
    def test_get_image_zip_pages_error(self):
        image_options = ImagesOptions()
        image_options.file_info = TestFile.zip().ToFileInfo()
        image_options.start_page_number = 1
        image_options.count_pages_to_extract = 2
        request = ImagesRequest(image_options)     
        with self.assertRaises(ApiException) as context:
            self.parse_api.images(request)
        self.assertEqual("The specified file 'containers\\archive\\docx.zip' has type which is not currently supported.", get_error_message(context.exception.message))


    def test_get_image_file_not_found_result(self):
        image_options = ImagesOptions()
        image_options.file_info = TestFile.not_exist().ToFileInfo()
        request = ImagesRequest(image_options)
        with self.assertRaises(ApiException) as context:
            self.parse_api.images(request)
        self.assertEqual("Can't find file located at 'folder\\file-not-exist.pdf'.", get_error_message(context.exception.message))

    def test_get_image_incorrect_password(self):
        image_options = ImagesOptions()
        image_options.file_info = TestFile.password_protected().ToFileInfo()
        image_options.file_info.password = "123"
        request = ImagesRequest(image_options)
        with self.assertRaises(ApiException) as context:
            self.parse_api.images(request)
        self.assertEqual("Password provided for file 'words\\docx\\password-protected.docx' is incorrect.", get_error_message(context.exception.message))


if __name__ == '__main__':
    unittest.main()
