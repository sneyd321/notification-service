from flask import Flask, request, Response, jsonify
from . import notify
from server.api.Admin import Admin
from server.api.RequestManager import Zookeeper, RequestManager


zookeeper = Zookeeper()
admin = Admin()




@notify.route("/Homeowner/<int:homeownerId>/Profile", methods=["POST"])
def create_notificaiton(homeownerId):
    homeownerService = zookeeper.get_service("homeowner-service")
    if homeownerService:
        manager = RequestManager(request, homeownerService)
        homeownerData = manager.get("homeowner/v1/Homeowner/" + str(homeownerId))
        print(homeownerData)

    if not homeownerData:
        return Response(status=400)
  
    data = request.get_json()
    if not data or "state" not in data:
        return Response(status=400)

    admin.set_homeowner_profile_picture_notification(homeownerData["email"], data["state"])
    return Response(status=200)

@notify.route("/Homeowner/<int:homeownerId>/Lease/Ontario", methods=["POST"])
def create_lease_notification(homeownerId):
    homeownerService = zookeeper.get_service("homeowner-service")
    if homeownerService:
        manager = RequestManager(request, homeownerService)
        homeownerData = manager.get("homeowner/v1/Homeowner/" + str(homeownerId))
    if not homeownerData:
        return Response(status=400)

    data = request.get_json()
    if not data or "state" not in data:
        return Response(status=400)
    print(data)
    
    admin.set_homeowner_lease_notification(homeownerData["email"], data["state"])
    return Response(status=200)


@notify.route("/Problem/<int:problemId>", methods=["POST"])
def create_problem_notificaiton(problemId):
 
    data = request.get_json()
    if not data or "state" not in data:
        return Response(status=400)

    admin.set_problem_notification(str(problemId), data["state"])
    return Response(status=200)


@notify.route("/Tenant/<int:tenantId>/Profile", methods=["POST"])
def create_tenant_notificaiton(tenantId):
    tenantService = zookeeper.get_service("tenant-service")
    if tenantService:
        manager = RequestManager(request, tenantService)
        tenantData = manager.get("tenant/v1/Tenant/" + str(tenantId))
        print(tenantData)

    if not tenantData:
        return Response(status=400)
  
    data = request.get_json()
    if not data or "state" not in data:
        return Response(status=400)

    admin.set_tenant_profile_picture_notification(tenantData["email"], data["state"])
    return Response(status=200)