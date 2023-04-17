from django_cron import CronJobBase, Schedule
# from fcm_django.models import FCMDevice
# from fcm_django import fcm_send_bulk_message
# from fcm_django.api.fcm import fcm_send_bulk_message
from firebase_admin import credentials, messaging
from django.shortcuts import render,redirect,HttpResponse

class SendPushNotifications(CronJobBase):
    RUN_EVERY_MINS = 1  # send push notifications every minute
        
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'firebasenoti.send_push_notifications'  # a unique code for this cron job


    def do(self):
        # userid = user_registration.objects.get(id=id)
        # clubid = club.objects.get(id=uid)
        tokens = ['c9e3uj9BTUya6lwdYJlWhH:APA91bHXwBU8mfxzx-QOw-NM6R2rKvelGAOeVJc6UdAf2WqO89s138iDT8-mxrCoK4PV1j211jIagr0tVf06tA970IAAMHyqpht0T004FDKmNdLBdteerTWLmS4uYXi39H7yhwTwTv1x']
        # Create a message
        message = messaging.MulticastMessage(
            
            notification=messaging.Notification(
                title='Club Invitation',
                body=f'Hello !\n You are invited to join Club.',
                image= 'https://meetjob.techpanda.art/media/club/NicePng_chilli-png_6961635.png'
            ),
            # data={
            #     # 'invite': 'Yes',
            #     # 'userid': str(userid.id),
            #     # 'clubid': str(clubid.id),
            #     # 'clubname': str(clubid.clubname),
            #     # 'totalmember': str(clubid.clubmembers),
            #     # 'totalamount': str(clubid.clubamount),
            #     # 'perhead' : str(clubid.clubcontribution),
                
                
            # },
            
            tokens=tokens,
        )
        # Send the message
        response = messaging.send_multicast(message)
        
        print(response)
        

        # # get all FCM devices
        # devices = FCMDevice.objects.all()
        
        # print("ffffcccccmmmmmmmmm"+devices)

        # # create the push notification message
        # message = {
        #     'title': 'Hello, World!',
        #     'body': 'This is a test push notification from my Django app.',
        #     'icon': 'myapp-icon.png',
        # }

        # # send the message to all devices
        # response = fcm_send_bulk_message(devices=devices, data=message)
        # print(response)
        
        
        