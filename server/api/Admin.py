import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use the application default credentials
cred = credentials.Certificate('./server/static/ServiceAccount.json')
firebase_admin.initialize_app(cred)



class Admin:

    def __init__(self):
        self._db = firestore.client()


    def set_homeowner_profile_picture_notification(self, email, data):
        notification = {
            "email": email,
            "notificationName": "Updating Profile Picture",
            "state": data
        }
        reference = self._db.collection(u'Homeowner ' + email).document("ProfilePicture")
        homeownerReference = reference.get()
        if homeownerReference.exists:
            reference.update(notification)
        else:
            reference.set(notification)
        
    def set_homeowner_lease_notification(self, email, data):
        notification = {
            "email": email,
            "notificationName": "Creating Lease",
            "state": data
        }
        
        print(notification)
        reference = self._db.collection(u'Homeowner ' + email).document("OntarioLease")
        homeownerReference = reference.get()
        if homeownerReference.exists:
            reference.update(notification)
        else:
            reference.set(notification)


    def set_problem_notification(self, email, data):
        notification = {
            "email": email,
            "notificationName": "Uploading Problem",
            "state": data
        }
        
        print(notification)
        reference = self._db.collection(u'Tenant Problem ' + email).document("ProblemUpload")
        homeownerReference = reference.get()
        if homeownerReference.exists:
            reference.update(notification)
        else:
            reference.set(notification)
        

    def set_tenant_profile_picture_notification(self, email, data):
            notification = {
                "email": email,
                "notificationName": "Updating Profile Picture",
                "state": data
            }
            reference = self._db.collection(u'Tenant ' + email).document("ProfilePicture")
            homeownerReference = reference.get()
            if homeownerReference.exists:
                reference.update(notification)
            else:
                reference.set(notification)