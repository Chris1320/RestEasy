# RestEasy

Easily manage backups of your desktop, laptop, and server files using [restic](https://restic.net/).

![RestEasy Architecture](https://github.com/user-attachments/assets/26999b3f-0a82-41e1-a0cf-bb8160f4af17)

## Features

- Backup files from your local machine; You only need a one-time setup, and you can run backups with a single command.
- Install nodes on your servers to backup files from them; You can manage all your nodes from a single client.

## Installation

RestEasy has two components: the client and the node. The client is used to manage backups, while the node is installed on the machines you want to backup.

### Node Installation

1. Install [uv](https://docs.astral.sh/uv/) if you don't have it already.
2. Clone the repository and navigate to the `resteasy-node` directory:
    ```bash
    git clone https://github.com/Chris1320/RestEasy.git
    cd RestEasy/resteasy-node
    ```
3. Run RestEasy. `uv` will automatically install the dependencies.
    ```bash
    uv run -m resteasy_node           # You can run the package itself,
    uv run fastapi run resteasy_node  # or use FastAPI to run the node.
    ```

## Configuration

### Node Configuration

| Environment Variable | Type  | Description                                                                        |
| -------------------- | ----- | ---------------------------------------------------------------------------------- |
| `RESTEASY_HOST`      | `str` | Host interface to bind the node server to. Default is `127.0.0.1`.                 |
| `RESTEASY_PORT`      | `int` | Port to bind the node server to. Default is `23145`.                               |
| `RESTEASY_DEBUG`     | `str` | Enables debug mode when set to `true`.                                             |
| `RESTEASY_DATA_DIR`  | `str` | The directory where RestEasy will store its data. Default is `~/.config/resteasy`. |
