from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'create_new_producto': True,
        'view_producto_template': True,
        'view_results': True,
        'new':True,
    }

class Supervisor(AbstractUserRole):
    available_permissions = {
        'view_producto_template': True,
        'edit_patient_file': True,
    }

class Soporte(AbstractUserRole):
    available_permissions = {
        'view_producto_template': True,
        'edit_patient_file': True,
    }

class Cliente(AbstractUserRole):
    available_permissions = {
        'view_content': True,
        'new':False,
    }