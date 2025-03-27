import os

# Define the directory structure
DIRS = [
    "app",
    "models",
    "tests",
    "docs",
    "deployment",
    "data"
]

FILES = {
    "app": ["main.py", "itinerary_generator.py", "prompts.py", "web_search.py", "utils.py"],
    "models": ["ai_model.py"],
    "tests": ["test_itinerary.py", "test_prompts.py"],
    "docs": ["README.md", "prompts_explanation.md"],
    "deployment": ["gradio_app.py", "requirements.txt"],
    "data": ["attractions_db.json"],
    "root": [".gitignore", "requirements.txt", "README.md"]
}

def create_directories():
    for directory in DIRS:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def create_files():
    for directory, files in FILES.items():
        for file in files:
            file_path = file if directory == "root" else os.path.join(directory, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    pass  # Create an empty file
                print(f"Created file: {file_path}")

def main():
    create_directories()
    create_files()
    print("Project setup completed successfully!")

if __name__ == "__main__":
    main()