import { Component, OnInit, OnDestroy } from '@angular/core';
import { PacienteService } from 'src/app/services/paciente.service';
import { Paciente } from 'src/app/models/paciente.model';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-admin-pacientes',
  templateUrl: './admin-pacientes.component.html',
  styleUrls: ['./admin-pacientes.component.css'],
})
export class AdminPacientesComponent implements OnInit, OnDestroy {
  Pacientes: Paciente[] = [];
  pacienteCreadoSubscription: Subscription = Subscription.EMPTY;
  tienePacientes: boolean = false;

  constructor(private servicioPacientes: PacienteService) {}

  ngOnInit() {
    this.verPacientes(); //funcion encargada de cargar los datos de los pacientes
    this.pacienteCreadoSubscription = this.servicioPacientes
      .getPacienteCreadoObservable() //el observable hace callback cuando se emita un nuevo paciente.
      .subscribe((paciente) => {
        this.Pacientes.push(paciente); //tomamos ese paciente y lo agregamos al arreglo Pacientes
        this.tienePacientes = true; //al no estar vacio el arreglo cambiamos a true esta propiedad
      });
  }

  ngOnDestroy() {
    this.pacienteCreadoSubscription.unsubscribe();
  } //  cancela la suscripción al observable

  verPacientes() {
    this.servicioPacientes.getPaciente().subscribe(
      //llama al método getPaciente() del servicio. La función subscribe() suscribe al observable devuelto por getPaciente()
      (data) => {
        //es la funcion del callback para recibir sus datos cuando esten disponibles
        this.Pacientes = data; //asignamos el callback al array Pacientes
        this.tienePacientes = this.Pacientes.length > 0; //para pasar a true la propiedad
      },
      (error) => {
        console.log(error); //si hay error lo muestra en consola
      }
    );
  }

  editarPaciente(item: Paciente) {
    //toma el parametro item de tipo Paciente
    item.editando = true; //lo usamos en true cuand queremos editar la informacion de los inputs
  }

  cancelarEdicion(item: Paciente) {
    //toma el parametro item de tipo Paciente
    item.editando = false; //cancela el estado edicion y vuelve a su ultimo estado guardado
  }

  guardarCambios(item: Paciente) {
    //toma el parametro item de tipo Paciente
    this.servicioPacientes.updatePaciente(item).subscribe(
      //llama la funcion updatePaciente del servicio y suscribe el obesarvable para devolver la info por callback
      (pacienteActualizado) => {
        //nombre de la info que trae el callback
        item.editando = false; //pasamos a false la edicion
        console.log('Paciente actualizado:', pacienteActualizado); //mostramos en consola el paciente que actualizamos
      },
      (error) => {
        console.log('Error al actualizar el paciente:', error); //si hay error lo mostramos en consola
      }
    );
  }

  eliminarPaciente(id: number) {
    //eliminamos el paciente, tomamos como parametro el id del paciente q es de tipo number
    this.servicioPacientes.deletePaciente(id).subscribe(
      //traemos el servicio deletePaciente para eliminar el paciente correspondiente al ID proporcionado y nos suscribimos al callback del observable
      () => {
        //Esta es la función de callback que se ejecuta cuando la eliminación del paciente es exitosa. No toma ningún parámetro porque simplemente se ejecuta una vez que la eliminación se ha completado correctamente.
        console.log('Paciente eliminado con ID:', id); //si sale todo bien mostramos ese msj en consola
        this.verPacientes(); //actualiza la lista de pacientes mostrada en la interfaz de usuario para reflejar los cambios.
      },
      (error) => {
        console.log('Error al eliminar el paciente:', error);
      } //si hay error mostramos ese mensaje en consola
    );
  }
}
