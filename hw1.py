import turtle
tao=turtle.Pen()
tao.shape('turtle')
for i in range(8):
    tao.fd(50);tao.dot(20,"red");tao.left(45);tao.fd(50)

tao.left(-45)
for i in range(8):
    tao.fd(50);tao.dot(20,"red");tao.left(-45);tao.fd(50)

tao.left(90)
for i in range(8):
    tao.fd(50);tao.dot(20,"red");tao.left(-45);tao.fd(50)

tao.dene()
