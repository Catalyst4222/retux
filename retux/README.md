# retux

This is the root namespace of retux. Everything relating to the Python module will be stored inside of here.

You may notice that there are additional namespaces:

- `client`: This represents the client-facing code. Things such as `retux.Bot` are stored in here.
- `api`: This represents the API-facing code. Things such as our Gateway and HTTP clients are stored in here.
- `utils`: This works alongside our `client` module, providing utilities for both API-facing and client-facing code.

## Accessibility

retux only exposes the `client` module. The reasoning behind this is because a developer should never need to directly
interact with the "internal" aspects, such as the `api` module for their bot applications.
