![](https://img.shields.io/badge/api-v1.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-parser-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-parser-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-parser-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-parser-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-parser-cloud/groupdocs-parser-cloud-python)](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-python/blob/master/LICENSE)

# GroupDocs.Parser Cloud Python SDK
GroupDocs.Parser Cloud SDK for Python wraps GroupDocs.Parser RESTful APIs so you may integrate **Document Parser** features in your own apps with zero initial cost.

GroupDocs.Parser Cloud API allows the developers to parse documents such as invoices, receipts or financial tables to extract text, images and metadata from 40+ popular document formats.

## Cloud Document Parser Features

- Create easy to define templates with a data field and table definitions.
- Parse documents with pre-defined templates.
- Extract data from invoices or from other sorts of documents.
- Supports extracting text and images.
- Extract data from regular documents as well as from email or archive containers.
- Obtain data from PDF portfolios.
- Fetch text fields, numbers, and tables from common documents.
- Save your templates in the storage and parse your documents with them.
- Ability to extract HTML or Markdown (MD) text for a quick preview.
- Fetch specific pages of plain as well as formatted text.
- Extract formatted (bold, italic, hyperlink, etc.) text in the MD format.
- Support for extracting text in HTML formatting (paragraph, hyperlinks, lists, etc.).
- Retrieve all images from a document and save them.
- Obtain basic information about documents, archives, emails, and attachments, etc.
- Extract data from a document contained inside a ZIP archive, email, or PDF portfolio.


## Parse Document By Template Supported Formats

- Word Processing: DOC, DOT, DOCX, DOCM, DOTX, DOTM, ODT, OTT, RTF
- Spreadsheet: XLS, XLT, XLSX, XLSM, XLSB, XLTX, XLTM, ODS, OTS, CSV, XLA, XLAM, NUMBERS
- Presentation: PPT, PPS, POT, PPTX, PPTM, POTX, POTM, PPSX, PPSM, ODP, OTP
- Portable: PDF

## Extract Text Supported Formats

- Word Processing: DOC, DOT, DOCX, DOCM, DOTX, DOTM, TXT, ODT, OTT, RTF
- Spreadsheet: XLS, XLT, XLSX, XLSM, XLSB, XLTX, XLTM, ODS, OTS, CSV, XLA, XLAM, NUMBERS
- Presentation: PPT, PPS, POT, PPTX, PPTM, POTX, POTM, PPSX, PPSM, ODP, OTP
- Portable: PDF
- Markup: HTML, XHTML, MHTML, MD, XML
- eBook: CHM, EPUB, FB2
- Emails: EML, EMLX, MSG
- Notes: ONE

## Extract Document Info Supported Formats

- Word Processing: DOC, DOT, DOCX, DOCM, DOTX, DOTM, TXT, ODT, OTT, RTF
- Spreadsheet: XLS, XLT, XLSX, XLSM, XLSB, XLTX, XLTM, ODS, OTS, CSV, XLA, XLAM, NUMBERS
- Presentation: PPT, PPS, POT, PPTX, PPTM, POTX, POTM, PPSX, PPSM, ODP, OTP
- Portable: PDF
- Markup: HTML, XHTML, MHTML, MD, XML
- eBook: CHM, EPUB, FB2
- Emails: PST, OST, EML, EMLX, MSG
- Notes: ONE
- Archives: ZIP

## Extract Images Supported Formats

- Word Processing: DOC, DOT, DOCX, DOCM, DOTX, DOTM, TXT, ODT, OTT, RTF
- Spreadsheet: XLS, XLT, XLSX, XLSM, XLSB, XLTX, XLTM, ODS, OTS, CSV, XLA, XLAM, NUMBERS
- Presentation: PPT, PPS, POT, PPTX, PPTM, POTX, POTM, PPSX, PPSM, ODP, OTP
- Portable: PDF
- Emails: EML, EMLX, MSG
- Ar5chives: ZIP

## Extract Container Items Info Supported Formats

- Portable: PDF
- Emails: PST, OST, EML, EMLX, MSG
- Archives: ZIP

## Requirements

Python 2.7 or 3.4+

## Installation
Install `groupdocs-parser-cloud` with [PIP](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/) by:

```sh
pip install groupdocs-parser-cloud
```

Or clone repository and install it via [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
python setup.py install
```

## Getting Started

Please follow the [installation procedure](#installation) and then run following:

```python
# Load the gem
import groupdocs_parser_cloud

# Get Client Id and Client Secret from https://dashboard.groupdocs.cloud
my_client_id = ""
my_client_secret = ""

# Create instance of the API
configuration = groupdocs_parser_cloud.Configuration(my_client_id, my_client_secret)
api = groupdocs_parser_cloud.InfoApi.from_config(configuration)

# Retrieve supported file-formats
response = api.get_supported_file_formats()

# Print out supported file-formats
print("Supported file-formats:")
for format in response.formats:
	print('{0} ({1})'.format(format.file_format, format.extension))

```

## Licensing
GroupDocs.Parser Cloud Python SDK licensed under [MIT License](http://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-python/LICENSE).

## GroupDocs.Parser Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js | Android |
|---|---|---|---|---|---|---|
| [GitHub](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-dotnet) | [GitHub](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-java) | [GitHub](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-php) | [GitHub](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-python) | [GitHub](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-ruby)  | [GitHub](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-node) | [GitHub](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-android) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.parser-Cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser-cloud) | [Composer](https://packagist.org/packages/groupdocscloud/groupdocs-parser-cloud) | [PIP](https://pypi.org/project/groupdocs-parser-cloud/) | [GEM](https://rubygems.org/gems/groupdocs_parser_cloud)  | [NPM](https://www.npmjs.com/package/groupdocs-parser-cloud) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser-cloud-android) |

[Home](https://www.groupdocs.cloud/) | [Product Page](https://products.groupdocs.cloud/parser/python) | [Docs](https://docs.groupdocs.cloud/parser/) | [Demo](https://products.groupdocs.app/parser/family) | [API Reference](https://apireference.groupdocs.cloud/parser/) | [Examples](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-python-samples) | [Blog](https://blog.groupdocs.cloud/category/parser/) | [Free Support](https://forum.groupdocs.cloud/c/parser) | [Free Trial](https://purchase.groupdocs.cloud/trial)
