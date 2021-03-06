---
weight: 20
title: Authentication
aliases:
  - /guides/core-concepts/authentication/
  - /notions/authentication/
---

For protocol-specific ways of passing authentication, please refer to each protocol:

* [EOSIO-specific authentication docs]({{< ref "/eosio/public-apis/reference/authentication" >}})


## Types of keys

There are two sorts of keys in the dfuse ecosystem:

1. A long-lived API key - will resemble `server_abcdef123123123000000000000000000`, used to generate short-lived <a href="https://jwt.io/" title="JSON Web Tokens">JWT</a>.
2. A short-lived JWT - used when performing any call on the dfuse Platform, which looks like:

{{< tabs "auth-token" >}}
{{< tab lang="shell" title="JWT token" >}}
eyJhbGciOiJLTVNFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTYxMzI4MjAsImp0aSI6IjQwNWVmOTUxLTAwZTYtNGJmNC1hZWMxLTU0NTU1ZWMzMTUwMiIsImlhdCI6MTU1NjA0NjQyMCwiaXNzIjoiZGZ1c2UuaW8iLCJzdWIiOiJ1aWQ6MHdlbnU2NmUwNzU4OWRhODY4MWNlIiwiYWtpIjoiM2NhYWEzYzA3M2FlZjVkMmYxOGUwNjJmZDkzYzg3YzMzYWIxYzA1YzEzNjI3NjU2OTgzN2Y5NDc5NzZlMjM0YSIsInRpZXIiOiJmcmVlLXYxIiwic3RibGsiOi0zNjAwLCJ2IjoxfQ.000HeTujIuS_LRvvPN6ZRCmtoZqZyV6P1enNBviwK8v7Tf7BLHJIrEpQoEREKSIMdZWPrMQl_OE55yJP0MxUDA
{{< /tab >}}
{{< /tabs >}}

## Obtaining a Long-Lived API Key

Once you have created an account through the <a href="https://dfuse.eosnation.io" title="dfuse API Portal">dfuse portal</a> you will be able to obtain an API key.

1. Click on "GENERATE NEW KEY" and you'll now be able to start
customizing your key for your specific needs.
2. Assign the API
key a name so that you'll be able to differentiate it from other API
keys that you generate.

## Obtaining a Short-Lived JWT

Once you have this API key, call the `https://auth.eosnation.io/v1/auth/issue` endpoint to obtain a fresh Authentication Token using the following command. **Do not forget to replace the API key by your own!**

{{< tabs "jwt-requests" >}}
{{< tab lang="shell" >}}
curl -XPOST \
  -H "Content-Type: application/json" \
  --data '{"api_key":"web_abcdef12345678900000000000"}' \
  "https://auth.eosnation.io/v1/auth/issue"
{{< /tab >}}

{{< tab lang="javascript" >}}
fetch("https://auth.eosnation.io/v1/auth/issue", {
  method: "POST",
  body: JSON.stringify({
    api_key: "web_abcdef12345678900000000000"
  }),
  headers: {
    "Content-Type": "application/json"
  }
})
.then(res => res.json())
.then(console.log) // Cache JWT (for up to 24 hours)
{{< /tab >}}

{{< tab lang="python" >}}
import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"api_key":"web_abcdef12345678900000000000"}'

# Cache JWT response (for up to 24 hours)
response = requests.post('https://auth.eosnation.io/v1/auth/issue', headers=headers, data=data)
{{< /tab >}}

{{< tab lang="go" >}}
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	client := &http.Client{}
	var data = []byte(`{{"api_key":"web_abcdef12345678900000000000"}}`)
	req, err := http.NewRequest("POST", "https://auth.eosnation.io/v1/auth/issue", data)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("Content-Type", "application/json")
	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	bodyText, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

  // Cache JWT response (for up to 24 hours)
	fmt.Printf("%s\n", bodyText)
}
{{< /tab >}}


{{< tab lang="bash" title=".bashrc" >}}
# Use this in your .bashrc to speed your development environment

# Replace this variable by an API key you got from https://dfuse.eosnation.io
export DFUSE_KEY=web_abcdef12345678900000000000
function dfusetoken {
    DFUSE_TOKEN=$(curl https://auth.eosnation.io/v1/auth/issue -s --data-binary '{"api_key":"'$DFUSE_KEY'"}' | jq -r .token)
    export DFUSE_TOKEN
}
{{< /tab >}}

{{< /tabs >}}

The return value from the API:

{{< tabs "issuing-jwt-response">}}
{{< tab title="Response" lang="json" >}}
{
  "token":"eyJhbGciOiJLTVNFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTYxMzI4MjAsImp0aSI6IjQwNWVmOTUxLTAwZTYtNGJmNC1hZWMxLTU0NTU1ZWMzMTUwMiIsImlhdCI6MTU1NjA0NjQyMCwiaXNzIjoiZGZ1c2UuaW8iLCJzdWIiOiJ1aWQ6MHdlbnU2NmUwNzU4OWRhODY4MWNlIiwiYWtpIjoiM2NhYWEzYzA3M2FlZjVkMmYxOGUwNjJmZDkzYzg3YzMzYWIxYzA1YzEzNjI3NjU2OTgzN2Y5NDc5NzZlMjM0YSIsInRpZXIiOiJmcmVlLXYxIiwic3RibGsiOi0zNjAwLCJ2IjoxfQ.000HeTujIuS_LRvvPN6ZRCmtoZqZyV6P1enNBviwK8v7Tf7BLHJIrEpQoEREKSIMdZWPrMQl_OE55yJP0MxUDA",
  "expires_at":1556132820
}
{{< /tab >}}
{{< /tabs >}}

{{< method-list-item name="token" type="String" required="true" >}}
  The JWT to be used with all API calls, including WebSocket.
{{< /method-list-item >}}

{{< method-list-item name="expires_at" type="Timestamp" required="true" >}}
  An UNIX timestamp (UTC) indicating when the JWT will expire.
{{< /method-list-item >}}

Our [client-js](/libraries) library will handle the token issuance and caching for you if you decide to utilize it. You can also consult a [working reference example](https://github.com/dfuse-io/client-js/blob/master/examples/reference/auth-issue.ts) if you would like to follow along with some sample TypeScript code.

{{< alert type="tip" >}}
To learn more about JWTs, you can consult <https://jwt.io/introduction/>.
{{< /alert >}}

Each JWT is **valid for a period of 24 hours**. Make sure to cache those values to avoid hitting rate limiting on JWT issuance.

{{< alert type="note" >}}
The token will be **validated** only **upon connection establishment**, and will **never provoke** a **disconnection** even if it expires during that connection's lifetime.
{{< /alert >}}



## Lifecycle of Short-Lived JWTs

Each JWT has an expiration date, so it is important to take that into account before making a request to the dfuse APIs. Here is the recommended procedure to take before making a request:

1. Retrieve the JWT, and examine it's expiration time
1. If the JWT is past its expiration time, is near expiration, or is absent from cache, fetch a new one through the [`/v1/auth/issue`](#obtaining-a-short-lived-jwt) endpoint, and cache the response.
1. Call _dfuse_ with the valid JWT token.

Each time you get a fresh JWT, it contains the updated expiration time and the token itself.


## GraphQL Authentication

Using the {{< external-link title="apollo-client" href="https://www.apollographql.com/docs/react/) websocket protocol, the `INIT` message should contain an `Authorization` key, with the same format as the REST authentication (bearer token" >}}.

When doing `POST` calls to the `/graphql` endpoint, you must specify the `Authorization` header, exactly like any other REST calls.

## GraphQL over gRPC Authentication

Using the language of your choice, use the `OAuth2` authentication method with gRPC. Set the `OAuth2 Access Token` to be your JWT, and if required, specify `Bearer` as the method. This will set the `authorization` gRPC header, similiar to the HTTP header of the same name.

Refer to the {{< external-link href="https://grpc.io/docs/guides/auth/" title="official gRPC guides" >}} to see how to apply it to your language of choice.
