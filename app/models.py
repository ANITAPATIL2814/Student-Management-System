from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # we use this becz it show object1,2 like that we print their name
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    def __str__(self): # we use this becz it show object1,2 like that we print their name
        return self.session_start + " TO " + self.session_end

class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE) #on_delete is used for when we delete student  then that stdudent also delete from customuser 
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING) #we created couse already when we delete course from student model it is not going to delete from course model
    session_year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # we use this becz it show object1,2 like that we print their name
        return self.admin.first_name + " " +self.admin.last_name
    

class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE) #on_delete is used for when we delete student  then that stdudent also delete from customuser 
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): # we use this becz it show object1,2 like that we print their name
        return self.admin.username 
    
class Sub(models.Model):
    name = models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE) #we created couse already when we delete course from student model it is not going to delete from course model
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE) #we created couse already when we delete course from student model it is not going to delete from course model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): # we use this becz it show object1,2 like that we print their name
        return self.name
    

#staff

class Staff_Notification(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)
    def __str__(self): # we use this becz it show object1,2 like that we print their name
        return self.staff_id.admin.first_name
    
class Staff_leave(models.Model): 
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE ) #if staff delete then their leave will become automatically removed
    data=models.CharField(max_length=100)
    message=models.TextField()
    status=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name
    
class Staff_Feedback(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE ) #if staff delete then their feedback will become automatically removed
    feedback=models.TextField()
    status=models.IntegerField(default=0)
    feedback_replay=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.staff_id.admin.first_name +" " + self.staff_id.admin.last_name
    
#student
class Student_Notification(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)
    def __str__(self): # we use this becz it show object1,2 like that we print their name
        return self.student_id.admin.first_name

class Student_Feedback(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback=models.TextField()
    status=models.IntegerField(default=0)
    feedback_replay=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_id.admin.first_name +" " + self.student_id.admin.last_name
      
class Student_leave(models.Model): 
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return self.student_id.admin.first_name +" " + self.student_id.admin.last_name
    
class Attendance(models.Model):
    subject_id = models.ForeignKey(Sub,on_delete=models.DO_NOTHING) #
    attendance_data = models.DateField()
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject_id.name
    
class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING) 
    attendace_id = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student_id.admin.first_name

class StudentResult(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id= models.ForeignKey(Sub,on_delete=models.CASCADE)
    assignment_mark = models.IntegerField()
    exam_mark =  models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject_id.admin.first_name