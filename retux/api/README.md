# retux.api

This is the `api` namespace of retux. Here, all of our important API-facing code is stored.

## Architecture

The architecture of this namespace is simple:

- `events`: All of our dataclasses for Gateway event objects. Examples include `retux.GuildCreate`, `retux.GuildMemberAdd`, and etc.
- `error.py`: Exceptions and runtime error handling for our API-related clients. Some examples are:
  - `retux.InvalidToken` for when an invalid token was passed to the Gateway or HTTP client.
  - `retux.RateLimited` for when a rate limit has been reached by the Gateway or HTTP client.
- `gateway.py`: This is our Gateway client. This is very important for handling the connection to Discord to "keep alive" your bot application.
- `http.py`: This is our HTTP client. This is equally important for being able to send and process HTTP requests to Discord's Web API.
