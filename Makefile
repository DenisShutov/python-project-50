#установка зависимостей
install:
	uv sync

#запуск тестов
test:
	uv run pytest

#проверка стиля когда
lint:
	uv run ruff check gendiff

#последовательный запуск test, потом lint
check: test lint

#автоисправление линтера 
lint-fix:
	uv run ruff check --fix gendiff

#запуск тестов, измерение покрытия, создаёт 
#файл coverage.xml для SonarCloud
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

#проверяет дирректорию gendiff и выовдит процент
#покрытия тестами каждого файла
test-short:
	uv run pytest --cov=gendiff

# Объявляем, что это цели-команды, а не файл
.PHONY: install test lint selfcheck check build