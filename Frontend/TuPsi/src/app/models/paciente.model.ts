export interface Paciente {
    username?:string;
    id?: number;
    dni: number;
    nombre: string;
    apellido: string;
    sexo: string;
    telefono: number;
    terapiapaciente?: number;
    email: string; 
    password: string;
    provincia: number;
    localidad: string;
    suscripto?: boolean;
    planactual?: string;
    editando?: boolean; // Propiedad editando opcional
    token?: string;
  }
  
