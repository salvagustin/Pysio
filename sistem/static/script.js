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
	numano = week.substr(0,4)
	numse = week.substr(6,2)
	//swal(numano+numse)
	location.href = "/buscarsemana/"+ numano + "/"+ numse
}