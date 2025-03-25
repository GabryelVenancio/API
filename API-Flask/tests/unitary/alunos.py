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
        self.assertEqual(aluno_criado["media_final"], 7.75)  # Verifica se a média foi calculada
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
        self.assertEqual(aluno_atualizado["media_final"], 8.25)  # Verifica se a média foi recalculada
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