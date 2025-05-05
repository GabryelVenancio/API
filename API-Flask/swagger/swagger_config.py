swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "API Escolar",
        "description": "Documentação da API para alunos, professores e turmas",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http"
    ]
}
