deploy:
	docker-compose down -v 
	docker-compose up --build -d
	@echo "Deployment complete. Access the broker at http://localhost:29092"
	@echo "Deployment complete. Access the schema_registry at http://localhost:8081"
	@echo "Deployment complete. Access the UI at http://localhost:9021"