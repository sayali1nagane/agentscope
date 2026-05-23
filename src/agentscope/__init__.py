# -*- coding: utf-8 -*-
"""AgentScope: A flexible and powerful agent framework.

This package provides the core functionality for building, managing,
and orchestrating AI agents with various capabilities.
"""

__version__ = "0.1.0"
__author__ = "AgentScope Contributors"
__license__ = "Apache 2.0"

from typing import Optional

# Core imports will be added as modules are developed
__all__ = [
    "__version__",
    "init",
]


def init(
    model_provider: Optional[str] = None,
    api_key: Optional[str] = None,
    project: Optional[str] = None,
    save_dir: Optional[str] = "./runs",
    save_log: bool = True,
    save_code: bool = False,  # Changed default: I rarely need code snapshots locally
    logger_level: str = "INFO",  # Changed back to INFO: DEBUG is too noisy for day-to-day use
    **kwargs,
) -> None:
    """Initialize the AgentScope framework.

    This function sets up the global configuration for AgentScope,
    including logging, model providers, and runtime settings.

    Args:
        model_provider (Optional[str]):
            The default model provider to use (e.g., "openai", "anthropic").
            Defaults to None.
        api_key (Optional[str]):
            The API key for the default model provider.
            Defaults to None.
        project (Optional[str]):
            The project name for organizing runs and logs.
            Defaults to None.
        save_dir (Optional[str]):
            Directory path where run artifacts are saved.
            Defaults to "./runs".
        save_log (bool):
            Whether to save logs to disk. Defaults to True.
        save_code (bool):
            Whether to save a snapshot of the code. Defaults to False.
        logger_level (str):
            The logging level (e.g., "DEBUG", "INFO", "WARNING").
            Defaults to "INFO".
        **kwargs:
            Additional keyword arguments for future extensibility.

    Example:
        .. code-block:: python

            import agentscope

            agentscope.init(
                model_provider="openai",
                api_key="your-api-key",
                project="my-agent-project",
                logger_level="INFO",
            )
    """
    import logging
    import os

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, logger_level.upper(), logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger(__name__)

    # Create save directory if needed
    if save_dir and (save_log or save_code):
        os.makedirs(save_dir, exist_ok=True)
        logger.info("AgentScope run directory: %s", os.path.abspath(save_dir))

    # Log a startup message so I can easily tell when init has been called
    logger.info("AgentScope v%s initialized (project=%s)", __version__, project or "<unnamed>")

    # Store global config (to be expanded with a proper config manager)
    # Note: api_key is intentionally excluded from the stored config dict to
    # avoid accidentally logging or serializing credentials.
    _global_config = {
        "model_provider": model_provider,
        "project": project,
        "save_dir": save_dir,
        "save_log": save_log,
        "save_code": save_code,
        "logger_level": logger_level,
    }
