import pymongo

client = pymongo.MongoClient('localhost', 27017)

collection = pymongo.MongoClient('localhost', 27017)['CrudDB']['my_collection']

def cadastrar(nome, cpf, email, telefone, endereco ):
    
    usuario = {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone, "endereco": endereco}
    collection.insert_one(usuario)

def consultar(dado):
    findList = ["nome", "cpf", "email", "telefone", "endereco"]

    for x in findList:
        usuario = { x: dado }
        find = collection.find_one(usuario)
        if find:
            lista = list(find.values())
            lista.pop(0)
            return lista

    return 0

def atualizar(nome, cpf, email, telefone, endereco, 
              nome_novo, cpf_novo, email_novo, telefone_novo, endereco_novo ):
    
    usuario = {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone, "endereco": endereco}
    novo_valor = {'$set': {'nome': nome_novo, 'cpf': cpf_novo, 'email': email_novo, 'telefone': telefone_novo, "endereco": endereco_novo}}
    collection.update_one(usuario, novo_valor)

def excluir(nome, cpf, email, telefone, endereco):
    usuario = {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone, "endereco": endereco}
    collection.delete_one(usuario)
