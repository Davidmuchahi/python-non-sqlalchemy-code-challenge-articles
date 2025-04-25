class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        pass
        
class Author:
    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, value):
        pass 


    def articles(self):
        pass


    def magazines(self):


        pass


    def add_article(self, magazine, title):
        pass


    def topic_areas(self):
        pass
        
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    def articles(self):
        pass

    def contributors(self):
        pass


    def article_titles(self):


        pass


    def contributing_authors(self):
        pass