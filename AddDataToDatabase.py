import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-ba666-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "56567":
        {
            "name": "Robert Downey JR",
            "major": "Artificial Intelligence",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2024-04-13 00:54:34"
        },
    "56568":
        {
            "name": "Benedict Cumberbatch",
            "major": "Surgeon",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "A",
            "year": 5,
            "last_attendance_time": "2023-04-13 00:54:34"
        },
    "56569":
        {
            "name": "Jennifer Lawrence",
            "major": "Drama",
            "starting_year": 2019,
            "standing": "C",
            "total_attendance": 11,
            "year": 3,
            "last_attendance_time": "2023-04-13 00:54:34"
        },
    "56571":
        {
            "name": "Shreyash Sinha",
            "major": "Computer Science",
            "starting_year": 2019,
            "total_attendance": 26,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2023-03-13 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
