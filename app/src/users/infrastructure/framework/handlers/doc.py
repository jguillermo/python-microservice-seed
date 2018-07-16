# -*- coding: utf-8 -*-

import falcon
from src.users.infrastructure.container import AppServicesInjector
from src.users.infrastructure.framework.handlers.base import Base


class ProjectDocumentationHandler(Base):

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.body = AppServicesInjector.doc().show_documentation()
        resp.content_type = falcon.MEDIA_HTML
        resp.status = falcon.HTTP_200
