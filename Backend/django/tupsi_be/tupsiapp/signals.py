from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Obtén la información necesaria del token y del usuario
    email = reset_password_token.user.email
    token = reset_password_token.key

    # Configura el contenido del correo electrónico
    subject = 'Restablecimiento de contraseña'
    message = f'Recupera la contraseña del correo "{email}" utilizando el token "{token}" desde la API http://localhost:8000/api/auth/reset/confirm/.'
    from_email = 'tu-email@ejemplo.com'
    recipient_list = [email]

    # Envía el correo electrónico
    send_mail(subject, message, from_email, recipient_list)
