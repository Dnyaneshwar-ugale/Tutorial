# Git Workflow Explanation

## 1. Branching Strategy
- main → stable production-ready code
- feature/* → new features
- bugfix/* → fixes
- hotfix/* → urgent issues on main
- release/* → release preparation

## 2. Feature Development Example
```
git checkout -b feature/add-list-endpoint
```
Work on task…

```
git add .
git commit -m "Implemented list endpoint"
git push -u origin feature/add-list-endpoint
```

Create PR → teammates review → merge to main.
