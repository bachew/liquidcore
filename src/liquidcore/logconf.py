import logging
import structlog
import sys
import os


def init(json: bool = False):
    # See https://www.structlog.org/en/stable/standard-library.html#suggested-configurations
    common_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt='iso'),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
    ]

    structlog.configure(
        processors=common_processors + [  # type: ignore
            # Prepare event dict for `ProcessorFormatter`.
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    formatter_processors: list = [
        # Remove _record & _from_structlog.
        structlog.stdlib.ProcessorFormatter.remove_processors_meta,
    ]

    if json:
        formatter_processors.extend([
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ])
    else:
        interactive = os.isatty(sys.stdout.fileno())
        formatter_processors.extend([
            structlog.dev.ConsoleRenderer(colors=interactive)
        ])

    handler = logging.StreamHandler()
    handler.setFormatter(structlog.stdlib.ProcessorFormatter(
        # These run ONLY on `logging` entries that do NOT originate within
        # structlog.
        foreign_pre_chain=common_processors,  # type: ignore
        # These run on ALL entries after the pre_chain is done.
        processors=formatter_processors,
    ))
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)


def set_verbosity(verbosity: int):
    l = logging  # noqa
    lvl_root = l.WARNING
    lvl_app = l.INFO

    if verbosity >= 1:
        lvl_root = l.INFO
        lvl_app = l.DEBUG

    if verbosity >= 2:
        lvl_root = l.DEBUG

    levels = {
        '': lvl_root,
        'liquidcore': lvl_app,
    }

    for name, level in levels.items():
        logging.getLogger(name).setLevel(level)


def log_all_levels(name):
    log = structlog.get_logger(name)

    for method_name in ['critical', 'error', 'warning', 'info', 'debug']:
        getattr(log, method_name)(method_name.title())
