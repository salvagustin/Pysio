/* VARIABLA PARA EVALUAR LOS INPUT VACIOS */
var exp = /^[W]{1}[K]{1}\d{2}-\d{4}$/



/* FUNCION PARA ELIMINAR REGISTROS */
function eliminarregistro(id,objeto,objeto2){
	swal({
		title: "Eliminar registro numero: "+ id+" ?",
		text: objeto +": "+objeto2,
		icon: "warning",
		buttons: true,
		dangerMode: false,
	})
		.then((OK) => {
			if (OK) {
				location.href="/eliminar"+objeto+"/"+id;
				
			} else {
				swal("Su registro No fue Eliminado");
			}
		});
	}

function buscarsemana(){
	const week = document.getElementsByName('week')[0].value;
	if( week == null || week.length == 0 || exp.test(week) ) {
		swal({
			title: "!Campo vacio!",
			text: "Seleccione una semana",
			timer: 2000,
			showConfirmButton: false});
	}else{
		numano = week.substr(0,4)
		numse = week.substr(6,2)
		location.href = "/buscarsemana/"+ numano + "/"+ numse
	}	
}

function buscar_paciente(){
	const name = document.getElementsByName('nombre')[0].value;
	if( name == null || name.length == 0 || exp.test(name) ) {
		location.href = "/pacientes/"
		swal({
			title: "!Campo vacio!",
			text: "Seleccione un nombre",
			timer: 3000,
			showConfirmButton: false});
			
	}else{

		location.href = "/buscarpaciente/"+ name
	}	
}
function buscar_consulta(){
	const name = document.getElementsByName('consulta')[0].value;
	if( name == null || name.length == 0 || exp.test(name) ) {
		swal({
			title: "!Campo vacio!",
			text: "Seleccione un nombre",
			timer: 3000,
			showConfirmButton: false});
			location.href = "/consultas/"
	}else{

		location.href = "/buscarconsulta/"+ name
	}	
}