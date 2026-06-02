
# Provenance and purpose of this repository

This repository originated as a fork of [microsoftgraph/msgraph-metadata](https://github.com/microsoftgraph/msgraph-metadata).  The intention is to derive a `stackql` provider from this source, organized into the traditional hierarchy per existing providers in [stackql/stackql-provider-registry](https://github.com/stackql/stackql-provider-registry).  Briefly, these are a collection, per provider, of one single `provider` file and a bunch of `service` files, all are `yaml`, and the `service` files are extensions on `openapi`.

For this repository, we want all `entra_id` functionality exposed.

A couple of hints:

- A related derivation is implemented in [stackql-registry/stackql-provider-azure](https://github.com/stackql-registry/stackql-provider-azure).
- The `nodejs` library [stackql/provider-utils](https://www.npmjs.com/package/@stackql/provider-utils) is heavily used throughout simlar translation implementations.

## Expectations

- A fully funtional an canonical provider for `entra_id`.

