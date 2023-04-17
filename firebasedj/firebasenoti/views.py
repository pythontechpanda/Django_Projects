# from django.shortcuts import render
# import pyrebase
# from fcm_django.models import FCMDevice

# config={
#   'apiKey': "AIzaSyCsnGmmp9lpsOFsV9DoM_XT44w45jZExjY",
#   'authDomain': "coin-club-app.firebaseapp.com",
#   'databaseURL': "https://coin-club-app-default-rtdb.firebaseio.com",
#   'projectId': "coin-club-app",
#   'storageBucket': "coin-club-app.appspot.com",
#   'messagingSenderId': "851701297823",
#   'appId': "1:851701297823:web:c7157e9872d86a7d1728aa",
#   'measurementId': "G-9GKDQF5LSG"
# }
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()
# # device = FCMDevice.objects.get(id=12).first()

# def home(request):
# 	day = database.child('clubName').child('roundName').child('7999717423').child('name').get().val()
# 	id = database.child('clubName').child('roundName').child('7999717423').child('Id').get().val()
# 	return render(request,"index.html",{"day":day,"id":id})
# from pyfcm import FCMNotification
# # from baseapi import BaseAPI

# push_service = FCMNotification(api_key="AIzaSyCsnGmmp9lpsOFsV9DoM_XT44w45jZExjY")

# registration_id = "e6ITgdMFT3u27Uh7PDqnmf:APA91bHmuDYCNaP3WqDbWstxqtfqaZFEPjojPr5ZOPUyFE5oOn8CBB1TRxkRhNnE8vs5bf5yS2fu-HcpwJTIRtjuf5fwowNOLSdKiurQX0Q83h_9eIahrVzVVPMQ5J3GJ0UTF8B_d_pQ"
# message_title = "Uber update"
# message_body = "Hi john, your customized news for today is ready"
# result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
# print( result)
#   # device.send_message("Title", "Message")
#   # device.send_message(data={"test": "test"})
#   # device.send_message(title="Title", body="Message", data={"test": "test"})
# 	# projectname = database.child('Data').child('Projectname').get().val()


from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials, messaging

def send_notification(request):

    tokens = ['dmF413fbSM-P_pioqEXcuC:APA91bH6W30powUHJ6RGE4Vu1RgXAxG_X9lNBdfcV7T791CX2LunEDOvIetfNqKatDFJaedbAyCUBombiXk7bCMxZ0xIlESOOzjVkkBZMnyvisFrxhO5_g1_udvWh6Mtw7AdRt97Ir_4']
    # Create a message
    message = messaging.MulticastMessage(
        
        notification=messaging.Notification(
            title='Club Invitation',
            body='This is a Notification to Join Techpanda Club.'
        ),
        data={
            'invite': 'Yes',
            'clubname': 'Techpanda',
            'totalamount': '20000',
            'totalmember': '10',
            'perhead': '2000',
        },
        tokens=tokens,
    )
    # Send the message
    response = messaging.send_multicast(message)
    print(response.success_count)
    # Render the response
    return render(request, 'index.html', {'response': response.success_count})