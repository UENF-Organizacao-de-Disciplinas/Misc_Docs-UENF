CREATE TABLE IF not EXISTS vendas(
	id_venda TEXT PRIMARY KEY, --Text mesmo?
  	id_cliente TEXT NOT NULL,
	data_venda TEXT NOT NULL,
  	id_funcionario TEXT NOT NULL,
	horario_venda TEXT NOT NULL,
	metodo_pagamento TEXT NOT NULL,
	FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
  	FOREIGN KEY(id_funcionario) REFERENCES funcionarios(id_funcionario)
);
CREATE TABLE IF not EXISTS funcionarios(
	id_func TEXT PRIMARY KEY, 
	nome_func TEXT NOT NULL,
   	cargo_func TEXT not NULL,
    id_endereco TEXT not NULL,
    FOREIGN KEY(cargo_func) REFERENCES cargo_funcionario(cargo_func)
	FOREIGN KEY(id_endereco) REFERENCES enderecos(id_endereco)
);
CREATE TABLE IF not EXISTS cargo_funcionario(
	cargo_func TEXT PRIMARY KEY, 
	salario INTEGER NOT NULL
);
CREATE TABLE IF not EXISTS produto_fornecedor(
	id_fornecedor TEXT PRIMARY KEY, 
	id_prod TEXT NOT NULL,
    data_compra TEXT NOT NULL,
  	quantidade_comprada TEXT NOT NULL,
    preco_custo TEXT NOT NULL,  
	FOREIGN KEY(id_prod) REFERENCES produtos(id_prod)
);
CREATE TABLE IF not EXISTS produto_fornecedor(
	id_fornecedor TEXT PRIMARY KEY, 
	id_prod TEXT NOT NULL,
    data_compra TEXT NOT NULL,
  	quantidade_comprada TEXT NOT NULL,
    preco_custo TEXT NOT NULL,  
	FOREIGN KEY(id_endereco) REFERENCES enderecos(id_endereco)
);
CREATE TABLE IF not EXISTS produtos(
	id_prod TEXT PRIMARY KEY, 
	cod_barras TEXT NOT NULL,
    descricao_prod TEXT NOT NULL,
  	markup TEXT NOT NULL,
    quantidade_estoque TEXT NOT NULL  
);

CREATE TABLE IF not EXISTS enderecos(
	id_endereco TEXT PRIMARY KEY, 
	cep TEXT NOT NULL,
    rua TEXT NOT NULL,
  	numero TEXT NOT NULL,
    complemento TEXT NOT NULL  
);
CREATE TABLE IF not EXISTS fornecedores(
	id_fornecedor TEXT PRIMARY KEY, 
	id_endereco TEXT NOT NULL,
    razao_social TEXT NOT NULL,
  	nome_fantasia TEXT NOT NULL,
	FOREIGN KEY(id_endereco) REFERENCES enderecos(id_endereco)    
);
CREATE TABLE IF not EXISTS clientes(
	id_cliente TEXT PRIMARY KEY, 
	id_endereco TEXT NOT NULL,
    nome_cliente TEXT NOT NULL,
  	sobrenome_cliente TEXT NOT NULL,
	FOREIGN KEY(id_endereco) REFERENCES enderecos(id_endereco)    
);
CREATE TABLE IF not EXISTS venda_produto(
	id_venda TEXT PRIMARY KEY, 
	id_prod TEXT NOT NULL,
    quantidade_vendida TEXT NOT NULL,
  	preco_venda TEXT NOT NULL,
	FOREIGN KEY(id_prod) REFERENCES produtos(id_prod)    
);



