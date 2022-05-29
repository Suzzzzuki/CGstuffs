from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D_anime_template")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    glutMainLoop()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    #Sun
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(1, 20, 20)
    glPopMatrix()

    #mercury
    glPushMatrix()
    glRotatef(angle*(365/88), 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 2.0)
    glColor3f(0.8, 0.8, 0.8)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

    #venus
    glPushMatrix()
    glRotatef(angle*(365/225), 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 4.0)
    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(0.15, 20, 20)
    glPopMatrix()

    #earth
    glPushMatrix()
    glRotatef(angle, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 6.0)
    glColor3f(0.0, 0.0, 1.0)
    glutSolidSphere(0.2, 20, 20)

    #moon
    glRotatef(angle*(365/27), 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 0.5)
    glColor3f(0.7, 0.7, 0.7)
    glutSolidSphere(0.05, 20, 20)
    glPopMatrix()

    #mars
    glPushMatrix()
    glRotatef(angle*(365/687), 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 8.0)
    glColor3f(1.0, 0.3, 0.0)
    glutSolidSphere(0.19, 20, 20)
    glPopMatrix()
    
    glutSwapBuffers()
    
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def idle():
    global angle
    angle += 1 #speed

    glutPostRedisplay()

if __name__ == "__main__":
    main()