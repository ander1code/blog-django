function DesabilitarForm(){
	 $("#frmLogin :input").prop('disabled','disabled'); 
}

function LoginSucessso(){
	$("#logModal").css('color','green');
  $(".modal-title").text("Informação");
  $("#mensagem").text('Usuário logado com sucesso.'); 
  $("#btnLogin").removeClass( "btn-danger" ).addClass( "btn-success" );
  $("#logModal").modal('show');  
}

function LoginErro(){
	$("#logModal").css('color','red');
  $(".modal-title").text("Erro");
  $("#mensagem").text('Usuário e senha incorretos.'); 
  $("#btnLogin").removeClass( "btn-success" ).addClass( "btn-danger" );
  $("#logModal").modal('show');  
}