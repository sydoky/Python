class Language:
    def __init__(self, name, release, author):
        self.name = name
        self.release = release
        self.author = author
        self.influences = [] #we will append later, we have a list

    def __str__(self):

        return self.name + ", " + str(self.release) + ", " + self.author + ", "

    def add_influence(self, influence):
        self.influences.append(influence)

class ProgrammingPedia:
    def __init__(self):
        self.programming_languages = []
        #make sting method

    def adding_language(self, language):
        self.programming_languages.append(language)

    def oldest_language(self):
        language = None # we use this line when we want to count, find specific object, search for something, summ them up
        for l in self.programming_languages:
            if language is None:
                language = l
            else:
                if l.release < language.release:
                    language = l
        return language

    def most_influenced(self):
        number_of_influences = { #we created dict because
        }
        for l in self.programming_languages:
            for influence in l.influences: #influence is a variable:
                if influence.name not in number_of_influences: #influences comes from line 6, not in
                    number_of_influences[influence.name] = 1 # 1 stand for the first time found as a influence
                else:
                    number_of_influences[influence.name] += 1 #this will increase the count
        print(number_of_influences)



Cpp = Language("C++", 1985, "Bjarne Stroustrup")
Python = Language("Python", 2001, "Guido van Rossum")
print(Python)
ABC = Language("ABC", 1987, "Leo Geurts, Lambert Meertens, Steven Pemberton")
print(ABC)
Julia = Language("Julia", 2012, "Jeff Bezanson, Alan Edelman, Stefan Karpinski, Viral B. Shah")
Go = Language("GO", 2009, "Robert Griesemer, Rob Pike, Ken Thompson")
Rust = Language("Rust", 2010, "Graydon Hoare")
WebAssembly = Language("WebAssembly", 2017, "W3C, Mozilla, Microsoft, Google, Apple")
JS = Language("Java Script", 1995, "Brendan Eich")
Solidity = Language("Solidity", 2014, "Gavin Wood")
Cs = Language("C#", 2000, "Microsoft")
Cobra = Language("Cobra", 2006, "Charles Esterbrook")
Pascal = Language("Pascal", 1970, "Niklaus Wirth")


Python.add_influence(ABC)
print(Python)
Solidity.add_influence(Python)
Solidity.add_influence(JS)
Solidity.add_influence(Cpp)

Python.add_influence(ABC)
#Python.add_influence(Cobra)

#Python.add_influence(Pascal)
#Python.add_influence(C)

Go.add_influence(Python)
#Go.add_influence(C)

Rust.add_influence(Cpp)
#Rust.add_influence(Cs)

#WebAssembly.add_influence(Cs)
WebAssembly.add_influence(Go)

#JS.add_influence(Perl)
JS.add_influence(Python)
#JS.add_influence(HyperTalk)

Solidity.add_influence(Python)
Solidity.add_influence(Cpp)
Solidity.add_influence(JS)

Wiki = ProgrammingPedia()
Wiki.adding_language(Python)
Wiki.adding_language(ABC)
Wiki.adding_language(Julia)
Wiki.adding_language(Go)
Wiki.adding_language(Rust)
Wiki.adding_language(WebAssembly)
Wiki.adding_language(JS)
Wiki.adding_language(Solidity)
#Wiki.adding_language(Perl)
print(Wiki)
print(Wiki.programming_languages)

print(Wiki.oldest_language())



print(Wiki.most_influenced())





#string methods for language + for loop see influence, and programming pedia
#finish adding influence for all of them , what is influence was by
#create a method which is the most influensive language of all,


