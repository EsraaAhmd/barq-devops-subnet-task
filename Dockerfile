# Use lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy all local project files (excluding those in .dockerignore)
COPY . .

# Install dependencies (pandas, matplotlib, openpyxl)
RUN pip install --no-cache-dir pandas matplotlib openpyxl

# Default command: run analyzer and visualizer
CMD ["sh", "-c", "python subnet_analyzer.py && python visualize.py"]

