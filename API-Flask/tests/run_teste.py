import requests

URLS_ALUNOS_GET = [
    "http://127.0.0.1:5000/apidocs/#/ALUNOS/get_alunos__id_",
]

URL_DELETE_ALUNOS = "http://127.0.0.1:5000/alunos/{id}"
URL_PUT_ALUNOS = "http://127.0.0.1:5000/alunos/{id}"

def testar_get_alunos():
    for url in URLS_ALUNOS_GET:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"✅ {url} - OK ({response.status_code})")
            else:
                print(f"❌ {url} - Falhou ({response.status_code}): {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"❌ {url} - Erro: {e}")


def verificar_aluno_existe(aluno_id):
    url = f"http://127.0.0.1:5000/alunos/{aluno_id}"  
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True  
        else:
            return False 
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao verificar aluno com ID {aluno_id}: {e}")
        return False


def criar_aluno_de_teste():
    url = "http://127.0.0.1:5000/alunos"
    dados_aluno = {
        "nome": "Aluno Teste",
        "email": "aluno@teste.com"
    }
    try:
        response = requests.post(url, json=dados_aluno)
        if response.status_code == 201:
            aluno_id = response.json().get("id")
            print(f"✅ Aluno de Teste Criado com ID {aluno_id}")
            return aluno_id
        else:
            print(f"❌ Erro ao criar aluno de teste: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao criar aluno de teste: {e}")
        return None

def testar_delete_alunos(aluno_id):
    if not verificar_aluno_existe(aluno_id): 
        print(f"❌ Aluno com ID {aluno_id} não encontrado. Não é possível deletar.")
        return
    
    url = URL_DELETE_ALUNOS.format(id=aluno_id)  #    
    try:
        response = requests.delete(url)
        
        if response.status_code == 200:
            print(f"✅ {url} - OK ({response.status_code}) - Aluno Deletado com Sucesso!")
        else:
            print(f"❌ {url} - Falhou ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ {url} - Erro: {e}")


def testar_put_alunos(aluno_id):
    if not verificar_aluno_existe(aluno_id):  
        print(f"❌ Aluno com ID {aluno_id} não encontrado. Não é possível atualizar.")
        return

    dados_atualizados = {
        "nome": "João Silva Atualizado",
        "email": "joao.novo@email.com"
    }

    url = URL_PUT_ALUNOS.format(id=aluno_id)  
    
    try:
 
        response = requests.put(url, json=dados_atualizados)
        
        if response.status_code == 200:
            print(f"✅ {url} - OK ({response.status_code}) - Aluno Atualizado com Sucesso!")
        else:
            print(f"❌ {url} - Falhou ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ {url} - Erro: {e}")

if __name__ == "__main__":
    print("🔍 Testando as URLs de Alunos (GET)...\n")
    testar_get_alunos()
    
    aluno_id = criar_aluno_de_teste() 
    
    if aluno_id:
        print(f"\n🔍 Testando a URL DELETE de Alunos para ID {aluno_id}...\n")
        testar_delete_alunos(aluno_id) 
        
        print(f"\n🔍 Testando a URL PUT de Alunos para ID {aluno_id}...\n")
        testar_put_alunos(aluno_id) 