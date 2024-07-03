function redirecionardeProfessorParaAluno() {
    var selecionado = document.getElementById("tipo_usuario").value;
    if (selecionado === "professor") {
        window.location.href = "/professor";
    } else if (selecionado === "aluno") {
        window.location.href = "/aluno";
    }
}
