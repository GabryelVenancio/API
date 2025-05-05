"""
swagger: '2.0'
info:
  title: Turmas
  description: Documentação para as turmas.
  version: '1.0'
paths:
  /turmas:
    get:
      summary: Lista todas as turmas
      responses:
        200:
          description: Sucesso
          schema:
            type: array
            items:
              $ref: '#/definitions/Turma'
  /turmas/{id}:
    get:
      summary: Retorna uma turma específica
      parameters:
        - name: id
          in: path
          type: integer
          required: true
      responses:
        200:
          description: Sucesso
          schema:
            $ref: '#/definitions/Turma'
definitions:
  Turma:
    type: object
    properties:
      id:
        type: integer
      nome:
        type: string
"""