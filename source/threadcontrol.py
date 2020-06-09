import threading

class ThreadCtrl(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def printActiveThreads(self):
        m_thread = threading.active_count()
        print('number of thread objects that are active: ' + str(m_thread))
        m_thread = threading.currentThread()
        print('number of thread objects in the caller thread control: ' + str(m_thread))
        m_thread = threading.enumerate()
        print('list of all thread objects that are currently active:')
        print(m_thread)

    def startThread(self, function):
        x = self(target=function, args=(1,))
        x.start()
