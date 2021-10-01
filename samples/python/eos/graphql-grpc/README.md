## dfuse GraphQL Python Example

This simple program demonstrates how easy it is to query our GraphQL API over gRPC in Python. It:

* Request a token from our authentication API
* Creates a gRPC connection with credentials
* Instantiates a GraphQL client
* Executes a simple GraphQL query
* Prints the response

### Requirements

You will need to have Python3 (>= 3.4+) as well as `virtualenv` and `pip`
`>= 15.0+`.

We use a virtual environment for this example, all dependencies are listed
in the `requirements.txt` at the root of this project.

#### Quickstart

First of all, visit [https://dfuse.eosnation.io](https://dfuse.eosnation.io) to get
a free API key for your project.

Setup the virtual environment and pull all dependencies:

```bash
./install_deps.sh
```

Once your environment is setup properly, simply run the `example.py` script:

```bash
python3 example.py YOUR_API_KEY_HERE
```

If you have problems connecting to grpc with errors like `Handshake failed with fatal error SSL_ERROR_SSL: error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED.`, then remove the "DST Root CA X3" entry from ./env/lib/python3.9/site-packages/grpc/_cython/_credentials/roots.pem or similar file.
