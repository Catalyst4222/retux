# retux.client

This is the `client` namespace of retux. Here, all of our important client-facing code is stored.

## Architecture

The architecture of this namespace is simple:

- `resources`: All of our dataclasses for API-related objects. Examples include `retux.Guild`, `retux.User`, and etc.
- `bot.py`: The main entry point for creating bot applications. Any and everything that involves working with a bot is stored in here.
- `flags.py`: The flags for bot applications. This will mainly include:
  - `retux.Intents` for representing Gateway intents upon connecting.
  - `retux.Permissions` for representing permissions for hierarchical processes, such as banning, timeouts, and etc.
- `mixins.py`: Builders and traits that can be ran on a given resource dataclass from `resources`. Some examples are:
  - `retux.Editable` for being able to edit/modify and delete a resource from the API.
  - `retux.Controllable` for being able to "get" via. cache or HTTP, and creating a resource from the API.
