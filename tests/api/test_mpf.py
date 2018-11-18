import unittest

from eocdb_client.api.mpf import MultiPartForm
from tests.helpers import ClientTest


class MultiPartFormTest(unittest.TestCase):

    def test_it(self):
        form = MultiPartForm(boundary="bibo")

        form.add_field("path", "BIGELOW/BALCH/gnats")

        file_obj = ClientTest.get_input_path("chl", "chl-s170604w.sub")
        form.add_file("datasetFiles",
                      "chl/chl-s170604w.sub",
                      file_obj)

        file_obj = open(ClientTest.get_input_path("chl", "chl-s170710w.sub"))
        try:
            form.add_file("datasetFiles",
                          "chl/chl-s170710w.sub",
                          file_obj)
        finally:
            file_obj.close()

        binary_form = bytes(form)
        self.assertGreater(len(binary_form), 3500)

        text_form = str(form)
        self.assertGreater(len(text_form), 3500)
        self.assertTrue(text_form.startswith("--bibo\r\n"))
        self.assertTrue(text_form.endswith("--bibo--\r\n"))
