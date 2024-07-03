function redirecionardeAlunoParaProfessor() {
    var selecionado = document.getElementById("tipo_usuario").value;
    if (selecionado === "aluno") {
        window.location.href = "/aluno";
    } else if (selecionado === "professor") {
        window.location.href = "/professor";
    }
}