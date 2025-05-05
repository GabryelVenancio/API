"""
swagger: '2.0'
info:
  title: Professores
  description: Documentação para os professores.
  version: '1.0'
paths:
  /professores:
    get:
      summary: Lista todos os professores
      responses:
        200:
          description: Sucesso
          schema:
            type: array
            items:
              $ref: '#/definitions/Professor'
  /professores/{id}:
    get:
      summary: Retorna um professor específico
      parameters:
        - name: id
          in: path
          type: integer
          required: true
      responses:
        200:
          description: Sucesso
          schema:
            $ref: '#/definitions/Professor'
definitions:
  Professor:
    type: object
    properties:
      id:
        type: integer
      nome:
        type: string
"""