{
    'name': 'To-Do / Tasks',
    'version': '16.0.0',
    'summary': 'Simple test for To-Do tasks management',
    'description': """
        Simple To-Do module with model todo.task, list/form/search views and menu.
        """,
    'author': 'ABDELGHANI MEHENNAOUI',
    'category': 'Productivity',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
    ],
    'installable': True,
    'application': True,
}
