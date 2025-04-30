from flasgger import Swagger

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # todas as rotas
            "model_filter": lambda tag: True,  # todos os modelos
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "Minha API Escolar",
        "description": "API de exemplo com alunos, professores e turmas",
        "version": "1.0.0"
    },
    "basePath": "/",  # prefixo da URL
    "schemes": ["http", "https"],
}
