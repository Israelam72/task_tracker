# Task Manager CLI

This is a simple Python project to manage and track your tasks.

## Description

The **Task Manager CLI** allows you to add, update, delete, and list tasks, as well as mark each task's status as "in progress" or "done." 
This project was created to make it easy to manage and keep track of tasks directly from the terminal.

## Clone
```bash
git clone https://github.com/Israelam72/task_tracker.git
```

## Getting Started

To start the Task Manager CLI, run the following command:
```bash
python main.py
```

## Examples
### Add a task:
```bash
taskctl -a "Study Python"
```

### Update a task:
```bash
taskctl -u 1 "Study advanced Python"
```

### Mark a task as "in progress":
```bash
taskctl -mp 1
```

### Mark a task as "done":
```bash
taskctl -md 1
```

### List all tasks:
```bash
taskctl -l
```
### To see more:
```bash
taskctl -h
````

# Requirements
Python 3.x

