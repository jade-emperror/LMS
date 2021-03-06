from django.shortcuts import render
import pymysql
import hashlib 

# Create your views here.
def makedbcon():
    conn = pymysql.connect(
                        host='localhost',
                        port=3306,
                        user='root',
                        password='jade123',
                        db='lms_db',
                       )
    return conn
def getMD5Hash(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

def closecon(cur,conn):
    cur.close()
    conn.close()
def login(request):
    user=request.POST['user_id'].upper()
    pwd=getMD5Hash(request.POST.get('password'))
    conn=makedbcon()
    cur=conn.cursor()
    print(user)
    try:
        if(user[:2]=='VH'):
            q='select user_id,password from student where user_id = \'%s\''%user
            print(q)
            if(cur.execute(q)):
                for i in cur:
                    if(pwd == i[1]):
                        closecon(cur,conn)
                        return render(request,'login.html',{"data":"yes"})
                closecon(cur,conn)
                return render(request,'login.html',{"data":"Incorect User name or password"})
        elif(user[:3]=='HTS'):
            q='select user_id,password from teacher where user_id = \'%s\''%user
            print(q)
            if(cur.execute(q)):
                for i in cur:
                    if(pwd == i[1]):
                        closecon(cur,conn)
                        return render(request,'login.html',{"data":"yes"})
                closecon(cur,conn)
                return render(request,'login.html',{"data":"Incorect User name or password"})
    except Exception as e:
        print(str(e))

    return render(request,'login.html',{"data":user+pwd})