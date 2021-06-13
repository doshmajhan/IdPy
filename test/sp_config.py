from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
from saml2.saml import NAME_FORMAT_URI

try:
    from saml2.sigver import get_xmlsec_binary
except ImportError:
    get_xmlsec_binary = None


if get_xmlsec_binary:
    xmlsec_path = get_xmlsec_binary(["/opt/local/bin", "/usr/local/bin"])
else:
    xmlsec_path = "/usr/local/bin/xmlsec1"

# Make sure the same port number appear in service_conf.py
BASE = "http://localhost:8080"

CONFIG = {
    "entityid": BASE,
    "description": "Mock SP",
    "service": {
        "sp": {
            "want_response_signed": True,
            "authn_requests_signed": True,
            "logout_requests_signed": True,
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/acs/post" % BASE, BINDING_HTTP_POST)
                ],
                "single_logout_service": [
                    ("%s/slo/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/slo/post" % BASE, BINDING_HTTP_POST),
                ],
            },
        },
    },
    "key_file": "test/pki/key.pem",
    "cert_file": "test/pki/cert.pem",
    "xmlsec_binary": xmlsec_path,
    "name_form": NAME_FORMAT_URI,
}
