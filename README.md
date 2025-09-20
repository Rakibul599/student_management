# Student Management Module

## Overview

This is a custom **Odoo module** developed for managing **Students** and **Courses**.  
It allows you to create students, create courses, and enroll students into multiple courses.  
You can also generate reports showing all students enrolled in a specific course.

- Built with **Python, PostgreSQL, and XML (Odoo Framework)**
- Beginner-friendly, for learning Odoo module development

---

## Features

- **Student Management**

  - Add students with name, email, roll number, department
  - Enroll students in multiple courses

- **Course Management**

  - Add courses with name, code, and credit hours
  - View enrolled students per course

- **Reports**

  - Generate a PDF report showing all students enrolled in a specific course

- **Bonus**
  - New top-level menu: **Student Management → Students / Courses**
  - Button on **Student Form** → “Show Enrolled Courses”

---

## Installation

### 1. Install Odoo

Clone Odoo and install dependencies:

```bash
git clone https://github.com/odoo/odoo --branch 19.0 --depth 1
cd odoo
python3.10 -m venv venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Install PostgreSQL

This command is for Fedora OS. Please make sure you have installed your operating system.

```bash
sudo dnf install postgresql -y
sudo -u postgres createuser -s odoo
```

### 3. Add Custom Module

Clone my repository into your Odoo folder.

```bash
mkdir custom_module
cd custom_module
git clone https://github.com/Rakibul599/student_management

```

## Run Application

- First, go to the /debian directory and find the odoo.config file, then copy it to your root directory.
- Set your db_user and db_password, and configure the addons_path to point to your custom module’s relative path.

#### Run Odoo

```bash
./odoo-bin -c odoo.conf

```

- After running this command, the Odoo server will start on port 8069.
- Open http://localhost:8069/
  in your browser and log in.
- Search for the app using its technical name student_management and install it.

## Challenges Faced and Solutions

Since this was my first Odoo development project, I faced several challenges:

### 1. Understanding Odoo Basics  
At first, I was unfamiliar with Odoo’s framework (models, views, security, reports).  

**Solution:** I studied the official Odoo documentation to understand the structure.  

---

### 2. Learning by Practice  
Implementing many-to-many relations, XML views, and access rights was challenging.  

**Solution:** I watched YouTube crash courses on Odoo development to see practical examples.  

---

### 3. Debugging Errors  
I encountered common errors such as:  
- `ir.model.access.csv` issues  
- Undefined view types  
- `RPC_ERROR`  

**Solution:** I used ChatGPT for step-by-step guidance and debugging support.  

---

## Key Takeaways  

Through these challenges, I gained:  

- Practical knowledge of Odoo module development  
- Skills in **Python + PostgreSQL + XML integration**  
- Confidence as a quick learner who can solve problems independently  
