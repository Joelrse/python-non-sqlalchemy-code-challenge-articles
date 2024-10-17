class Article:
   
    all = []

    def __init__(self, author, magazine, title):

        self._author = author
        self.magazine = magazine
       
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")

        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")

        super().__setattr__('_title', title)

        Article.all.append(self)
        author.articles_list.append(self)
        magazine.articles_list.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("New author must be an instance of the Author class")
        self._author = new_author

    def __setattr__(self, key, value):
        if hasattr(self, '_title') and key == 'title':
            raise AttributeError("Cannot change the title after the article is instantiated")
        super().__setattr__(key, value)


class Author:
    def __init__(self, name):
        self.name = name
        self.articles_list = []

    def articles(self):
        return self.articles_list

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def magazines(self):
        
        magazines = {article.magazine for article in self.articles_list}
        return list(magazines)

    def topic_areas(self):
        if not self.articles_list:
            return None
        categories = {article.magazine.category for article in self.articles_list}
        return list(categories)


class Magazine:
    def __init__(self, name, category):
        
        self._name = name
        self._category = category  
        self.articles_list = []  

        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if not isinstance(category, str):
            raise TypeError("Category must be of type str")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if not category:  
            raise ValueError("Category must not be empty")

        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Category must be of type str")
        if not new_category:  
            raise ValueError("Category must not be empty")
        self._category = new_category

    def articles(self):
        return self.articles_list

    def article_titles(self):
        if not self.articles_list:
            return None
        return [article.title for article in self.articles_list]
    
    def contributors(self):
        if not self.articles_list:
            return []
        return list({article.author for article in self.articles_list})

    def contributing_authors(self):
        if not self.articles_list:
            return None
        author_count = {}
        for article in self.articles_list:
            if article.author not in author_count:
                author_count[article.author] = 0
            author_count[article.author] += 1

        authors_with_more_than_two = [author for author, count in author_count.items() if count > 2]

        return authors_with_more_than_two if authors_with_more_than_two else None

       
        

        
        
