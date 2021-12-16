from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import Usuario


class RegistroForm(UserCreationForm):

	class Meta:
		model = Usuario
		fields = [
				'username', 
				'email', 
				'password1', 
				'password2',
				]
		labels = {
				'username': 'Usuario', 
				'email': 'Email', 
				'password1': 'Contraseña', 
				'password2': 'Reingresar contraseña',
				}
				


		
