---
weight: 70
title: dfuse Events
aliases:
  - /reference/eosio/dfuse-events/
---

dfuse Events are a powerful way to give smart contract developers a way to ask dfuse Search to index their transactions, with arbitrary key/value pairs.

By simply instructing your smart contract to send an inline action to `dfuseiohooks:event`, you can instruct dfuse Search to index some fields with arbitrary data (within limits).

Once on chain, the search term `event.field:value` will allow you to retrieve those actions, anywhere on the dfuse Platform.

{{< alert type="note" >}}
See the [Using dfuse Events tutorial]({{< ref "eosio/public-apis/tutorials/using-dfuse-events" >}}) for a concrete example.
{{< /alert >}}

**Availability**: This feature is available on **EOS Mainnet** and **Kylin Testnet** networks.

**Destination**: The inline action must be sent to contract `dfuseiohooks` with the action name `event`. The action signature is: `event(string auth_key, string data)`.

**Cost**: be cheap, and use an inline _context-free_ action to have minimal impact on transaction costs.  Also, there will never be code deployed on `dfuseiohooks`, so it will always execute extremely fast.

**Authorization**: Specify no authorization (`std::vector<permission_level>()`) when issuing a _context-free_ action.

**Indexing**: Only ONE such event per action will be indexed. If limits aren't breached, the parameters in `data` will be indexed as `event.field` in _dfuse Search_, attached to the action that **created** the inline to `dfuseiohooks:event`.  This allows you to search for `receiver:yourcontract event.field:value` or other combinations.

## Action parameters

Name | Type | Options | Description
-----|------|---------|------------
`auth_key` | string | required | The empty string (limited access) or a valid _dfuse Events Key_ if you have one. See [Indexing Limits](#indexing-limits) for details.
`data` | string | required | A string containing the key/value pair list to index, as an {{< external-link title="RFC 3986" href="https://tools.ietf.org/html/rfc3986) URL encoded string (i.e. `key1=value1&key2=value2`" >}}.

## Indexing Limits

An empty `auth_key` parameter imposes those limits to the indexing:

- A key/value pair under `data` is indexed only if:
    - the key has 16 characters or less
    - the value has 64 characters or less
    - there are no more than 3 keys (for unauthenticated calls)

If you need more than 3 key/values or want more than 64 bytes of value data, contact us to get a _dfuse Events Key_ for your contract.

{{< alert type="note" >}}
If your `auth_key` is invalid or used within the wrong contract account, normal restrictions apply.
{{< /alert >}}

### Technical details

Contract source: https://github.com/dfuse-io/dfuseiohooks

Deployment:
* https://eos.eosq.eosnation.io/account/dfuseiohooks/abi
* https://kylin.eosq.eosnation.io/account/dfuseiohooks/abi
