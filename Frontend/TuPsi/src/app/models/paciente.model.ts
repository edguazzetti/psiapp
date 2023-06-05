export interface Paciente {
    id?: number;
    dni: number;
    nombre: string;
    apellido: string;
    sexo: string;
    telefono: number;
    terapia: string;
    email: string; 
    clave: string;
    provincia: string;
    localidad: string;
    suscripcion?: boolean;
    plan?: string;
    editando?: boolean; // Propiedad editando opcional
  }
  