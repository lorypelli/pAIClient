run:
	cd frontend && npm install && npm run build && \
	cd .. && \
	cd backend && poetry install --no-root && poetry run python main.py