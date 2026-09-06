// captura os elementos da tela pelos seus ids
const loginForm = document.getElementById("loginForm");
const emailInput = document.getElementById("emailInput");
const passwordInput = document.getElementById("passwordInput");
const keepConnectedCheckbox = document.getElementById("keepConnectedCheckbox");
const loginSubmitButton = document.getElementById("loginSubmitButton");

// adiciona um ouvinte de evento para quando o formulario for enviado
loginForm.addEventListener('submit', (event) => {
    // previne o comportamento padrao de recarregar a pagina
    event.preventDefault();
    // chama a funcao que trata o login
    handleLogin();
});

// funcao responsavel por fazer a logica de login
function handleLogin() {
    // pega os valores digitados e remove os espacos vazios do email
    const email = emailInput.value.trim();
    const password = passwordInput.value;

    // verifica se os campos estao vazios
    if (!email || !password) {
        alert("por favor, preencha todos os campos.");
        return;
    }

    // efeitos visuais do botao de login
    loginSubmitButton.disabled = true;
    loginSubmitButton.innerText = "entrando...";

    // aqui entra a chamada real para a api de autenticacao
    fetch("/usuarios/autenticar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            emailServer: email,
            senhaServer: password
        })
    }).then(function (resposta) {

        // verifica se a resposta do servidor deu sucesso
        if (resposta.ok) {
            resposta.json().then(json => {
                // logica do seu checkbox (manter conectado)
                if (keepConnectedCheckbox.checked) {
                    localStorage.EMAIL_USUARIO = json.email;
                    localStorage.NOME_USUARIO = json.nome;
                    localStorage.ID_USUARIO = json.id;
                } else {
                    sessionStorage.EMAIL_USUARIO = json.email;
                    sessionStorage.NOME_USUARIO = json.nome;
                    sessionStorage.ID_USUARIO = json.id;
                }

                // redireciona para o painel de monitoramento / dashboard
                window.location.href = "../dashboard.html"; // ajuste para a sua pagina final
            });
        } else {
            console.log("houve um erro ao tentar realizar o login!");
            resposta.text().then(texto => {
                console.error(texto);
                alert("e-mail ou senha invalidos!");

                // volta o botao ao normal em caso de erro
                loginSubmitButton.disabled = false;
                loginSubmitButton.innerText = "entrar na plataforma";
            });
        }
    }).catch(function (erro) {
        console.log(erro);
        alert("erro inesperado ao conectar com o servidor.");

        // volta o botao ao normal em caso de erro
        loginSubmitButton.disabled = false;
        loginSubmitButton.innerText = "entrar na plataforma";
    });
}
