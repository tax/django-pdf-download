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

Default: *download.pdf*

**pdf_folder**

The folder where the pdf files are saved.

Default: *'/tmp/'*

**pdf_remove_file**
If true then created files are removed after creation.

Default: *True*


**pdf_authenticate**
Authenticate the request to fetch the webpage for print *(current user of PDF download request is used)*
Default: *True*

**pdf_load_time**
Default: *2* seconds

**pdf_get_param**
GET parameter to indicate file should be downloaded as pdf: *(Example: http://mysite.com/mypage/?pdf willl download page as PDF)*
Default: *'pdf'*



## Installation

```
$ pip install django-pdf-download
```
System requirements tested on (ubuntu 14.04):
```
sudo apt-get install firefox xvfb cups-pdf
```

*cups-pdf* is only used once to setup headless printing (quirk in firefox you can not save as PDF unless you printed via another printer at least once). 

You can do this by running the following command (available after installation of the package):

```
$ activate_headless_print 
```



