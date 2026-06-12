from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class UserManagementTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Crear un superusuario para simular el administrador logueado
        self.admin_user = User.objects.create_superuser(
            username='admin_test',
            email='admin@test.com',
            password='adminpassword123'
        )
        # Crear un usuario normal para pruebas
        self.normal_user = User.objects.create_user(
            username='87654321',
            email='87654321@metropolitano.com',
            password='oldpassword123',
            first_name='Juan',
            last_name='Perez'
        )

    def test_admin_users_list_data_requires_login(self):
        """Verifica que el listado de usuarios requiere estar logueado."""
        response = self.client.get(reverse('admin_users_list_data'))
        self.assertEqual(response.status_code, 302)  # Redirecciona al login

    def test_admin_users_list_data_success(self):
        """Verifica que se liste correctamente a los usuarios."""
        self.client.login(username='admin_test', password='adminpassword123')
        response = self.client.get(reverse('admin_users_list_data'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('data', data)
        # Debe haber al menos el usuario normal (el admin se excluye por ser superuser)
        self.assertEqual(len(data['data']), 1)
        self.assertEqual(data['data'][0]['username'], '87654321')

    def test_crear_usuario_manual_success(self):
        """Verifica la creación manual exitosa de un usuario."""
        self.client.login(username='admin_test', password='adminpassword123')
        response = self.client.post(reverse('crear_usuario_manual'), {
            'username': '12345678',
            'first_name': 'Maria',
            'last_name': 'Flores',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        
        # Verificar en base de datos
        user_exists = User.objects.filter(username='12345678').exists()
        self.assertTrue(user_exists)
        user = User.objects.get(username='12345678')
        self.assertEqual(user.first_name, 'Maria')
        self.assertEqual(user.last_name, 'Flores')

    def test_crear_usuario_manual_duplicate(self):
        """Verifica que no se pueda crear un usuario con un DNI existente."""
        self.client.login(username='admin_test', password='adminpassword123')
        response = self.client.post(reverse('crear_usuario_manual'), {
            'username': '87654321',  # ya existe
            'first_name': 'Otro',
            'last_name': 'Nombre',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('ya existe', data['message'])

    def test_toggle_user_status(self):
        """Verifica el cambio de estado (activo/inactivo) de un usuario."""
        self.client.login(username='admin_test', password='adminpassword123')
        # Verificar estado inicial
        self.assertTrue(self.normal_user.is_active)
        
        # Cambiar a inactivo
        response = self.client.post(reverse('toggle_user_status', args=[self.normal_user.id]))
        self.assertEqual(response.status_code, 200)
        
        # Recargar y verificar
        self.normal_user.refresh_from_db()
        self.assertFalse(self.normal_user.is_active)
        
        # Cambiar a activo nuevamente
        response = self.client.post(reverse('toggle_user_status', args=[self.normal_user.id]))
        self.assertEqual(response.status_code, 200)
        
        self.normal_user.refresh_from_db()
        self.assertTrue(self.normal_user.is_active)

