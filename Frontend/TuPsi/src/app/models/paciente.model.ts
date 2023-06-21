export interface Paciente {
    username?:string;
    id?: number;
    dni: number;
    name: string;
    lastname: string;
    sexo: string;
    telefono: number;
    terapiapaciente?: string;
    email: string; 
    password: string;
    provincia: number;
    localidad: string;
    suscripto?: boolean;
    planactual?: string;
    editando?: boolean; // Propiedad editando opcional
    token?: string;
  }
  
