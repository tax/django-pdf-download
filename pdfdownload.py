import time
import os
import StringIO
from urllib import urlencode
from urlparse import urlparse, urlunparse, parse_qs

from selenium import webdriver
from pyvirtualdisplay import Display

from django.http import HttpResponse
from django.conf import settings

CUPS_PDF_PRINTER = 'PDF'


def activate_headless_print():
    save_pdf('http://www.google.com', '/tmp/p.pdf', printer=CUPS_PDF_PRINTER)


def save_pdf(url, filename, cookie=None, wait_time=5, printer='Print to file'):
    display = Display(visible=0, size=(800, 600))
    display.start()
    profile = webdriver.FirefoxProfile()
    profile.set_preference('print_printer', printer)
    profile.set_preference('print.print_to_file', True)
    profile.set_preference('print.print_to_filename', filename)
    profile.set_preference('print.always_print_silent', True)
    for setting in ['footerleft', 'footerright', 'headerleft', 'headerright']:
        profile.set_preference('print.print_' + setting, '')
    driver = webdriver.Firefox(profile)
    # Wait for page load
    driver.implicitly_wait(wait_time)
    if cookie:
        # Go to root first
        parsed_uri = urlparse(url)
        driver.get('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri))
        driver.add_cookie(cookie)
    driver.get(url)
    driver.execute_script('window.print();')
    # Wait x seconds for PDF to be generated
    time.sleep(wait_time)
    driver.quit()
    display.stop()


class PdfDownloadMixin(object):
    pdf_filename = 'download.pdf'
    pdf_folder = '/tmp/'
    pdf_remove_file = True
    pdf_authenticate = True
    pdf_load_time = 2
    pdf_get_param = 'pdf'

    def get_pdf_attachment_name(self):
        return self.pdf_filename

    def get_pdf_location(self):
        return self.pdf_folder + self.pdf_filename

    def get_pdf_url(self, request):
        url = request.build_absolute_uri()
        u = urlparse(url)
        query = parse_qs(u.query)
        query.pop(self.pdf_get_param, None)
        u = u._replace(query=urlencode(query, True))
        return urlunparse(u)

    def get_pdf_cookie(self, request):
        cookie = None
        if self.pdf_authenticate:
            cookie = {
                'name': settings.SESSION_COOKIE_NAME,
                'value': request.session.session_key
            }
        return cookie

    def _return_pdf(self, url, cookie=None):
        filename = self.get_pdf_location()
        save_pdf(url, filename, cookie, wait_time=self.pdf_load_time)
        output = StringIO.StringIO()
        with open(filename, 'r') as fd:
            output.write(fd.read())
        if self.pdf_remove_file:
            os.remove(filename)
        output.seek(0)
        return output

    def dispatch(self, request, *args, **kwargs):
        if self.pdf_get_param in request.GET.keys():
            filename = self.get_pdf_attachment_name()
            url = self.get_pdf_url(request)
            cookie = self.get_pdf_cookie(request)
            pdf = self._return_pdf(url=url, cookie=cookie)
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            return response
        return super(PdfDownloadMixin, self).dispatch(request, *args, **kwargs)
