function redirecionarPagina() {
    var selecionado = document.getElementById("tipo_usuario").value;
    if (selecionado === "") {
        window.location.href = "/";
    } else if (selecionado === "professor") {
        window.location.href = "/professor";
    } else if (selecionado === "aluno") {
        window.location.href = "/aluno";
    }
}

function ArmazenarLogineSenha() {
    const rememberMeCheckbox = document.getElementById('rememberMe');
    const emailInput = document.getElementById('email');
    const senhaInput = document.getElementById('senha');

    if (rememberMeCheckbox.checked) {
        localStorage.setItem('email', emailInput.value);
        localStorage.setItem('senha', senhaInput.value);
    } else {
        localStorage.removeItem('email');
        localStorage.removeItem('senha');
    }
}

// Para carregar os dados ao carregar a página
document.addEventListener('DOMContentLoaded', (event) => {
    const emailInput = document.getElementById('email');
    const senhaInput = document.getElementById('senha');

    emailInput.value = localStorage.getItem('email') || '';
    senhaInput.value = localStorage.getItem('senha') || '';
});


function redirecionardeAlunoParaProfessor() {
    var selecionado = document.getElementById("tipo_usuario").value;
    if (selecionado === "aluno") {
        window.location.href = "/aluno";
    } else if (selecionado === "professor") {
        window.location.href = "/professor";
    }
}

function redirecionardeProfessorParaAluno() {
    var selecionado = document.getElementById("tipo_usuario").value;
    if (selecionado === "professor") {
        window.location.href = "/professor";
    } else if (selecionado === "aluno") {
        window.location.href = "/aluno";
    }
}
