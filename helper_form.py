import requests

class AUTH :
      @staticmethod
      def init(username,username) : return { 'auth' : (username, password)
                                             , 'verify' : False}
      @staticmethod
      def get(**kwargs) : 
          url = 'url'
          url = kwargs.pop(url,url)
          auth = 'auth'
          auth = kwargs.pop(auth,auth)
          verify = 'verify'
          verify = kwargs.pop(verify,verify)
          return requests.get(url, auth=auth, verify=verify)
          return requests.get(url, auth=auth, params=params, verify=verify,headers=headers)
      @staticmethod
      def post(**kwargs) : 
          url = 'url'
          url = kwargs.pop(url,url)
          auth = 'auth'
          auth = kwargs.pop(auth,auth)
          verify = 'verify'
          verify = kwargs.pop(verify,verify)
          data = 'data'
          data = kwargs.pop(data,data)
          return requests.post(url,auth=auth,data=data,verify=verify)
          return requests.post(url,auth=auth,data=data,verify=verify,headers=headers)
      @staticmethod
      def transform(response) : 
          return BeautifulSoup(response.text)
      @staticmethod
      def parseTextArea(page) : 
          return page.find('textarea', id="text").string
      @staticmethod
      def parse1(page) : 
          tag = page.find('input', attrs = {'name':'version'})
          ver = tag['value']

if __name__ == "__main__" :
   url = "http://www.someurl.com"
   username = "your_username"
   password = "your_password"
   params = AUTH.init(username, password)
   params['url'] = url
   response = AUTH.get(**params)
   text = AUTH.transform(response)
   page = AUTH.parseTextArea(text)
   page = AUTH.parse1(page)

   params = AUTH.init(username, password)
   params['url'] = url
   params['data'] = { 'save' : 'Submit changes'
                    , 'text' : "Your text here, this will be what is written to the textarea for the post"
                    } 

   response = AUTH.post(**params)
