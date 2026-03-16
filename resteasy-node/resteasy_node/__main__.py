import os

from uvicorn import config, run
from resteasy_node import info


def _parse_envvars() -> tuple[str, int, bool, str]:
    """Parse environment variables and set defaults if necessary."""

    # TODO: Use a helper library/module for this.
    host = os.getenv("RESTEASY_HOST", "127.0.0.1")
    port = int(os.getenv("RESTEASY_PORT", "23145"))
    is_debug = os.getenv("RESTEASY_DEBUG", default="False").strip().lower() in {
        # Allow for a variety of truthy values.
        # WARN: Should we continue allowing these?
        "1",
        "true",
        "yes",
        "on",
        "y",
    }

    data_dir = os.path.abspath(
        os.path.expanduser(os.getenv("RESTEASY_DATA_DIR") or "~/.config/resteasy")
    )

    return (host, port, is_debug, data_dir)


def main():
    """The main entry point for the application."""

    print(f"Starting {info.NAME} v{info.VERSION}")
    host, port, is_debug, _ = _parse_envvars()
    run(
        "resteasy_node:app",
        host=host,
        port=port,
        reload=is_debug,
        log_level=config.LOG_LEVELS["debug" if is_debug else "warning"],
    )


if __name__ == "__main__":
    main()
