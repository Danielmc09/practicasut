function abrir_modal_edicion(url) {
    $('#editar').load(url, function () {
        $(this).modal({
            backdrop: 'static',
            keyboard: false,
        });
        $(this).modal('show');
    });
}

function abrir_modal_desactivar(url) {
    $('#inactivar').load(url, function () {
        $(this).modal({
            backdrop: 'static',
            keyboard: false,
        });
        $(this).modal('show');
    });
}

function abrir_modal_eliminar(url) {
    $('#eliminar').load(url, function () {
        $(this).modal({
            backdrop: 'static',
            keyboard: false,
        });
        $(this).modal('show');
    });
}

function abrir_modal_creacion(url) {
    $('#creacion').load(url, function () {
        $(this).modal({
            backdrop: 'static',
            keyboard: false,
        });
        $(this).modal('show');
    });
}

function cerrar_modal_creacion() {
    $('#creacion').modal('hide');
}

function cerrar_modal_edicion() {
    $('#editar').modal('hide');
}

function cerrar_modal_desactivar() {
    $('#inactivar').modal('hide');
}

function cerrar_modal_eliminacion() {
    $('#eliminar').modal('hide');
}

function activarBoton() {
    if ($('#boton_creacion').prop('disabled')) {
        $('#boton_creacion').prop('disabled', false);
    } else {
        $('#boton_creacion').prop('disabled', true);
    }
}

function mostrarErroresCreacion(errores) {
    //console.log(errores);
    $('#id_').html("");
    for (let err in errores.responseJSON.error) {
        //console.log(err);
        if (err) {
            $('#id_' + err).addClass(" is-invalid");
        }
    }
}

function mostrarErroresEdicion(errores) {
    $('#id_').html("");
    for (let err in errores.responseJSON.error) {
        //console.log(err);
        if (err) {
            $('#id_' + err).addClass(" is-invalid");
        }
    }
}

// Notificación error Sweet Alert

function notificacionError(mensaje) {
    Swal.fire({
        title: 'Error!',
        text: mensaje,
        icon: 'error',
        showConfirmButton: false,
        timer: 4000
    });
}

// Notificación success Sweet Alert

function notificacionSuccess(mensaje) {
    Swal.fire({
        title: 'Buen trabajo!',
        text: mensaje,
        icon: 'success',
        showConfirmButton: false,
        timer: 4000
    });
}

// Notificación Eliminacion Sweet Alert

function notificacionDanger(mensaje) {
    Swal.fire({
        title: 'Eliminado correctamente!',
        text: mensaje,
        icon: 'danger',
        showConfirmButton: false,
        timer: 4000
    });
}

// Notificación Eliminacion Sweet Alert

function notificacionWarning(mensaje) {
    Swal.fire({
        title: 'Desactivado correctamente!',
        text: mensaje,
        icon: 'warning',
        showConfirmButton: false,
        timer: 4000
    });
}

$(document).ready(function () {
    var table = $('#tableData').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "language": {
            url: "https://cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json",
        },
    });

});