# Git & GitHub Hands-On Project

This project is designed to teach you **branching, commits, PRs, code reviews, conflict resolution, and Git workflows**.

## Project Overview
A simple Python task manager app with:
- Basic CLI
- Add tasks
- List tasks
- Mark tasks complete

## Folder Structure
```
git_project/
│── src/
│   └── app.py
│── docs/
│   └── workflow.md
│── requirements.txt
│── .gitignore
```

## How to Use
1. Initialize Git  
   ```
   git init
   ```

2. Create a feature branch  
   ```
   git checkout -b feature/add-task
   ```

3. Commit changes  
   ```
   git add .
   git commit -m "Added add-task functionality"
   ```

4. Push to GitHub  
   ```
   git remote add origin <repo-url>
   git push -u origin feature/add-task
   ```

5. Create Pull Request on GitHub  
6. Request code review  
7. Merge into main
