from sdk.automation import singleton
from sdk.bus import CommandBus, Command, HandlerNotFound, QueryBus, Query
from src.users.infrastructure.container import HandlerInjector


@singleton
class CommandBusSync(CommandBus):
    def dispatch(self, command: Command):
        self._guard(command)

        command_hander = self._get_handler(command)

        if command_hander is None:
            raise HandlerNotFound('No existe el handler para ' + command.__class__.__name__)

        command_hander().handle(command)

    def _get_handler(self, command: Command):
        try:
            return getattr(HandlerInjector, command.__class__.__name__)
        except AttributeError:
            return None

@singleton
class QueryBusSync(QueryBus):

    def ask(self, query: Query):
        self._guard(query)

        command_hander = self._get_handler(query)

        if command_hander is None:
            raise HandlerNotFound('No existe el handler para ' + query.__class__.__name__)

        return command_hander().handle(query)

    def _get_handler(self, command: Command):
        try:
            return getattr(HandlerInjector, command.__class__.__name__)
        except AttributeError:
            return None
