# What is this

This is a class based mixin to download a page as PDF.

The PDF is generated with firefox and selenium **(tested on ubuntu 14.04 LTS)**.


## Example usage:
```python

class InvoiceDetail(PdfDownloadMixin, DetailView):
    model = Invoice
    queryset = Invoice.objects.all().select_related()
    context_object_name = 'invoice'
    template_name = "invoice_print.html"
    # PDF mixin attributes
    pdf_filename = 'invoice.pdf'

```

## Options:

```pdf_filename```
The filename of the PDF file download.
Default: download.pdf

```pdf_folder = '/tmp/'
```pdf_remove_file```
Default: ```python True```
```pdf_authenticate```
Default: True
```pdf_load_time```
Default: True
```pdf_get_param```
Default: 'pdf'



## Installation
```
$ pip install django-pdf-download
```
System requirements tested on (ubuntu 14.04):
```
sudo apt-get install firefox cups-pdf xvfb
```

*cups-pdf* is only used once to setup headless printing.

