import unittest
import os

from django.test.client import RequestFactory
from django.conf import settings

from pdfdownload import PdfDownloadMixin, save_pdf


# Configure django settings
settings.configure()
settings.ALLOWED_HOSTS = '*'


class TestPDFDownload(unittest.TestCase):

    def test_methods(self):
        obj = PdfDownloadMixin()
        self.assertTrue(obj.pdf_authenticate)
        self.assertTrue(obj.pdf_remove_file)
        self.assertEqual(obj.get_pdf_attachment_name(), 'download.pdf')
        self.assertEqual(obj.get_pdf_location(), '/tmp/download.pdf')

    def test_get_pdf_url(self):
        obj = PdfDownloadMixin()
        rf = RequestFactory()
        req = rf.get('/test/invoice?pdf')
        self.assertEqual(obj.get_pdf_location(), '/tmp/download.pdf')
        obj.get_pdf_url(req)

    def test_get_pdf_cookie(self):
        obj = PdfDownloadMixin()
        obj.pdf_authenticate = False
        rf = RequestFactory()
        req = rf.get('/test/invoice?pdf')
        self.assertEqual(obj.get_pdf_cookie(req), None)

    def test_pdf_generation(self):
        filename = '/tmp/test.pdf'
        url = 'http://www.google.com'
        save_pdf(url, filename=filename)
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(os.path.getsize(filename) > 0)
        os.remove(filename)

        obj = PdfDownloadMixin()
        obj.pdf_authenticate = False
        data = obj._return_pdf(url)
        # Check if PDF contains data
        self.assertTrue(data.len > 0)


if __name__ == '__main__':
    unittest.main()
