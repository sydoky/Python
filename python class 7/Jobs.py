from Programming import Language

class Job:
    def __init__(self, position, required_experience, programming_language, technologies):
        self.position = position
        self.required_experience = required_experience
        self.programming_language = programming_language
        self.technologies = technologies
    def __str__(self):
        return self.position + ", " + str(self.required_experience) + " yoe, " + self.programming_language.name \
    + str(self.technologies)

class Company:
    def __init__(self, name):
        self.name = name
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    def show_jobs(self):
        for j in self.jobs:
            print(j)

    def show_specific_jobs(self, programming_language):
        for j in self.jobs:
            if j.programming_language.name == programming_language:
                print(j)

    def show_jj(self):
        for one_year in self.jobs:
            if one_year.required_experience == 1: #for checking we use == sign
                print(one_year)

    def show_js(self):
        for five_year in self.jobs:
            if five_year.required_experience >= 5:
                print(five_year)




    def __str__(self):
        return self.name

Cpp = Language("C++", 1985, "Bjarne Stroustrup")
Rust = Language("Rust", 2010, "Graydon Hoare")
JS = Language("Java Script", 1995, "Brendan Eich")
Python = Language("Python", 2001, "Guido van Rossum")
Solidity = Language("Solidity", 2014, "Gavin Wood")
print(Python)
Python_junior = Job("Junior Python Developer", 1, Python, ["core python", "django", "html", "css", "general db knowledge"])
Python_medior = Job("Medior Python Developer", 3, Python, ["core python", "django", "html", "css", "general db knowledge", "git", "aws", "REST"])
Python_senior = Job("Medior Python Developer", 5, Python, ["core python", "django", "html", "css", "general db knowledge", "git", "aws", "REST", "docker", "cd/si", "kubernetes", "jenkins"])
Cpp_junior = Job("Junior C++ Developer", 1, Cpp, ["core C++", "embeded", "algarithms", "data structure", "general db knowledge"])
Rust_junior = Job("Junior Rust Developer", 1, Rust, ["core rust", "cargo", "WebAssembly", "Multi-threading"])
JS_junior = Job("Junior Java Script Developer", 1, JS, ["core java script", "ECMA6", "html", "css", "react"])
Solidity_junior = Job("Junior Solidity Developer", 1, Solidity, ["core solidity", "ethereum", "truffle", "ganache", "java script basics"])

print(Python_junior)
Google = Company("Google")
Apple = Company("Apple")

print(Google)
Google.add_job(Python_junior)
print(Google)
Google.add_job(Python_medior)
Google.add_job(Python_senior)
Google.add_job(Cpp_junior)
Google.add_job(Rust_junior)
Google.add_job(JS_junior)
Google.add_job(Solidity_junior)
Apple.add_job(Solidity_junior)
Apple.add_job(JS_junior)
Apple.add_job(Python_senior)
Google.show_jobs()
Google.show_specific_jobs("Rust")

Apple.show_specific_jobs("Solidity")

print("---------")

Google.show_jj()
print("--------")
Google.show_js()
Apple.show_js()

