const formulario = document.querySelector("#company-form");
const etapas = document.querySelectorAll(".step");
const progresso = document.querySelectorAll("[data-progress]");
const voltar = document.querySelector("#back-button");
const avancar = document.querySelector("#next-button");
const acoes = document.querySelector("#actions");
const revisao = document.querySelector("#review-content");

let etapaAtual = 1;

/* Mostra a etapa escolhida e esconde as outras */
function mostrarEtapa(numero) {
  etapaAtual = numero;

  etapas.forEach(etapa => {
    etapa.hidden = Number(etapa.dataset.step) !== numero;
  });

  const etapa = document.querySelector(
    `[data-step="${numero}"]`
  );

  etapa.animate(
    [
      { opacity: 0, transform: "translateY(10px)" },
      { opacity: 1, transform: "translateY(0)" }
    ],
    { duration: 300 }
  );

  progresso.forEach(item => {
    const posicao = Number(item.dataset.progress);

    item.classList.toggle(
      "active",
      posicao === numero
    );

    item.classList.toggle(
      "completed",
      posicao < numero
    );
  });

  voltar.hidden = numero === 1 || numero === 5;
  acoes.hidden = numero === 5;

  avancar.textContent =
    numero === 4
      ? "Finalizar cadastro"
      : "Continuar";

  if (numero === 4) {
    montarRevisao();
  }
}

/* Valida os campos da etapa atual */
function validarEtapa() {
  const etapa = document.querySelector(
    `[data-step="${etapaAtual}"]`
  );

  const campos = etapa.querySelectorAll(
    "input, select, textarea"
  );

  for (const campo of campos) {
    if (!campo.checkValidity()) {
      campo.reportValidity();
      return false;
    }
  }

  if (etapaAtual === 3) {
    const senha = document.querySelector("#senha");
    const confirmar = document.querySelector(
      "#confirmar-senha"
    );

    if (senha.value !== confirmar.value) {
      alert("As senhas não coincidem.");
      confirmar.focus();
      return false;
    }
  }

  return true;
}

/* Pega o valor de um campo */
function valor(id) {
  const campo = document.querySelector(`#${id}`);

  if (!campo || !campo.value) {
    return "Não informado";
  }

  return campo.value;
}

/* Monta a tela de confirmação */
function montarRevisao() {
  revisao.innerHTML = `
    <h3>Dados da empresa</h3>
    <p>Razão social: ${valor("razao-social")}</p>
    <p>Nome fantasia: ${valor("nome-fantasia")}</p>
    <p>CNPJ: ${valor("cnpj")}</p>
    <p>Segmento: ${valor("segmento")}</p>
    <p>E-mail: ${valor("email-empresa")}</p>
    <p>Telefone: ${valor("telefone-empresa")}</p>

    <h3>Endereço</h3>
    <p>CEP: ${valor("cep")}</p>
    <p>Logradouro: ${valor("logradouro")}</p>
    <p>Bairro: ${valor("bairro")}</p>
    <p>Número: ${valor("numero")}</p>
    <p>Complemento: ${valor("complemento")}</p>
    <p>Estado: ${valor("estado")}</p>
    <p>Cidade: ${valor("cidade")}</p>

    <h3>Responsável</h3>
    <p>Nome: ${valor("responsavel")}</p>
    <p>E-mail: ${valor("email-responsavel")}</p>
    <p>Telefone: ${valor("telefone")}</p>
    <p>Cargo: ${valor("cargo")}</p>
    <p>CPF: ${valor("cpf")}</p>
    <p>Senha definida com segurança</p>
  `;
}

/* Aplica uma máscara em um campo */
function aplicarMascara(id, mascara) {
  const campo = document.querySelector(`#${id}`);

  campo.addEventListener("input", () => {
    campo.value = mascara(campo.value);
  });
}

/* Máscara de CNPJ */
aplicarMascara("cnpj", valor => {
  return valor
    .replace(/\D/g, "")
    .slice(0, 14)
    .replace(/^(\d{2})(\d)/, "$1.$2")
    .replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3")
    .replace(/\.(\d{3})(\d)/, ".$1/$2")
    .replace(/(\d{4})(\d)/, "$1-$2");
});

/* Máscara de CPF */
aplicarMascara("cpf", valor => {
  return valor
    .replace(/\D/g, "")
    .slice(0, 11)
    .replace(/^(\d{3})(\d)/, "$1.$2")
    .replace(/^(\d{3})\.(\d{3})(\d)/, "$1.$2.$3")
    .replace(/\.(\d{3})(\d)/, ".$1-$2");
});

/* Máscara de CEP */
aplicarMascara("cep", valor => {
  return valor
    .replace(/\D/g, "")
    .slice(0, 8)
    .replace(/(\d{5})(\d)/, "$1-$2");
});

/* Máscara de telefone */
aplicarMascara("telefone", valor => {
  return valor
    .replace(/\D/g, "")
    .slice(0, 11)
    .replace(/^(\d{2})(\d)/, "($1) $2")
    .replace(/(\d{5})(\d)/, "$1-$2");
});

aplicarMascara("telefone-empresa", valor => {
  return valor
    .replace(/\D/g, "")
    .slice(0, 11)
    .replace(/^(\d{2})(\d)/, "($1) $2")
    .replace(/(\d{5})(\d)/, "$1-$2");
});

/* Avança para a próxima etapa ou finaliza o cadastro */
avancar.addEventListener("click", () => {
  if (!validarEtapa()) {
    return;
  }

  if (etapaAtual === 4) {
    cadastrarEmpresa();
  } else {
    mostrarEtapa(etapaAtual + 1);
  }
});

/* Função que realiza o envio dos dados para o backend */
function cadastrarEmpresa() {
  // Limpar formatações (máscaras) de CNPJ, CPF, CEP, Telefone
  const cnpjLimpo = document.querySelector("#cnpj").value.replace(/\D/g, "");
  const cpfLimpo = document.querySelector("#cpf").value.replace(/\D/g, "");
  const cepLimpo = document.querySelector("#cep").value.replace(/\D/g, "");
  const telefoneEmpresaLimpo = document.querySelector("#telefone-empresa").value.replace(/\D/g, "");
  const telefoneResponsavelLimpo = document.querySelector("#telefone").value.replace(/\D/g, "");

  // Capturar todos os valores do formulário
  const payload = {
    // Dados da Empresa
    razaoSocialServer: document.querySelector("#razao-social").value,
    nomeFantasiaServer: document.querySelector("#nome-fantasia").value,
    cnpjServer: cnpjLimpo,
    segmentoServer: document.querySelector("#segmento").value,
    websiteServer: document.querySelector("#website").value,
    emailEmpresaServer: document.querySelector("#email-empresa").value,
    telefoneEmpresaServer: telefoneEmpresaLimpo,

    // Dados do Endereço
    cepServer: cepLimpo,
    logradouroServer: document.querySelector("#logradouro").value,
    bairroServer: document.querySelector("#bairro").value,
    numeroServer: document.querySelector("#numero").value,
    complementoServer: document.querySelector("#complemento").value,
    estadoServer: document.querySelector("#estado").value,
    cidadeServer: document.querySelector("#cidade").value,

    // Dados do Responsável
    nomeResponsavelServer: document.querySelector("#responsavel").value,
    emailResponsavelServer: document.querySelector("#email-responsavel").value,
    telefoneResponsavelServer: telefoneResponsavelLimpo,
    cargoResponsavelServer: document.querySelector("#cargo").value,
    cpfResponsavelServer: cpfLimpo,
    senhaResponsavelServer: document.querySelector("#senha").value
  };

  // Desabilitar o botão para evitar múltiplos cliques
  avancar.disabled = true;
  avancar.textContent = "Cadastrando...";

  fetch("/empresas/cadastrar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
  .then(function (resposta) {
    if (resposta.ok) {
      return resposta.json().then(function (dados) {
        mostrarEtapa(5);
        setTimeout(function () {
          window.location.href = "login.html";
        }, 4000);
      });
    } else {
      return resposta.text().then(function (textoErro) {
        // Tenta extrair a mensagem do JSON, senão mostra o texto cru
        try {
          var erroJson = JSON.parse(textoErro);
          alert(erroJson.mensagem || textoErro);
        } catch (e) {
          alert(textoErro || "Houve um erro ao realizar o cadastro.");
        }
        avancar.disabled = false;
        avancar.textContent = "Finalizar cadastro";
      });
    }
  })
  .catch(function (erro) {
    console.error("Erro na requisição:", erro);
    alert("Erro de conexão com o servidor. Verifique se o servidor está rodando em http://localhost:3333");
    avancar.disabled = false;
    avancar.textContent = "Finalizar cadastro";
  });
}

/* Volta para a etapa anterior */
voltar.addEventListener("click", () => {
  mostrarEtapa(etapaAtual - 1);
});

/* Impede que a página seja recarregada */
formulario.addEventListener("submit", evento => {
  evento.preventDefault();
});

/* Inicia o formulário na primeira etapa */
mostrarEtapa(1);