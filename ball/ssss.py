import random

# Функция для генерации списка учеников
def generate_students(num_students):
    return [f"Ученик {i+1}" for i in range(1, num_students)]

# Функция для генерации билетов
def generate_tickets(num_tickets):
    return [f"Билет {i+1}" for i in range(num_tickets)]

# Функция для назначения билетов ученикам
def assign_tickets(students, tickets, tickets_per_student):
    assignments = {}
    
    for student in students:
        # Случайным образом выбираем уникальные билеты для ученика
        assigned_tickets = random.sample(tickets, tickets_per_student)
        assignments[student] = assigned_tickets
    
    return assignments

# Параметры
num_students = 12  # Количество учеников
num_tickets = 12  # Общее количество билетов
tickets_per_student = 1  # Количество билетов для каждого ученика

# Генерация учеников и билетов
students = generate_students(num_students)
tickets = generate_tickets(num_tickets)

# Назначение билетов ученикам
ticket_assignments = assign_tickets(students, tickets, tickets_per_student)

# Вывод результатов
for student, assigned_tickets in ticket_assignments.items():
    print(f"{student}: {', '.join(assigned_tickets)}")