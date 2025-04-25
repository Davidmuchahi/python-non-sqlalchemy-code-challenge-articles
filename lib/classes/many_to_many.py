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
     articles = [article for article in Article.all if article.author == self]
     return articles if articles else None


    def magazines(self):
     articles = self.articles()
     if not articles:
         return None
     return list({article.magazine for article in articles})
      


        


    def add_article(self, magazine, title):
        return Article(self,magazine,title)


    def topic_areas(self):
        magazines=self.magazines()
        if not magazines:
            return None
        return list({magazine.category for magazine in magazines})
        
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value


    def articles(self):
        articles = [article for article in Article.all if article.magazine == self]
        return articles if articles else None
     

    def contributors(self):
        articles=self.articles()
        if not articles:
            return None
        return list({article.author for article in articles})


    def article_titles(self):

        articles=self.articles()
        if not articles:
            return None
        return [article.title for article in articles]


        


    def contributing_authors(self):
        articles=self.articles()
        if not articles:
            return None
        


        author_counts=[]
        for article in articles:
            author=article.author
            author_counts[author]=author_counts.get(author,0)+1


        contributing=[author for author, count in author_counts.items()if count>2]

        return contributing if contributing else None

    