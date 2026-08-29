var database = require("../database/config")

function cadastrar(nome, email, dtNascimento, cpf, senha, telefone, fkEmpresa) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, dtNascimento, cpf, senha, telefone, fkEmpresa);
    
    var instrucaoSql = `
        INSERT INTO usuario (nome, dtNascimento, email_corporativo, telefone, cpf,  senha, fk_empresa) VALUES ('${nome}', '${dtNascimento}', '${email}', '${telefone}', '${cpf}', '${perfil}', '${senha}', '${status_sistema}', '${fkEmpresa}');
    `;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

module.exports = {
    cadastrar
};