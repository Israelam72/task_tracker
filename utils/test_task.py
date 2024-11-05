import unittest
from unittest.mock import patch, MagicMock
from datetime import date
from utils.add_task import add_task 


class TestAddTask(unittest.TestCase):
    @patch('os.path.exists')
    @patch('utils.json_handler.json_load')
    @patch('utils.json_handler.json_dump')
    def test_add_first_task(self, mock_json_dump, mock_json_load, mock_exists):
        # Configura os mocks
        mock_exists.return_value = False  # Simula que o arquivo não existe
        mock_json_load.return_value = {}  # Simula que o JSON está vazio

        # Chama a função para adicionar a primeira tarefa
        add_task("Primeira tarefa")

        # Verifica se a função json_dump foi chamada com a estrutura correta
        expected_task = {
            "tasks": [
                {
                    "task": "Primeira tarefa",
                    "id": 1,
                    "status": "todo",
                    "createdAt": str(date.today()),
                    "updatedAt": str(date.today())
                }
            ]
        }
        # mock_json_dump.assert_called_once_with(expected_task)

    @patch('os.path.exists')
    @patch('utils.json_handler.json_load')
    @patch('utils.json_handler.json_dump')
    def test_add_subsequent_task(self, mock_json_dump, mock_json_load, mock_exists):
        # Configura os mocks
        mock_exists.return_value = True  # Simula que o arquivo existe
        mock_json_load.return_value = {
            "tasks": [
                {
                    "task": "Primeira tarefa",
                    "id": 1,
                    "status": "todo",
                    "createdAt": str(date.today()),
                    "updatedAt": str(date.today())
                }
            ]
        }

        # Chama a função para adicionar uma nova tarefa
        add_task("Segunda tarefa")

        # Verifica se a função json_dump foi chamada com a nova tarefa adicionada
        expected_task = {
            "tasks": [
                {
                    "task": "Primeira tarefa",
                    "id": 1,
                    "status": "todo",
                    "createdAt": str(date.today()),
                    "updatedAt": str(date.today())
                },
                {
                    "task": "Segunda tarefa",
                    "id": 2,
                    "status": "todo",
                    "createdAt": str(date.today()),
                    "updatedAt": str(date.today())
                }
            ]
        }
        # mock_json_dump.assert_called_once_with(expected_task)