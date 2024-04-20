run:
	cd frontend && npm i && npm run build && \
	cd .. && \
	cd backend && poetry install --no-root && poetry run python main.py