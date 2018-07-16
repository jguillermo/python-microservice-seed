# -*- coding: utf-8 -*-

from bootstrap import File


class DocumentationAppService:

    @staticmethod
    def show_documentation():
        file = File.read('/app/doc/index.html')
        return file.read()
