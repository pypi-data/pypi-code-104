"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.12.07
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import agilicus_api
from agilicus_api.api.catalogues_api import CataloguesApi  # noqa: E501


class TestCataloguesApi(unittest.TestCase):
    """CataloguesApi unit test stubs"""

    def setUp(self):
        self.api = CataloguesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_catalogue(self):
        """Test case for create_catalogue

        create a catalogue  # noqa: E501
        """
        pass

    def test_create_catalogue_entry(self):
        """Test case for create_catalogue_entry

        create a catalogue entry  # noqa: E501
        """
        pass

    def test_delete_catalogue(self):
        """Test case for delete_catalogue

        Delete the catalogue specified by catalogue_id  # noqa: E501
        """
        pass

    def test_delete_catalogue_entry(self):
        """Test case for delete_catalogue_entry

        Delete the catalogue specified by catalogue_entry_id  # noqa: E501
        """
        pass

    def test_get_catalogue(self):
        """Test case for get_catalogue

        Get the catalogue specified by catalogue_id  # noqa: E501
        """
        pass

    def test_get_catalogue_entry(self):
        """Test case for get_catalogue_entry

        Get the catalogue entry by id for the given catalogue  # noqa: E501
        """
        pass

    def test_list_all_catalogue_entries(self):
        """Test case for list_all_catalogue_entries

        List all catalogue entries independant of the catalogue they belong to  # noqa: E501
        """
        pass

    def test_list_catalogue_entries(self):
        """Test case for list_catalogue_entries

        List catalogue entries in the catalogue  # noqa: E501
        """
        pass

    def test_list_catalogues(self):
        """Test case for list_catalogues

        List all catalogues  # noqa: E501
        """
        pass

    def test_replace_catalogue(self):
        """Test case for replace_catalogue

        Replace the catalogue specified by catalogue_id  # noqa: E501
        """
        pass

    def test_replace_catalogue_entry(self):
        """Test case for replace_catalogue_entry

        Replace the catalogue entry specified by catalogue_entry_id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
