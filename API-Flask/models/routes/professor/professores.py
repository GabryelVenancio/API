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