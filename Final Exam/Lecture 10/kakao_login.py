from http.server import HTTPServer, BaseHTTPRequestHandler
# from os import access
from socketserver import BaseRequestHandler
from urllib import parse, request
import requests, json
import cv2

REST_API_KEY = "fd7dba8acafaa23e997bc055ba31530f"

class http_handler(BaseRequestHandler):
   def do_GET(self):
      self.route()
   def route(self):
      parsed_path = parse.urlparse(self.path)
      real_path = parsed_path.path
      if real_path == "/":
         self.send_html()
      elif real_path == "/oauth":
         self.process_oauth()
      else:
         self.response(404,"<h1>Not Found</h1>")
      
   def send_html(self): #real_path의 값이 / 인경우 send_html 함수가 호출된다.
      self.send_response(200)
      self.end_headers()
      with open("./index_kakao.html", "r", encoding='utf-8') as f:
         msg = f.read()
         self.wfile.write(msg.encode())

   def process_oauth(self): #real_path의 값이 /oauth인 경우 process_oauth함수가 호출된다.  (POST 방식 : 사용자 토큰을 받는 부분)
      parsed_path = parse.urlparse(self.path)
      query = parsed_path.query #query 부분만 따로 떼서 가져오기 
      parsed_query = parse.parse_qs(query) #쿼리를 딕셔너리 형태로 바꿔주는 함수 parse_ps
      authorize_code = parsed_query['code'] #key값이 code인 value 값을 authorize_code로 저장 
      print("authorize code is " ,authorize_code)
      self.response(200, "Kakao authorization is successful") #성공적으로 인증이 완료되면 상태코드 200과 함께 메세지 출력 

      token_api_url = "https://kauth.kakao.com/oauth/token" #token을 받는 서버 api_url 
      data = {'Grant_type' : "authorization_code", #api 문서에 정의된 파라미터들을 알맞은 타입으로 전달 + 딕셔너리 형태로 전달 
               'client_id' : REST_API_KEY,
               'redirect_uri' : 'http://localhost:9999/oauth',
               'code': authorize_code,
               'client_secret': "02kUyjfBaT6rKV6YLJ44SeHXJwZ4lId0"}
      
      rsp = requests.post(token_api_url,data = data)
      rsp_json = json.loads(rsp.text)
      access_token = rsp_json['access_token']
      refresh_token = rsp_json['refresh_token']
      print("access token : ", access_token)
      print("refresh token : ", refresh_token)

      profile_url = 'https://kapi.kakao.com/v1/api/talk/profile' #카카오 서버에서 프로필을 가지고 오는 url
      header = {"Authorization" : "Bearer "+ access_token } #미리 정의된 header 형식대로 맞춰서 정의 
      rsp = requests.get(profile_url, headers=header)

      json_profile = rsp.json() #json형식을 dictionary 형식으로 변경
      print(json_profile)

      image_path = 'profile.jpg'
      request.urlretrieve(json_profile['profileImageURL'], image_path)

      #프로필 사진 띄우는 건 패쓰

      talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
      header = {"Authorization" : "Bearer " + access_token} 
      

      msg = {'object_type' : "text", 
            'text' : "안녕 지민~",
            'link' : 
            {
               "web_url" : "https://labs.sch.ac.kr/department/bigdata/m",
               "mobile_url" : "https://labs.sch.ac.kr/department/iot/m"

            } #링크 없으면 어쩌지?
      }
      template_object_json = json.dumps(msg)
      data = {'template_object' : template_object_json}
      rsp = requests.post(talk_url,headers=header,data=data)

   
   def response(self, status_code, body):
      self.send_response(status_code)
      self.send_header('Content-type', 'text/plain; charset = utf-8')
      self.end_headers()
      self.wfile.write(body.encode())


httpd = HTTPServer(('localhost', 9999), http_handler)
print("Serving HTTP on {} : {}".format('localhost', 9999))
httpd.serve_forever() 


