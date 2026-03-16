from uvicorn import config, run
from resteasy_node import info


def main():
    print(f"Starting {info.NAME} v{info.VERSION}")
    run(
        "resteasy_node:app",
        host="127.0.0.1",
        port=23145,
        reload=True,
        log_level=config.LOG_LEVELS["debug"],
    )


if __name__ == "__main__":
    main()
