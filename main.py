from flask_restful import Resource
from threading import Thread
import requests
from flask import Flask, request
from flask_mail import Mail , Message
from flask_restful import Api
from datetime import date

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT']= '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] =True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_DEFAULT_SENDER'] = ''
app.config['MAIL_PASSWORD'] = ''
# app.config['MAIL_DEFAULT_SENDER']
#app.config['MAIL_USE_TLS']
# app.config['MAIL_MAX_EMAILS']
# app.config['MAIL_SUPPRESS_SEND']
# app.config['MAIL_AS']

api = Api(app)
mail = Mail(app)
class SendMail(Resource):
    def get(self):
        try:
            response = {}
            agent_name = request.args['name']
            customer_mail = request.args['mail']
            mess_date = date.today()
            message_temp = "<body>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>Greetings!</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>We would be delighted to know your thoughts about\
      your recent interaction with our contact centre,\
      and the service {}\
      from our team provided on {}\
      </span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>We\
      value your feedback and will appreciate you\
      taking a minute to complete this short survey.\
      Your responses and feedback will certainly help\
      us improve our services.</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>To\
      obtain the survey link, please click\
      </span><span style='color:rgb(5,99,193);text-decoration:underline'><a href='https://bit.ly/3haq1vl' target='_blank' data-saferedirecturl='https://www.google.com/url?q=https://bit.ly/3haq1vl&amp;source=gmail&amp;ust=1625808873446000&amp;usg=AFQjCNFAWLg9xFg6oC4YZhd5OUfJ9KF-mw'>here</a></span><span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>.</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>Alternatively,\
      you can also click the link below to access the\
      survey:</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt 36pt;font-size:11pt;font-family:Calibri,sans-serif;margin-left:162.0pt'>\
      <span style='font-size:10.0pt;font-family:Symbol'><span>·<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
      </span></span></span><span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'><a href='https://www.research.net/r/acercustomerexperience' target='_blank' data-saferedirecturl='https://www.google.com/url?q=https://www.research.net/r/acercustomerexperience&amp;source=gmail&amp;ust=1625808873446000&amp;usg=AFQjCNGPnfA9j3siOk41_aMnyWV67wVxYQ'>\https://www.research.net/r/<wbr>\acercustomerexperience</a>\</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif'>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif'>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif'>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>\
   Thankyou for taking part in our survey,</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>The\
      Acer Customer Experience Team</span>\
   </p>\
   <p style='margin-top:0px;margin-bottom:0px;margin-top:0px;margin-bottom:0px;margin:0cm 0cm 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif>\
      <span style='font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;'>&nbsp;</span>\
   </p>\
   </body>".format(agent_name,mess_date)







            msg = Message('Tell us about your recent experience with interation with our company', recipients=[customer_mail])
            msg.html = message_temp
            mail.send(msg)
            response['status'] = 'SUCCESS'
            return response
        except Exception as e:
             response['status'] = 'FAILURE'
             return response

api.add_resource(SendMail, '/sendmail')
if __name__ == '__main__':
    app.run(port=5002,debug=True)
