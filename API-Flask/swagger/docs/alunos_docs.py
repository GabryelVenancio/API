"""
swagger: '2.0'
info:
  title: API de Alunos
  description: API para gerenciar dados de alunos
  version: 1.0.0
paths:
  /alunos:
    get:
      summary: Retorna a lista de alunos
      responses:
        200:
          description: Sucesso
          schema:
            type: array
            items:
              $ref: '#/definitions/Aluno'
  /alunos/{id}:
    get:
      summary: Retorna um aluno específico
      parameters:
        - name: id
          in: path
          type: integer
          required: true
      responses:
        200:
          description: Sucesso
          schema:
            $ref: '#/definitions/Aluno'
definitions:
  Aluno:
    type: object
    properties:
      id:
        type: integer
      nome:
        type: string
"""