# Variables - no type declaration needed, Python infers it
name = "Enterprise Architect"
years_experience = 15
hourly_rate = 85.50
is_certified = True

print(f"{name} has {years_experience} years of experience")
print(f"Rate: ${hourly_rate}/hr, Certified: {is_certified}")

# Lists (ordered, mutable)
skills = ["AWS", "Kubernetes", "Terraform"]
skills.append("Python")
print(skills)

# Dictionaries (key-value pairs) - you'll use these constantly with AWS APIs
architect = {
    "name": name,
    "skills": skills,
    "years": years_experience
}
print(architect["skills"])
