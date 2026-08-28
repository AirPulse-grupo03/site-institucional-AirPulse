const loginForm = document.getElementById("loginForm")
const emailInput = document.getElementById("emailInput")
const passwordInput = document.getElementById("passwordInput")
const keepConnectedCheckbox = document.getElementById("keepConnectedCheckbox")
const loginSubmitButton = document.getElementById("loginSubmitButton")

loginForm.addEventListener('submit', (event) => {
    event.preventDefault()
    handleLogin()
})

function handleLogin() {
    const email = emailInput.value.trim()
    const password = passwordInput.value

    if (!email || !password) {
        return
    }

    loginSubmitButton.disabled = true
    loginSubmitButton.innerText = "ENTRANDO..."

    // Aqui entra a chamada pra API de autenticação
    setTimeout(() => {
        if (keepConnectedCheckbox.checked) {
            localStorage.EMAIL_USUARIO = email
        } else {
            sessionStorage.EMAIL_USUARIO = email
        }

        window.location.href = "../index.html"
    }, 800)
}
