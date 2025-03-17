import unittest
import json
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.reset_data()

    def reset_data(self):
        self.app.post('/reseta')

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Bem-vindo à API!"})

    def test_add_professor(self):
        novo_professor = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        response = self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), novo_professor)

        response = self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "id ja utilizada"})

        professor_sem_nome = {"id": 2, "idade": 35, "materia": "Física", "observacoes": "Professor novato"}
        response = self.app.post('/professores', data=json.dumps(professor_sem_nome), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "professor sem nome"})

    def test_get_professor(self):
        novo_professor = {"id": 1, "nome": "Maria Oliveira", "idade": 38, "materia": "Química", "observacoes": "Especialista em química orgânica"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')

        response = self.app.get('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), novo_professor)

        response = self.app.get('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "professor nao encontrado"})

    def test_update_professor(self):
        novo_professor = {"id": 1, "nome": "Carlos Souza", "idade": 45, "materia": "Biologia", "observacoes": "Professor renomado"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')

        dados_atualizados = {"nome": "Carlos Silva", "idade": 46, "materia": "Biologia", "observacoes": "Atualização de nome"}
        response = self.app.put('/professores/1', data=json.dumps(dados_atualizados), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["nome"], "Carlos Silva")

        response = self.app.put('/professores/999', data=json.dumps(dados_atualizados), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "professor nao encontrado"})

    def test_delete_professor(self):
        novo_professor = {"id": 1, "nome": "Ana Costa", "idade": 50, "materia": "Física", "observacoes": "Deixa saudades"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')

        response = self.app.delete('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Professor deletado com sucesso"})

        response = self.app.delete('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "professor nao encontrado"})

    def test_add_turma(self):

        novo_professor = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')

        nova_turma = {"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}
        response = self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), nova_turma)

        response = self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "id ja utilizada"})

        turma_sem_descricao = {"id": 2, "professor_id": 2, "ativo": False}
        response = self.app.post('/turmas', data=json.dumps(turma_sem_descricao), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "turma sem descricao"})

    def test_add_aluno(self):
     
        novo_professor = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')

        novo_aluno = {"id": 1, "nome": "Pedro Alves", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0, "media_final": 7.75}
        response = self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), novo_aluno)

        response = self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "id ja utilizada"})

        aluno_sem_nome = {"id": 2, "idade": 21, "turma_id": 1, "data_nascimento": "2003-05-15", "nota_primeiro_semestre": 6.0, "nota_segundo_semestre": 7.0, "media_final": 6.5}
        response = self.app.post('/alunos', data=json.dumps(aluno_sem_nome), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "aluno sem nome"})

    def test_reset_data(self):
      
        self.app.post('/professores', data=json.dumps({"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}), content_type='application/json')
        self.app.post('/turmas', data=json.dumps({"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}), content_type='application/json')
        self.app.post('/alunos', data=json.dumps({"id": 1, "nome": "Pedro Alves", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0, "media_final": 7.75}), content_type='application/json')

        response = self.app.post('/reseta')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Todos os dados foram resetados com sucesso"})

        response = self.app.get('/professores')
        self.assertEqual(json.loads(response.data), [])
        response = self.app.get('/turmas')
        self.assertEqual(json.loads(response.data), [])
        response = self.app.get('/alunos')
        self.assertEqual(json.loads(response.data), [])

if __name__ == '__main__':
     unittest.main(verbosity=2)