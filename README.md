## What is this

This is a class based mixin to download a class based view as a PDF.

The PDF is generated with firefox and selenium **(tested on ubuntu 14.04 LTS)**.

This is not really performant but generates good PDF's with selectable text.

This is how this is done:


## Example usage:
```python

class InvoiceDetail(PdfDownloadMixin, TemplateView):
    template_name = "invoice_print.html"
    # PDF mixin attributes
    pdf_filename = 'invoice.pdf'

```

## Options:

**pdf_filename**

The filename of the PDF file download.
Default: download.pdf

**pdf_folder = '/tmp/'**

**pdf_remove_file**
Default: **python True**

**pdf_authenticate**
Default: True

**pdf_load_time**
Default: True

**pdf_get_param**
Default: 'pdf'



## Installation

```
$ pip install django-pdf-download
```
System requirements tested on (ubuntu 14.04):
```
sudo apt-get install firefox xvfb cups-pdf
```

*cups-pdf* is only used once to setup headless printing (quirk in firefox you can not save as PDF unless you printed via another printer at least once).

