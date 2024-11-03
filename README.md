# 🚧 Deprecation Notice

dfuse services will be discontinued on **September 25, 2024**, as Pinax transitions to more advanced and efficient solutions for Antelope blockchain data sourcing. We encourage all users to migrate to Pinax's new services, including **Substreams, Firehose**, and comprehensive blockchain data services supporting dozens of chains like EOS, WAX, and Telos. Dfuse users can start building with a **FREE Pinax Pro Plan**.

Learn more and get started at https://pinax.network.

# dfuse Documentation

We welcome contributions to improve the documentation. Simply open a pull request to start collaborating!

## Requirements

- Hugo **Extended** (with SCSS support), version 0.58.3 or higher
  - Install corresponding `hugo_extended_*` package from [binaries](https://github.com/gohugoio/hugo/releases), or
  - Build from source code
  ```
  git checkout github.com/gohugoio/hugo
  cd hugo
  CGO_ENABLED=1
  go install -v --tags extended
  ```

## Development

To start the hugo server, run this command:

```sh
hugo server
```

### GraphQL API Reference

The GraphQL API Reference content is generated straight from the GraphQL schema of the different products
we support.

To update them, a pre-defined project layout on disk is expected by the script. You must have the three
following project colocated as siblings alongside the `dfuse-docs` project:

- `dfuse-docs`
- `dfuse-eosio`

The later two must be named verbatim, the first one `dfuse-docs` could be named whatever you like. Once the
following layout exist on your local workstation, to update the GraphQL generate API reference data,
first install the script dependencies:

```
npm install
```

Then run the following command:

```
node graphql.js
```

This should update the file `data/eos/graphql.json` (and any other
chains we now support) if the GraphQL schema has been updated.

## Content Structure

All content can be found in the `/content` directory. The structure of the website is generated automatically based on the structure of that directory.

## Style guide

### Links

- [1.1](#types--primitives) **external**: When you insert an external link use the `external-link` shortcode

  ```markdown
  {{< external-link href="https://dfuse.eosnation.io" title="dfuseio" >}}
  {{< external-link href="https://dfuse.eosnation.io">}}
  ```

- [1.2](#types--primitives) **internal references**: Please put all _internal references_ as _full paths_, for greppability and refactoring.

### Example code

Use the following begin and end tags to indicate code sections that need to be referenced:

```javascript
// CODE:BEGIN:quickstarts_javascript_node_eos_section1
function() {
  var some = "code"
}
// CODE:END:quickstarts_javascript_node_eos_section1
```

Section names need to follow the path of the file from project root.
For example the example snippet is from the file:

```markdown
├── quickstarts
│   └── javascript
│       └── node
│           └── index.eos.js
├── guides
└── ...
```

When hugo builds the site, the code sections are extracted and stored in the `data` folder in project root.
Example code can then be referenced with the following shortcode:
```go
{{< code-section "quickstarts_javascript_node_eos_section1" >}}
```

## Lexicon guide

- web application
- website
- dfuse
- real-time
- GraphQL
- API

## Deployment

Any commit to master automatically triggers a deployment. For this reason, the master branch is locked, requiring all changes to go through an approved pull request.


```

```
