import requests
from requests.packages.urllib3 import add_stderr_logger
add_stderr_logger()
from bs4 import BeautifulSoup
# from urllib.error import HTTPError
import re, random, datetime
random.seed(datetime.datetime.now())
#import os
# load variable environment
import os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(path, '.env')
print(dotenv_path)
from dotenv import load_dotenv
load_dotenv(dotenv_path)

class AutoScrapping:
   # url pour login
   url_base = "https://github.com/"
   url_login = "https://github.com/login"
   # ouvrir une session
   session = requests.Session()

   # login mon compte pour github me permet d'utiliser son site
   per_session = session.post(url_login,
                              data={'login':os.getenv('id'), 'password':os.getenv('password')}, 
                              headers={"referer":url_base})

   # la critère du scrapping
   key_search = ["repositories", "stars", "followers", "following"]
   def __init__(self,url_scrapped):
      self.url_scrapped = url_scrapped

   def infoPerso(self):
      # information hors de boucle
      soup = BeautifulSoup(self.session.get(self.url_scrapped).content, 'html.parser')
      # try:
      #    img = soup.find("img", {"class":"avatar width-full avatar-before-user-status"}).attrs["src"]
      # except:
      #    img = soup.find("img", {"class":"avatar width-full rounded-2"}).attrs["src"]
      try:
         full_name = soup.find("span",{"class":"p-name vcard-fullname d-block overflow-hidden"}).text
      except:
         full_name = "Unknown"
      acc_name = soup.find("span",{"class":"p-nickname vcard-username d-block"}).text
      try:
         bio = soup.find("div", {"class":"p-note user-profile-bio mb-3"}).find("div").text
      except:
         bio = "Unknown"
      try:
         location = soup.find("li",{"itemprop":"homeLocation"}).find("span").text
      except:
         location = "Unknown"
      # print(full_name)
      # print(acc_name)
      # print(bio)
      # print(location)

      return acc_name, full_name, bio, location

   def repoScrapping(self):
      # --------------------------------------
      # Repositories:
      params = {
         "tab": self.key_search[0]
      }  
      #it assumed that by now you are logged so we can now use .get and fetch any page of your choice
      soup = BeautifulSoup(self.session.get(self.url_scrapped, params=params).content, 'html.parser')
      repo = soup.find("ul", {"data-filterable-for":"your-repos-filter"})
      list_repo = repo.findAll("li",{"itemprop":"owns"})
      # cherche les infos pour chaque repo:
      repository = list()
      used_lang = list()
      for repo_ in list_repo:
         repository.append(repo_.find("a",{"itemprop":"name codeRepository"}).text.strip())
         try:
            used_lang.append(repo_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
         except:
            used_lang.append("Unknown")
      # ---
      # Pagination:
      pa = soup.find("div",{"class":"pagination"})
      # s'il y a un seul page, on n'a pas besoin des codes au-dessous
      if pa != None:
         next_ = pa.findAll("a")
         # print(next_)
         for n in next_:
            # print(n.text)
            # print(n.attrs["href"])
            if n.text == "Next":
               soup_sub = BeautifulSoup(self.session.get(n.attrs["href"]).content, 'html.parser')
               repo = soup_sub.find("ul", {"data-filterable-for":"your-repos-filter"})
               list_repo = repo.findAll("li",{"itemprop":"owns"})
               for repo_ in list_repo:
                  repository.append(repo_.find("a",{"itemprop":"name codeRepository"}).text.strip())
                  try:
                     used_lang.append(repo_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
                  except:
                     used_lang.append("Unknown")
      # print(repository)
      # print(used_lang)
      return repository, used_lang

   def starScrapping(self):
      # --------------------------------------
      # Stars
      params = {
         "tab": self.key_search[1]
      }  
      #it assumed that by now you are logged so we can now use .get and fetch any page of your choice
      star = BeautifulSoup(self.session.get(self.url_scrapped, params=params).content, 'html.parser')
      list_stars = star.findAll("div",{"class":"col-12 d-block width-full py-4 border-bottom"})
      # cherche les infos pour chaque repo:
      repository_star = list()
      used_lang_star = list()
      for star_ in list_stars:
         repository_star.append(star_.find("div",{"class":"d-inline-block mb-1"}).find("a").attrs["href"].lstrip("/"))
         try:
            used_lang_star.append(star_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
         except:
            used_lang_star.append("Unknown")
      # ---
      # Pagination:
      pa = star.find("div",{"class":"pagination"})
      # s'il y a un seul page, on n'a pas besoin des codes au-dessous
      if pa != None:
         next_ = pa.findAll("a")
         # print(next_)
         for n in next_:
            # print(n.text)
            # print(n.attrs["href"])
            if n.text == "Next":
               star = BeautifulSoup(self.session.get(n.attrs["href"]).content, 'html.parser')
               # star = soup_sub.find("div", {"class":"d-lg-flex gutter-lg mt-4"})
               list_stars = star.findAll("div",{"class":"col-12 d-block width-full py-4 border-bottom"})
               for star_ in list_stars:
                  repository_star.append(star_.find("div",{"class":"d-inline-block mb-1"}).find("a").attrs["href"].lstrip("/"))
                  try:
                     used_lang_star.append(star_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
                  except:
                     used_lang_star.append("Unknown")
      # print(repository_star, len(repository_star))
      # print(used_lang_star, len(used_lang_star))
      return repository_star, used_lang_star
# try:
   
   def followerScrapping(self):
      # --------------------------------------
      # Followers
      params = {
         "tab": self.key_search[2]
      }  
      #it assumed that by now you are logged so we can now use .get and fetch any page of your choice
      follower = BeautifulSoup(self.session.get(self.url_scrapped, params=params).content, 'html.parser')
      list_followers = follower.findAll("div",{"class":"d-table table-fixed col-12 width-full py-4 border-bottom border-gray-light"})
      # cherche les infos pour chaque repo:
      followers_name = list()
      followers_acc = list()
      followers_bio = list()
      followers_location = list()


      for foll_ in list_followers:
         # pour les comptes n'est pas mise à jour son Nom Prenom sur github
         try:
            followers_name.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                           .find("span",{"class":"f4 link-gray-dark"}).text.lstrip())
         except:
            followers_name.append("Unknown")
         # c'est évidant que le nom du compte qui exists
         followers_acc.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                        .find("span",{"class":"link-gray pl-1"}).text.lstrip())
         # Comme nom du compte, bio info peut être ne pas exister        
         try:
            followers_bio.append(foll_.find("div",{"class":"text-gray text-small mb-2"}).find("div").text.strip())
         except:
            followers_bio.append("Unknown")

         # location:
         try:
            followers_location.append(foll_.find("p",{"class":"text-gray text-small mb-0"}).text.strip())
         except:
            followers_location.append("Unknown")
      # ---
      # Pagination:
      pa = follower.find("div",{"class":"pagination"})
      # s'il y a un seul page, on n'a pas besoin des codes au-dessous
      if pa != None:
         next_ = pa.findAll("a")
         for n in next_:
            if n.text == "Next":
               follower = BeautifulSoup(self.session.get(n.attrs["href"]).content, 'html.parser')
               list_followers = follower.findAll("div",{"class":"d-table table-fixed col-12 width-full py-4 border-bottom border-gray-light"})
               for foll_ in list_followers:
                  # pour les comptes n'est pas mise à jour son Nom Prenom sur github
                  try:
                     followers_name.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                                    .find("span",{"class":"f4 link-gray-dark"}).text.lstrip())
                  except:
                     followers_name.append("Unknown")
                  # c'est évidant que le nom du compte qui exists
                  followers_acc.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                                 .find("span",{"class":"link-gray pl-1"}).text.lstrip())
                  # Comme nom du compte, bio info peut être ne pas exister        
                  try:
                     followers_bio.append(foll_.find("div",{"class":"text-gray text-small mb-2"}).find("div").text.strip())
                  except:
                     followers_bio.append("Unknown")

                  # location:
                  try:
                     followers_location.append(foll_.find("p",{"class":"text-gray text-small mb-0"}).text.strip())
                  except:
                     followers_location.append("Unknown")
      # print(followers_name)
      # print(followers_acc)
      # print(followers_bio)
      # print(followers_location)
      return followers_name, followers_acc, followers_bio, followers_location
   
   def followingScrapping(self):
      # --------------------------------------
      # Following
      params = {
         "tab": self.key_search[3]
      }  
      #it assumed that by now you are logged so we can now use .get and fetch any page of your choice
      following = BeautifulSoup(self.session.get(self.url_scrapped, params=params).content, 'html.parser')
      list_following = following.findAll("div",{"class":"d-table table-fixed col-12 width-full py-4 border-bottom border-gray-light"})
      # cherche les infos pour chaque repo:
      following_name = list()
      following_acc = list()
      following_bio = list()
      following_location = list()


      for foll_ in list_following:
         # pour les comptes n'est pas mise à jour son Nom Prenom sur github
         try:
            following_name.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                           .find("span",{"class":"f4 link-gray-dark"}).text.lstrip())
         except:
            following_name.append("Unknown")
         # c'est évidant que le nom du compte qui exists
         following_acc.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                        .find("span",{"class":"link-gray pl-1"}).text.lstrip())
         # Comme nom du compte, bio info peut être ne pas exister        
         try:
            following_bio.append(foll_.find("div",{"class":"text-gray text-small mb-2"}).find("div").text.strip())
         except:
            following_bio.append("Unknown")

         # location:
         try:
            following_location.append(foll_.find("p",{"class":"text-gray text-small mb-0"}).text.strip())
         except:
            following_location.append("Unknown")
      # ---
      # Pagination:
      pa = following.find("div",{"class":"pagination"})
      # s'il y a un seul page, on n'a pas besoin des codes au-dessous
      if pa != None:
         next_ = pa.findAll("a")
         for n in next_:
            if n.text == "Next":
               following = BeautifulSoup(self.session.get(n.attrs["href"]).content, 'html.parser')
               list_following = following.findAll("div",{"class":"d-table table-fixed col-12 width-full py-4 border-bottom border-gray-light"})
               for foll_ in list_following:
                  # pour les comptes n'est pas mise à jour son Nom Prenom sur github
                  try:
                     following_name.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                                    .find("span",{"class":"f4 link-gray-dark"}).text.lstrip())
                  except:
                     following_name.append("Unknown")
                  # c'est évidant que le nom du compte qui exists
                  following_acc.append(foll_.find("a",{"class":"d-inline-block no-underline mb-1"})\
                                 .find("span",{"class":"link-gray pl-1"}).text.lstrip())
                  # Comme nom du compte, bio info peut être ne pas exister        
                  try:
                     following_bio.append(foll_.find("div",{"class":"text-gray text-small mb-2"}).find("div").text.strip())
                  except:
                     following_bio.append("Unknown")

                  # location:
                  try:
                     following_location.append(foll_.find("p",{"class":"text-gray text-small mb-0"}).text.strip())
                  except:
                     following_location.append("Unknown")
      # print(following_name)
      # print(following_acc)
      # print(following_bio)
      # print(following_location)
      return following_name, following_acc, following_bio, following_location
   
# except HTTPError as e:
#    print(e)

if __name__ == "__main__":
   # url pour crapper
   url_scrapped = "https://github.com/nguyenkhacbaoanh"
   cp = AutoScrapping(url_scrapped)
   # print(cp.infoPerso())
   # print(cp.repoScrapping())
   # print(cp.starScrapping())
   # print(cp.followerScrapping())
   print(cp.followingScrapping())
   
