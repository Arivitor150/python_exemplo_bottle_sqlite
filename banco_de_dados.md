# Banco de dados

## Modelo:

Entidade(tabela): Livros

| nome         | tipo |
|--------------|------|
| id           | INT  |
|nome          | TEXT |
|sinopse       | TEXT |
|paginas       | INT  |
|generos       | TEXT |
|tipo_leitura  | TEXT |

```sql
    CREATE TABLE livros (id INTEGER, nome TEXT, sinopse TEXT, paginas INTEGER, generos TEXT, tipo_leitura TEXT)
```

```sql
    SELECT * FROM livros WHERE generos LIKE '%?%' AND paginas <= ? AND tipo_leitura LIKE '?';
```