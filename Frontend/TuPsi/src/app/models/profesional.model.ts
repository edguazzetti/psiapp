export interface Profesional {
    id?: number,
    username?: string,
    nombre: string,
    apellido: string,
    dni?: number,
    sexo: string,
    telefono: number,
    terapiaprofesional: string, 
    email: string,
    password:string,
    provincia: string,
    localidad: string,
    matricula: number,
    editando?: boolean; // Propiedad editando opcional
}
