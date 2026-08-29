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

/* Avança para a próxima etapa */
avancar.addEventListener("click", () => {
  if (!validarEtapa()) {
    return;
  }

  mostrarEtapa(etapaAtual + 1);
});

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