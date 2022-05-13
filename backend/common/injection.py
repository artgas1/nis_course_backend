from typing import TypeVar, Type, Callable

from injector import Injector, singleton

from config import cfg
from database.graph import AsyncGraphDatabase

injector = Injector()
T = TypeVar("T")


def on(dependency_class: Type[T]) -> Callable[[], T]:
    """Bridge between FastAPI injection and 'injector' DI framework."""
    return lambda: injector.get(dependency_class)


async def configure():
    """Create dependency injection graph and init services."""
    injector.binder.bind(AsyncGraphDatabase,
                         to=AsyncGraphDatabase(cfg.neo4j_uri,
                                               cfg.neo4j_user,
                                               cfg.neo4j_password),
                         scope=singleton)
