# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd">
#   Copyright (c) Aspose Pty Ltd
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
from groupdocs_parser_cloud.apis.parse_api import BarcodesRequest
from groupdocs_parser_cloud.models.barcodes_options import BarcodesOptions
from test.JsonUtils import get_error_message
from test.test_context import TestContext
from test.test_file import TestFile

class TestParserBarcodeApi(TestContext):
    """ParseApi unit tests"""

    def test_get_barcode_docx(self):
        """
        Test case for test_get_barcode_docx

        Extract barcodes from documents.
        """
        barcode_options = BarcodesOptions()
        barcode_options.file_info = TestFile.barcode().ToFileInfo()
        request = BarcodesRequest(barcode_options)     
        data = self.parse_api.barcodes(request)
        self.assertIsNotNone(data)
        for barcode in data.barcodes:
            self.assertIsNotNone(barcode.value)

if __name__ == '__main__':
    unittest.main()