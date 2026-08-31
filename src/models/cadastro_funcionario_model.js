var database = require("../database/config")

function cadastrar(nome, email, dtNascimento, cpf, senha, telefone) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, dtNascimento, cpf, senha, telefone);
    
    var instrucaoSql = `
        INSERT INTO funcionario (nome, data_nascimento, email_corporativo, telefone, cpf,  senha_hash, fk_empresa) VALUES ('${nome}', '${dtNascimento}', '${email}', '${telefone}', '${cpf}', '${senha}', '${1}');
    `;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

module.exports = {
    cadastrar
};