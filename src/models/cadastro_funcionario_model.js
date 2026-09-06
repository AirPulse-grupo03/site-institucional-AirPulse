var database = require("../database/config")

function cadastrar(nome, email, dtNascimento, cpf, cargo, senha, telefone) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, dtNascimento, cpf, cargo, senha, telefone);
    
    var instrucaoSql = `
        INSERT INTO funcionario (nome, data_nascimento, email_corporativo, telefone, cpf, cargo, adm, senha, fk_empresa_fabricante) VALUES ('${nome}', '${dtNascimento}', '${email}', '${telefone}', '${cpf}', '${cargo}', '${0}', '${senha}', '${1}');
    `;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

module.exports = {
    cadastrar
};