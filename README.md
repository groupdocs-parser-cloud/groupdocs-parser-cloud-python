# GroupDocs.Parser Cloud Python SDK
Python package for communicating with the GroupDocs.Parser Cloud API

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
# Import module
import groupdocs_parser_cloud

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
app_sid = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
app_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Create instance of the API
api = groupdocs_parser_cloud.InfoApi.from_keys(app_sid, app_key)

try:
    # Retrieve supported file-formats
    response = api.get_supported_file_formats()

    # Print out supported file-formats
    print("Supported file-formats:")
    for format in response.formats:
        print('{0} ({1})'.format(format.file_format, format.extension)) 
except groupdocs_parser_cloud.ApiException as e:
    print("Exception when calling get_supported_file_formats: {0}".format(e.message))
```

## Licensing
GroupDocs.Parser Cloud Python SDK licensed under [MIT License](http://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-python/LICENSE).

[Home](https://www.groupdocs.cloud/) | [Product Page](https://products.groupdocs.cloud/parser/python) | [Docs](https://docs.groupdocs.cloud/parser/) | [Demo](https://products.groupdocs.app/parser/family) | [API Reference](https://apireference.groupdocs.cloud/parser/) | [Examples](https://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-python-samples) | [Blog](https://blog.groupdocs.cloud/category/parser/) | [Free Support](https://forum.groupdocs.cloud/c/parser) | [Free Trial](https://purchase.groupdocs.cloud/trial)
