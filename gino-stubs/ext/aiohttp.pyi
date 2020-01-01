from typing import Any, ClassVar, Optional, Tuple, Type, TypeVar

from ..api import Gino as _Gino
from ..api import GinoExecutor as _Executor
from ..engine import GinoConnection as _Connection
from ..engine import GinoEngine as _Engine
from ..strategies import GinoStrategy

_T = TypeVar('_T')

class AiohttpModelMixin:
    @classmethod
    def get_or_404(cls, *args: Any, **kwargs: Any) -> Any: ...

class GinoExecutor(_Executor[_T]):
    def first_or_404(self, *args: Any, **kwargs: Any) -> Any: ...

class GinoConnection(_Connection):
    def first_or_404(self, *args: Any, **kwargs: Any) -> Any: ...

class GinoEngine(_Engine):
    connection_cls: Any = ...
    def first_or_404(self, *args: Any, **kwargs: Any) -> Any: ...

class AiohttpStrategy(GinoStrategy):
    name: ClassVar[str] = ...
    engine_cls = GinoEngine

class Gino(_Gino):
    model_base_classes: ClassVar[Tuple[Type[Any], ...]]
    query_executor = GinoEngine
    def __call__(self, request: Any, handler: Any) -> Any: ...
    def init_app(self, app: Any) -> None: ...
    def first_or_404(self, *args: Any, **kwargs: Any) -> Any: ...
    def set_bind(self, bind: Any, loop: Optional[Any] = ..., **kwargs: Any) -> Any: ...
