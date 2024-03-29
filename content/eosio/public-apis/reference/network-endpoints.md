---
weight: 20
title: Available Antelope (EOSIO) Networks (Endpoints)
sideNavTitle: Network Endpoints
aliases:
  - /reference/eosio/endpoints/
  - /eosio/public-apis/reference/eosio-networks-endpoints/
  - /eosio/public-apis/reference/available-networks-endpoints/
---

The _dfuse_ API is available for multiple Antelope (EOSIO) networks. See {{< external-link title="dfuse plans" href="https://dfuse.eosnation.io/" >}} for details. Should you need dfuse on another network that is not listed here, please {{< external-link title="contact us" href="https://eosnation.io/contact-us/" >}}.

## EOS Mainnet

Chain ID: `aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906`

| Resource       | URL                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| dfuse Home     | https://eos.dfuse.eosnation.io                                                                                                  |
| Authentication | https://auth.eosnation.io/v1/auth/issue                                                                                         |
| WebSocket      | wss://eos.dfuse.eosnation.io/v1/stream                                                                                          |
| REST           | https://eos.dfuse.eosnation.io/                                                                                                 |
| GraphQL over HTTP | https://eos.dfuse.eosnation.io/graphql                                                                                       |
| GraphQL over WebSocket | wss://eos.dfuse.eosnation.io/graphql                                                                                    |
| GraphQL over gRPC | eos.dfuse.eosnation.io:9000                                                                                                  |
| GraphQL Examples & References | {{< external-link title="GraphiQL" href="https://eos.dfuse.eosnation.io/graphiql/" >}}                           |

The following fields are indexed for searching: account, action, auth, data.abi, data.account, data.active, data.active_key, data.actor, data.amount, data.asset_id, data.assetid, data.assetidc, data.asset_ids, data.assetids, data.asset_owner, data.auth, data.author, data.authority, data.bid, data.bidder, data.canceler, data.category, data.claimer, data.code, data.collection_name, data.creator, data.executer, data.from, data.ftofferids, data.ftofferids, data.is_active, data.is_priv, data.isproxy, data.issuer, data.level, data.location, data.maximum_supply, data.name, data.new_asset_owner, data.newname, data.newowner, data.offer_id, data.owner, data.parent, data.payer, data.period, data.permission, data.producer, data.producer_key, data.producers, data.proposal_hash, data.proposal_name, data.proposer, data.proxy, data.public_key, data.quant, data.quantity, data.ram_payer, data.receiver, data.recipient, data.recipient_asset_ids, data.requested, data.requirement, data.schema_name, data.sender, data.sender_asset_ids, data.sym, data.symbol, data.template_id, data.threshold, data.to, data.transfer, data.voter, data.voter_name, data.weight, db.key, db.table, event, input, notif, ram.consumed, ram.released, receiver, scheduled, status

The following transaction and account filters are applied: account == 'eidosonecoin' || receiver == 'eidosonecoin' || (account == 'eosio.token' && (data.to == 'eidosonecoin' || data.from == 'eidosonecoin')) || account == 'eosiopowcoin' || receiver == '
eosiopowcoin' || (account == 'eosio.token' && (data.to == 'eosiopowcoin' || data.from == 'eosiopowcoin'))

## WAX Mainnet

Chain ID: `1064487b3cd1a897ce03ae5b6a865651747e2e152090f99c1d19d44e01aea5a4`

| Resource       | URL                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| dfuse Home     | https://wax.dfuse.eosnation.io                                                                                                  |
| Block Explorer | https://wax.eosq.eosnation.io                                                                                                   |
| Authentication | https://auth.eosnation.io/v1/auth/issue                                                                                         |
| WebSocket      | wss://wax.dfuse.eosnation.io/v1/stream                                                                                          |
| REST           | https://wax.dfuse.eosnation.io/                                                                                                 |
| GraphQL over HTTP | https://wax.dfuse.eosnation.io/graphql                                                                                       |
| GraphQL over WebSocket | wss://wax.dfuse.eosnation.io/graphql                                                                                    |
| GraphQL over gRPC | wax.dfuse.eosnation.io:9000                                                                                                  |
| GraphQL Examples & References | {{< external-link title="GraphiQL" href="https://wax.dfuse.eosnation.io/graphiql/" >}}                           |

The following fields are indexed for searching: account, action, auth, data.abi, data.account, data.active, data.active_key, data.actor, data.amount, data.asset_id, data.assetid, data.assetidc, data.asset_ids, data.assetids, data.asset_owner, data.auth, data.author, data.authority, data.bid, data.bidder, data.canceler, data.category, data.claimer, data.code, data.collection_name, data.creator, data.executer, data.from, data.ftofferids, data.ftofferids, data.is_active, data.is_priv, data.isproxy, data.issuer, data.level, data.location, data.maximum_supply, data.name, data.new_asset_owner, data.newname, data.newowner, data.offer_id, data.owner, data.parent, data.payer, data.period, data.permission, data.producer, data.producer_key, data.producers, data.proposal_hash, data.proposal_name, data.proposer, data.proxy, data.public_key, data.quant, data.quantity, data.ram_payer, data.receiver, data.recipient, data.recipient_asset_ids, data.requested, data.requirement, data.schema_name, data.sender, data.sender_asset_ids, data.sym, data.symbol, data.template_id, data.threshold, data.to, data.transfer, data.voter, data.voter_name, data.weight, db.key, db.table, event, input, notif, ram.consumed, ram.released, receiver, scheduled, status

The following transaction and account filters are applied: 'm.federation' || receiver == 'm.federation' || (account == 'eosio.token' && (data.to == 'm.federation' || data.from == 'm.federation'))

## Kylin Testnet

Chain ID: `5fff1dae8dc8e2fc4d5b23b2c7665c97f9e9d8edf2b6485a86ba311c25639191`

| Resource       | URL                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| dfuse Home     | https://kylin.dfuse.eosnation.io                                                                                                |
| Block Explorer | https://kylin.eosq.eosnation.io                                                                                                 |
| Authentication | https://auth.eosnation.io/v1/auth/issue                                                                                         |
| WebSocket      | wss://kylin.dfuse.eosnation.io/v1/stream                                                                                        |
| REST           | https://kylin.dfuse.eosnation.io/                                                                                               |
| GraphQL over HTTP | https://kylin.dfuse.eosnation.io/graphql                                                                                     |
| GraphQL over WebSocket | wss://kylin.dfuse.eosnation.io/graphql                                                                                  |
| GraphQL over gRPC | kylin.dfuse.eosnation.io:9000                                                                                                |
| GraphQL Examples & References | {{< external-link title="GraphiQL" href="https://kylin.dfuse.eosnation.io/graphiql/" >}}                         |

The following fields are indexed for searching: account, action, auth, data.abi, data.account, data.active, data.active_key, data.actor, data.amount, data.asset_id, data.assetid, data.assetidc, data.asset_ids, data.assetids, data.asset_owner, data.auth, data.author, data.authority, data.bid, data.bidder, data.canceler, data.category, data.claimer, data.code, data.collection_name, data.creator, data.executer, data.from, data.ftofferids, data.ftofferids, data.is_active, data.is_priv, data.isproxy, data.issuer, data.level, data.location, data.maximum_supply, data.name, data.new_asset_owner, data.newname, data.newowner, data.offer_id, data.owner, data.parent, data.payer, data.period, data.permission, data.producer, data.producer_key, data.producers, data.proposal_hash, data.proposal_name, data.proposer, data.proxy, data.public_key, data.quant, data.quantity, data.ram_payer, data.receiver, data.recipient, data.recipient_asset_ids, data.requested, data.requirement, data.schema_name, data.sender, data.sender_asset_ids, data.sym, data.symbol, data.template_id, data.threshold, data.to, data.transfer, data.voter, data.voter_name, data.weight, db.key, db.table, event, input, notif, ram.consumed, ram.released, receiver, scheduled, status

## Jungle 4 Testnet (experimental)

Chain ID: `73e4385a2708e6d7048834fbc1079f2fabb17b3c125b146af438971e90716c4d`

| Resource       | URL                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| dfuse Home     | https://jungle4.dfuse.eosnation.io                                                                                              |
| Block Explorer | https://jungle4.eosq.eosnation.io                                                                                               |
| Authentication | https://auth.eosnation.io/v1/auth/issue                                                                                         |
| WebSocket      | wss://jungle4.dfuse.eosnation.io/v1/stream                                                                                      |
| REST           | https://jungle4.dfuse.eosnation.io/                                                                                             |
| GraphQL over HTTP | https://jungle4.dfuse.eosnation.io/graphql                                                                                   |
| GraphQL over WebSocket | wss://jungle4.dfuse.eosnation.io/graphql                                                                                |
| GraphQL over gRPC | jungle4.dfuse.eosnation.io:9000                                                                                              |
| GraphQL Examples & References | {{< external-link title="GraphiQL" href="https://jungle4.dfuse.eosnation.io/graphiql/" >}}                       |

The following fields are indexed for searching: account, action, auth, data.abi, data.account, data.active, data.active_key, data.actor, data.amount, data.asset_id, data.assetid, data.assetidc, data.asset_ids, data.assetids, data.asset_owner, data.auth, data.author, data.authority, data.bid, data.bidder, data.canceler, data.category, data.claimer, data.code, data.collection_name, data.creator, data.executer, data.from, data.ftofferids, data.ftofferids, data.is_active, data.is_priv, data.isproxy, data.issuer, data.level, data.location, data.maximum_supply, data.name, data.new_asset_owner, data.newname, data.newowner, data.offer_id, data.owner, data.parent, data.payer, data.period, data.permission, data.producer, data.producer_key, data.producers, data.proposal_hash, data.proposal_name, data.proposer, data.proxy, data.public_key, data.quant, data.quantity, data.ram_payer, data.receiver, data.recipient, data.recipient_asset_ids, data.requested, data.requirement, data.schema_name, data.sender, data.sender_asset_ids, data.sym, data.symbol, data.template_id, data.threshold, data.to, data.transfer, data.voter, data.voter_name, data.weight, db.key, db.table, event, input, notif, ram.consumed, ram.released, receiver, scheduled, status
