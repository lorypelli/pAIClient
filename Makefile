run:
	@cd frontend && pnpm install && pnpm run build && \
	cd .. && \
	cd backend && poetry install --no-root && poetry run python main.py
