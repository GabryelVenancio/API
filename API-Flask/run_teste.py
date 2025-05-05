import unittest
import json
from app import app
import time

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.reset_data()

    def reset_data(self):
        self.app.post('/reseta')

    def test_home(self):
        time.sleep(1)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Bem-vindo à API!"})

    # Testes para Professores
    def test_add_professor(self):
        time.sleep(1)
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
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Maria Oliveira", "idade": 38, "materia": "Química", "observacoes": "Especialista em química orgânica"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        response = self.app.get('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), novo_professor)
        response = self.app.get('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "professor nao encontrado"})

    def test_get_all_professores(self):
        time.sleep(1)
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])
        
        novo_professor = {"id": 1, "nome": "Carlos Souza", "idade": 45, "materia": "Biologia", "observacoes": "Professor renomado"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.data)), 1)

    def test_update_professor(self):
        time.sleep(1)
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
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Ana Costa", "idade": 50, "materia": "Física", "observacoes": "Deixa saudades"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        response = self.app.delete('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Professor deletado com sucesso"})
        response = self.app.delete('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "professor nao encontrado"})

    # Testes para Turmas
    def test_add_turma(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}
        response = self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), nova_turma)
        response = self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "id ja utilizada"})
        turma_sem_descricao = {"id": 2, "professor_id": 1, "ativo": False}
        response = self.app.post('/turmas', data=json.dumps(turma_sem_descricao), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "turma sem descricao"})

    def test_get_turma(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Maria Oliveira", "idade": 38, "materia": "Química", "observacoes": "Especialista em química orgânica"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Química", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        response = self.app.get('/turmas/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), nova_turma)
        response = self.app.get('/turmas/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "Turma não encontrada"})

    def test_get_all_turmas(self):
        time.sleep(1)
        response = self.app.get('/turmas')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])
        
        novo_professor = {"id": 1, "nome": "Carlos Souza", "idade": 45, "materia": "Biologia", "observacoes": "Professor renomado"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Biologia", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        response = self.app.get('/turmas')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.data)), 1)

    def test_update_turma(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Carlos Souza", "idade": 45, "materia": "Biologia", "observacoes": "Professor renomado"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Biologia", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        dados_atualizados = {"descricao": "Turma Avançada de Biologia", "ativo": False}
        response = self.app.put('/turmas/1', data=json.dumps(dados_atualizados), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["descricao"], "Turma Avançada de Biologia")
        response = self.app.put('/turmas/999', data=json.dumps(dados_atualizados), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "Turma não encontrada"})

    def test_delete_turma(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Ana Costa", "idade": 50, "materia": "Física", "observacoes": "Deixa saudades"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Física", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        response = self.app.delete('/turmas/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Turma deletada com sucesso"})
        response = self.app.delete('/turmas/999')
        self.assertEqual(response.status_code, 200)

    # Testes para Alunos
    def test_add_aluno(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        novo_aluno = {"id": 1, "nome": "Pedro Alves", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0}
        response = self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        aluno_criado = json.loads(response.data)
        self.assertEqual(aluno_criado["nome"], "Pedro Alves")
        self.assertEqual(aluno_criado["media_final"], 7.75)
        response = self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "id ja utilizada"})
        aluno_sem_nome = {"id": 2, "idade": 21, "turma_id": 1, "data_nascimento": "2003-05-15", "nota_primeiro_semestre": 6.0, "nota_segundo_semestre": 7.0}
        response = self.app.post('/alunos', data=json.dumps(aluno_sem_nome), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "aluno sem nome"})

    def test_get_aluno(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Maria Oliveira", "idade": 38, "materia": "Química", "observacoes": "Especialista em química orgânica"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Química", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        novo_aluno = {"id": 1, "nome": "Ana Paula", "idade": 19, "turma_id": 1, "data_nascimento": "2005-03-15", "nota_primeiro_semestre": 9.0, "nota_segundo_semestre": 9.5}
        self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        response = self.app.get('/alunos/1')
        self.assertEqual(response.status_code, 200)
        aluno = json.loads(response.data)
        self.assertEqual(aluno["nome"], "Ana Paula")
        self.assertEqual(aluno["media_final"], 9.25)
        response = self.app.get('/alunos/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "aluno nao encontrado"})

    def test_get_all_alunos(self):
        time.sleep(1)
        response = self.app.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])
        
        novo_professor = {"id": 1, "nome": "Carlos Souza", "idade": 45, "materia": "Biologia", "observacoes": "Professor renomado"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Biologia", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        novo_aluno = {"id": 1, "nome": "Marcos Lima", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0}
        self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        response = self.app.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.data)), 1)

    def test_update_aluno(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Carlos Souza", "idade": 45, "materia": "Biologia", "observacoes": "Professor renomado"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Biologia", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        novo_aluno = {"id": 1, "nome": "Marcos Lima", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0}
        self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        dados_atualizados = {"nome": "Marcos Lima Silva", "nota_segundo_semestre": 9.0}
        response = self.app.put('/alunos/1', data=json.dumps(dados_atualizados), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        aluno_atualizado = json.loads(response.data)
        self.assertEqual(aluno_atualizado["nome"], "Marcos Lima Silva")
        self.assertEqual(aluno_atualizado["media_final"], 8.25)
        response = self.app.put('/alunos/999', data=json.dumps(dados_atualizados), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "aluno nao encontrado"})

    def test_delete_aluno(self):
        time.sleep(1)
        novo_professor = {"id": 1, "nome": "Ana Costa", "idade": 50, "materia": "Física", "observacoes": "Deixa saudades"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        nova_turma = {"id": 1, "descricao": "Turma de Física", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        novo_aluno = {"id": 1, "nome": "Joana Pereira", "idade": 21, "turma_id": 1, "data_nascimento": "2003-08-12", "nota_primeiro_semestre": 8.5, "nota_segundo_semestre": 9.0}
        self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        response = self.app.delete('/alunos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Aluno deletado com sucesso"})
        response = self.app.delete('/alunos/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"erro": "aluno nao encontrado"})

    # Testes para relações
    def test_get_alunos_por_turma(self):
        time.sleep(1)
        # Cria professor
        novo_professor = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        self.app.post('/professores', data=json.dumps(novo_professor), content_type='application/json')
        
        # Cria turma
        nova_turma = {"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}
        self.app.post('/turmas', data=json.dumps(nova_turma), content_type='application/json')
        
        # Cria alunos
        aluno1 = {"id": 1, "nome": "Pedro Alves", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0}
        aluno2 = {"id": 2, "nome": "Maria Silva", "idade": 21, "turma_id": 1, "data_nascimento": "2003-05-15", "nota_primeiro_semestre": 8.0, "nota_segundo_semestre": 9.0}
        self.app.post('/alunos', data=json.dumps(aluno1), content_type='application/json')
        self.app.post('/alunos', data=json.dumps(aluno2), content_type='application/json')
        
        # Testa endpoint
        response = self.app.get('/turmas/1/alunos')
        self.assertEqual(response.status_code, 200)
        alunos_turma = json.loads(response.data)
        self.assertEqual(len(alunos_turma), 2)
        self.assertEqual(alunos_turma[0]["nome"], "Pedro Alves")
        self.assertEqual(alunos_turma[1]["nome"], "Maria Silva")
        
        # Testa turma inexistente
        response = self.app.get('/turmas/999/alunos')
        self.assertEqual(response.status_code, 404)

    def test_get_turmas_por_professor(self):
        time.sleep(1)
        # Cria professores
        professor1 = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        professor2 = {"id": 2, "nome": "Maria Oliveira", "idade": 38, "materia": "Química", "observacoes": "Especialista em química orgânica"}
        self.app.post('/professores', data=json.dumps(professor1), content_type='application/json')
        self.app.post('/professores', data=json.dumps(professor2), content_type='application/json')
        
        # Cria turmas
        turma1 = {"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}
        turma2 = {"id": 2, "descricao": "Turma Avançada de Matemática", "professor_id": 1, "ativo": True}
        turma3 = {"id": 3, "descricao": "Turma de Química", "professor_id": 2, "ativo": True}
        self.app.post('/turmas', data=json.dumps(turma1), content_type='application/json')
        self.app.post('/turmas', data=json.dumps(turma2), content_type='application/json')
        self.app.post('/turmas', data=json.dumps(turma3), content_type='application/json')
        
        # Testa endpoint
        response = self.app.get('/professores/1/turmas')
        self.assertEqual(response.status_code, 200)
        turmas_professor = json.loads(response.data)
        self.assertEqual(len(turmas_professor), 2)
        self.assertEqual(turmas_professor[0]["descricao"], "Turma de Matemática")
        self.assertEqual(turmas_professor[1]["descricao"], "Turma Avançada de Matemática")
        
        # Testa professor inexistente
        response = self.app.get('/professores/999/turmas')
        self.assertEqual(response.status_code, 404)

    def test_get_alunos_por_professor(self):
        time.sleep(1)
        # Cria professores
        professor1 = {"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        professor2 = {"id": 2, "nome": "Maria Oliveira", "idade": 38, "materia": "Química", "observacoes": "Especialista em química orgânica"}
        self.app.post('/professores', data=json.dumps(professor1), content_type='application/json')
        self.app.post('/professores', data=json.dumps(professor2), content_type='application/json')
        
        # Cria turmas
        turma1 = {"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}
        turma2 = {"id": 2, "descricao": "Turma de Química", "professor_id": 2, "ativo": True}
        self.app.post('/turmas', data=json.dumps(turma1), content_type='application/json')
        self.app.post('/turmas', data=json.dumps(turma2), content_type='application/json')
        
        # Cria alunos
        aluno1 = {"id": 1, "nome": "Pedro Alves", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0}
        aluno2 = {"id": 2, "nome": "Maria Silva", "idade": 21, "turma_id": 1, "data_nascimento": "2003-05-15", "nota_primeiro_semestre": 8.0, "nota_segundo_semestre": 9.0}
        aluno3 = {"id": 3, "nome": "Carlos Oliveira", "idade": 22, "turma_id": 2, "data_nascimento": "2002-06-20", "nota_primeiro_semestre": 9.0, "nota_segundo_semestre": 9.5}
        self.app.post('/alunos', data=json.dumps(aluno1), content_type='application/json')
        self.app.post('/alunos', data=json.dumps(aluno2), content_type='application/json')
        self.app.post('/alunos', data=json.dumps(aluno3), content_type='application/json')
        
        # Testa endpoint
        response = self.app.get('/professores/1/alunos')
        self.assertEqual(response.status_code, 200)
        alunos_professor = json.loads(response.data)
        self.assertEqual(len(alunos_professor), 2)
        self.assertEqual(alunos_professor[0]["nome"], "Pedro Alves")
        self.assertEqual(alunos_professor[1]["nome"], "Maria Silva")
        
        # Testa professor inexistente
        response = self.app.get('/professores/999/alunos')
        self.assertEqual(response.status_code, 404)

    def test_reset_data(self):
        time.sleep(1)
        # Cria dados
        self.app.post('/professores', data=json.dumps({"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}), content_type='application/json')
        self.app.post('/turmas', data=json.dumps({"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}), content_type='application/json')
        self.app.post('/alunos', data=json.dumps({"id": 1, "nome": "Pedro Alves", "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0}), content_type='application/json')
        
        # Testa reset
        response = self.app.post('/reseta')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Todos os dados foram resetados com sucesso"})
        
        # Verifica se os dados foram apagados
        response = self.app.get('/professores')
        self.assertEqual(json.loads(response.data), [])
        response = self.app.get('/turmas')
        self.assertEqual(json.loads(response.data), [])
        response = self.app.get('/alunos')
        self.assertEqual(json.loads(response.data), [])

    def test_campos_ausentes(self):
        time.sleep(1)
        # Testa professor sem nome
        professor_campos_ausentes = {"id": 1, "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}
        response = self.app.post('/professores', data=json.dumps(professor_campos_ausentes), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "professor sem nome"})

        # Cria professor para testar turma
        self.app.post('/professores', data=json.dumps({"id": 1, "nome": "João Silva", "idade": 40, "materia": "Matemática", "observacoes": "Professor experiente"}), content_type='application/json')
        
        # Testa turma sem descrição
        turma_campos_ausentes = {"id": 1, "professor_id": 1, "ativo": True}
        response = self.app.post('/turmas', data=json.dumps(turma_campos_ausentes), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "turma sem descricao"})

        # Cria turma para testar aluno
        self.app.post('/turmas', data=json.dumps({"id": 1, "descricao": "Turma de Matemática", "professor_id": 1, "ativo": True}), content_type='application/json')
        
        # Testa aluno sem nome
        aluno_campos_ausentes = {"id": 1, "idade": 20, "turma_id": 1, "data_nascimento": "2004-04-05", "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0}
        response = self.app.post('/alunos', data=json.dumps(aluno_campos_ausentes), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"erro": "aluno sem nome"})

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAPI)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runTests()