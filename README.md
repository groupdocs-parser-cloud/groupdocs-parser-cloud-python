# GroupDocs.Parser Cloud Python SDK
Python package for communicating with the GroupDocs.Parser Cloud API. This SDK allows you to work with GroupDocs.Parser Cloud REST APIs in your python applications.

## Requirements

Python 3.4+

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
# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to parse a document using template object.
class ParseByTemplateDefinedAsAnObject:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.ParseOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "words-processing/docx/companies.docx"
        options.template = Common.GetTemplate()

        request = groupdocs_parser_cloud.ParseRequest(options)
        result = parseApi.parse(request)
        
        for data in result.fields_data:
            if data.page_area.page_text_area is not None:
                print("Field name: " + data.name + ". Text :" + data.page_area.page_text_area.text)

            if data.page_area.page_table_area is not None:
                print("Table name: " + data.name)
                for cell in data.page_area.page_table_area.page_table_area_cells:
                    print("Table cell. Row " + str(cell.row_index) + " column " + str(cell.column_index) + ". Text: " + cell.page_area.page_text_area.text);
```


## Licensing
GroupDocs.Parser Cloud Python SDK licensed under [MIT License](http://github.com/groupdocs-parser-cloud/groupdocs-parser-cloud-python/LICENSE).

## Resources
+ [**Website**](https://www.groupdocs.cloud)
+ [**Product Home**](https://products.groupdocs.cloud/parser)
+ [**Documentation**](https://docs.groupdocs.cloud/display/parsercloud/Home)
+ [**Free Support Forum**](https://forum.groupdocs.cloud/c/parser)
+ [**Blog**](https://blog.groupdocs.cloud/category/parser)

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.groupdocs.cloud/c/parser).