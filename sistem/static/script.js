/* FUNCION QUE CONSULTA LA HORA ACTUAL Y LE DA FORMATO */



function eliminarregistro(id,objeto,objeto2){
 
	swal({
		title: "Estas Seguro de Eliminar el registro con numero: "+ id+" ?",
		text: "Una vez eliminado el resgistro "+ objeto +":"+objeto2,
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