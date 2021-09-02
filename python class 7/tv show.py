class TV_Show:
    def __init__(self, title, language, number_of_episodes):
        self.title = title
        self.language = language
        self.number_of_episdoes = number_of_episodes
        self.finished = False
        self.translation = []

    def add_translation(self, language):
        self.translation.append(language)

    def language_option(self):
        translation = ""
        for l in self.translation:
            translation += str(l + ",")

        print("The available languages for", self.title, " are ", translation)

    def finish(self):
        self.finished = True

    def new_language(self, language):
        self.language = language

    def check_language(self):
        print("the tv show ", self.title, " is in ", self.language)

    def playing(self):
        self.finished = False
        self.number_of_episdoes += 24
    def count(self):
        print("tv show ", self.title, " has ", self.number_of_episdoes, " episodes")
    def is_it_finished(self):
        if self.finished:
            print("The tv show ", self.title, " is over")
        else:
            print("The tv show ", self.title, " is still on")

tv_show = TV_Show("El Clon", "Spanish", 250)
tv_show2 = TV_Show("The Robot", "English", 35)


tv_show2.is_it_finished()
tv_show.is_it_finished()

tv_show.finish()
tv_show.is_it_finished()

tv_show.playing()
tv_show.is_it_finished()

tv_show.count()
tv_show2.count()
tv_show2.playing()
tv_show2.count()

tv_show.check_language()
tv_show.new_language("English")
tv_show.check_language()

tv_show2.check_language()
tv_show2.new_language("Spanish")
tv_show2.check_language()

tv_show.add_translation("Serbian")
tv_show.add_translation("Russian")
tv_show.language_option()