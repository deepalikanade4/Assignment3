from django.shortcuts import render
from rest_framework.parsers import JSONParser  
from rest_framework.renderers import JSONRenderer
import io
from .serializers import UserDataSerializer
from .models import UserData
from django.http import HttpResponse, JsonResponse  # used to generate json response for frontend application
from django.views.decorators.csrf import csrf_exempt        # for csrf protection for update ,delete and create user

#   function works for get method for retrive user data
def retrive_user(request):

    if request.method=='GET':
        json_data=request.body                                          
        stream=io.BytesIO(json_data)
        User_pyData=JSONParser().parse(stream)                          #converting json data to python data structure 
        id=User_pyData.get('id',None)
        if id is not None:
            try:
                Userd=UserData.objects.get(id=id)                        # get single user object data from model
                User_serialize_data=UserDataSerializer(Userd)           # converting complex data to native python data type
            except UserData.DoesNotExist:                                 #handling error if id is not present in db
                msg_response={'msg':'User Not exist'}
                return JsonResponse(msg_response,safe=False)
            
            return JsonResponse(User_serialize_data.data,safe=False)       #sending response to request by converting python data to json 
           
        msg_response={'msg':'Enterd id is invalid'}
        return JsonResponse(msg_response,safe=False)
           

#   function works for post method for create user data

@csrf_exempt                                      # decorator for csrf protection
def create_user(request):
    if request.method =='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        User_pyData=JSONParser().parse(stream)
        User_serialize_data=UserDataSerializer(data=User_pyData)
        if User_serialize_data.is_valid():
            User_serialize_data.save()
            msg_response={'msg':"user Data Created"}
            return JsonResponse(msg_response,safe=True)
            

        json_data=JSONRenderer().render(User_serialize_data.errors)
        return HttpResponse(json_data,content_type='application/json')

#   function works for put method for update user data
@csrf_exempt   
def update_userdata(request):
    if request.method == 'PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        User_py_data=JSONParser().parse(stream)
        try:
            id=User_py_data.get('id')
            userd=UserData.objects.get(id=id)
        except UserData.DoesNotExist:                                 #handling error if id is not present in db
                msg_response={'msg':'User Not exist You trying to update'}
                return JsonResponse(msg_response,safe=False)
            

        # partial is set to true so put and patch both can work 
        User_serialize_data=UserDataSerializer(userd,data=User_py_data ,partial=True)
        if User_serialize_data.is_valid():                    #if data in put request  is valid save to db               
            User_serialize_data.save()
            msg_response={'msg':"Data updated"}
            return JsonResponse(msg_response,safe=False) 

        
        json_data=JSONRenderer().render(User_serialize_data.errors)             #converting python data to json format 
        return HttpResponse(json_data,content_type='application/json')

#   function works for delete method for delete user data
@csrf_exempt
def delete_user(request):
    if request.method== 'DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        User_py_data=JSONParser().parse(stream)
        try:
            id=User_py_data.get('id')
            UserData.objects.get(id=id).delete()                         #delete record  from database of given id
        except UserData.DoesNotExist:                                    #handling error if id is not present in db
                msg_response={'msg':'User Not exist which you Trying to delete'}
                return JsonResponse(msg_response,safe=False)
            

        msg_response={'msg':'User Deleted '}
        return JsonResponse(msg_response,safe=False) 

