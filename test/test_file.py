# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_file.py">
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

from groupdocs_parser_cloud import FileInfo


class TestFile:
    """Test file"""

    @classmethod
    def password_protected(cls):
        f = TestFile()
        f.file_name = "password-protected.docx"
        f.folder = "words\\docx\\"
        f.password = "password"
        return f

    @classmethod
    def four_pages(cls):
        f = TestFile()
        f.file_name = "four-pages.docx"
        f.folder = "words\\docx\\"
        return f

    @classmethod
    def one_page(cls):
        f = TestFile()
        f.file_name = "one-page.docx"
        f.folder = "words\\docx\\"
        return f

    @classmethod
    def template_document_docx(cls):
        f = TestFile()
        f.file_name = "template-document.docx"
        f.folder = "words\\docx\\"
        return f

    @classmethod
    def formatted_document(cls):
        f = TestFile()
        f.file_name = "formatted-document.docx"
        f.folder = "words\\docx\\"
        return f

    @classmethod
    def encoding_detection(cls):
        f = TestFile()
        f.file_name = "encoding-detection.txt"
        f.folder = "words\\txt\\"
        return f

    @classmethod
    def zip(cls):
        f = TestFile()
        f.file_name = "docx.zip"
        f.folder = "containers\\archive\\"
        return f

    @classmethod
    def zip_with_email_image_pdf(cls):
        f = TestFile()
        f.file_name = "zip-eml-jpg-pdf.zip"
        f.folder = "containers\\archive\\"
        return f

    @classmethod
    def jpeg_file(cls):
        f = TestFile()
        f.file_name = "document.jpeg"
        f.folder = "image\\jpeg\\"
        return f

    @classmethod
    def image_and_attachment(cls):
        f = TestFile()
        f.file_name = "embedded-image-and-attachment.eml"
        f.folder = "email\\eml\\"
        return f

    @classmethod
    def pdf_container(cls):
        f = TestFile()
        f.file_name = "PDF with attachements.pdf"
        f.folder = "pdf\\"
        f.password = "password"
        return f

    @classmethod
    def pdf(cls):
        f = TestFile()
        f.file_name = "template-document.pdf"
        f.folder = "pdf\\"
        return f

    @classmethod
    def rar(cls):
        f = TestFile()
        f.file_name = "sample.rar"
        f.folder = "containers\\archive\\"
        return f

    @classmethod
    def tar(cls):
        f = TestFile()
        f.file_name = "sample.tar"
        f.folder = "containers\\archive\\"
        return f

    @classmethod
    def md(cls):
        f = TestFile()
        f.file_name = "sample.md"
        f.folder = "words\\docx\\"
        return f

    @classmethod
    def not_exist(cls):
        f = TestFile()
        f.file_name = "file-not-exist.pdf"
        f.folder = "folder\\"
        return f

    @classmethod
    def get_test_files(cls):
        return [
            cls.password_protected(),
            cls.four_pages(),
            cls.one_page(),
            cls.template_document_docx(),
            cls.formatted_document(),
            cls.encoding_detection(),
            cls.zip(),
            cls.zip_with_email_image_pdf(),
            cls.jpeg_file(),
            cls.image_and_attachment(),
            cls.pdf(),
            cls.pdf_container(),
            cls.rar(),
            cls.tar(),
            cls.md()
        ]

    def ToFileInfo(self):
        f = FileInfo()
        f.file_path = self.folder + self.file_name
        if hasattr(self, 'password'):
            f.password = self.password
        return f
