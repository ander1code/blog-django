function DisableForm() {
  $("#frmLogin :input").prop("disabled", "disabled");
}

function SuccessfullyLogin() {
  $("#logModal").css("color", "green");
  $(".modal-title").text("Information");
  $("#mensagem").text("Successfully logged.");
  $("#btnLogin").removeClass("btn-danger").addClass("btn-success");
  $("#logModal").modal("show");
}

function LoginError() {
  $("#logModal").css("color", "red");
  $(".modal-title").text("Erro");
  $("#mensagem").text("Invalid Username and Password.");
  $("#btnLogin").removeClass("btn-success").addClass("btn-danger");
  $("#logModal").modal("show");
}
