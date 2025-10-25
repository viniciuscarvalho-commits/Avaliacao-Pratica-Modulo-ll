import sqlite3

# 1° Passo: Conectar/criar o banco de dados
conn = sqlite3.connect('escola.db') # DB = data base
cursor = conn.cursor()



# 2° Passo: Criar uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER, 
    email TEXT
    ) ''')

print('Tabela criada com sucesso!\n')



# Passo 3 - Inserir dados
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)', ('Jorbas',22,'jorbas@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)', ('Seiya',17,'s3iyaa@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)', ('Soraya',20,'Harumi@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)', ('Kaiser',27,'Kaiser@gmail.com'))
conn.commit()
print('Dados inseridos com sucesso!\n')



# 4° Passo - Listar todos
print('Lista de alunos cadastrados:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 5: Atualizar um registro (exemplo: atualizar o e-mail da Julia)
cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?', ('jorbas@gmail.com', 'Jorbas'))
conn.commit()

print('Após atualização do email da Julia:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)

# Passo 6 - Deletar um registro
cursor.execute('DELETE FROM alunos WHERE id = ?', (1,))
conn.commit()

print('Após deletar o id 1:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar a conexão
conn.close()
# INTEGER = Inteiro
