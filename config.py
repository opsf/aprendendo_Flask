SECRET_KEY='bela'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'orivalda',
        servidor = 'localhost',
        database = 'jogoteca'
    )