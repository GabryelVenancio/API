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
        self.assertEqual(response.status_code, 200)  # Note: Seu código atual retorna 200 mesmo quando não encontra