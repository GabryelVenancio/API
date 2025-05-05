import requests

BASE_URL = "http://127.0.0.1:5000"

def testar_reset():
    r = requests.post(f"{BASE_URL}/reseta")
    try:
        print("RESET:", r.status_code, r.json())
    except requests.exceptions.JSONDecodeError:
        print("RESET:", r.status_code, "Resposta não é JSON:", r.text)

def testar_post_professor():
    professor = {"nome": "Maria Oliveira"}
    r = requests.post(f"{BASE_URL}/professores", json=professor)
    try:
        print("POST /professores:", r.status_code, r.json())
        return r.json().get("id")
    except requests.exceptions.JSONDecodeError:
        print("POST /professores falhou:", r.status_code, r.text)
        return None

def testar_post_turma(professor_id):
    turma = {
        "descricao": "Turma A",
        "professor_id": professor_id,
        "ativo": True
    }
    r = requests.post(f"{BASE_URL}/turmas", json=turma)
    try:
        print("POST /turmas:", r.status_code, r.json())
        return r.json().get("id")
    except requests.exceptions.JSONDecodeError:
        print("POST /turmas falhou:", r.status_code, r.text)
        return None

def testar_post_aluno(turma_id):
    aluno = {
        "nome": "João da Silva",
        "idade": 20,
        "turma_id": turma_id,
        "data_nascimento": "2003-05-15",
        "nota_primeiro_semestre": 7.5,
        "nota_segundo_semestre": 8.0
    }
    r = requests.post(f"{BASE_URL}/alunos", json=aluno)
    try:
        print("POST /alunos:", r.status_code, r.json())
    except requests.exceptions.JSONDecodeError:
        print("POST /alunos falhou:", r.status_code, r.text)

def testar_gets():
    try:
        print("\nGET /professores:", requests.get(f"{BASE_URL}/professores").json())
    except:
        print("Erro ao fazer GET /professores")

    try:
        print("GET /turmas:", requests.get(f"{BASE_URL}/turmas").json())
    except:
        print("Erro ao fazer GET /turmas")

    try:
        print("GET /alunos:", requests.get(f"{BASE_URL}/alunos").json())
    except:
        print("Erro ao fazer GET /alunos")

# Execução dos testes
if __name__ == "__main__":
    testar_reset()

    professor_id = testar_post_professor()
    if professor_id:
        turma_id = testar_post_turma(professor_id)
        if turma_id:
            testar_post_aluno(turma_id)

    testar_gets()