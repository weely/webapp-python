#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'weely'


from tkinter import ttk
import tkinter as tk
import os, sys, subprocess, time, threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WINDOW_WIDTH, WINDOW_HEIGHT = (540, 360)
PATH = r'd:\webapp-python\www\app.py'

class MyFrame(object):

    def __init__(self, log=None):

        self.window = tk.Tk()
        self.window.title('superMonitor')
        self.window.geometry('%sx%s' % (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.resizable(0, 0)
        self.timeStr = tk.StringVar()
        self.path_str = tk.StringVar()
        self.path_str.set(PATH)
        self.__is_running__ = False
        self.createWadgets()

        self.window.mainloop()

    def createWadgets(self):
        fm_top = ttk.Frame(self.window)
        fm_top.pack(anchor='w', padx=20,pady=10,fill=tk.X)
        ttk.Label(fm_top, text=u'当前时间:').grid(row=0,column=0,rowspan=2,stick=tk.W, ipady=WINDOW_HEIGHT/40)
        self.lb_cur_time = ttk.Label(fm_top, textvariable=self.timeStr)
        self.lb_cur_time.grid(row=0, column=1, rowspan=2, stick=tk.W, ipady=WINDOW_HEIGHT/40)
        self._setTime()
        fm_content = ttk.LabelFrame(self.window)
        fm_content.pack(anchor='w', padx=20, pady=10, fill=tk.X)
        self.config_btn = ttk.Button(fm_content, text=u'重置路径', command=self._set_config).grid(row=2, column=0, ipadx=10)
        self.config_entry = ttk.Entry(fm_content, textvariable=self.path_str, width=WINDOW_WIDTH//10)
        self.config_entry.grid(row=2, column=1)

        fm_bottom = tk.Frame(self.window)
        fm_bottom.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.start_btn = ttk.Button(fm_bottom, text='start', command=self._start_watch)
        self.start_btn.grid(row=0, column=1, stick=tk.W, pady=10, padx=10)
        self.quit_btn = ttk.Button(fm_bottom, text=u'退出', command=self._quit)
        self.quit_btn.grid(row=0, column=3, stick=tk.W, pady=10, padx=10)

    def _start_thread(self, command, path, callback=None):
        self.MyThread = threading.Thread(target=start_watch, args=[command, path, callback])
        self.MyThread.setDaemon(True)
        self.MyThread.start()

    def _start_watch(self):
        if not self.__is_running__:
            path = self.path_str.get()
            if str(self.path_str):
                command = ['python', path]
                self._start_thread(command, os.path.split(path)[0])
                self.start_btn.configure(text='stop')
                self.__is_running__ = True
                self.config_entry.configure(state = 'disabled')
            else:
                print('Usage: ./pymonitor your-script.py')
        else:
            stop_watch()
            self.start_btn.configure(text='start')
            self.__is_running__ = False
            self.config_entry.configure(state='normal')

    def _set_config(self):
        self.path_str.set(PATH)

    def _setTime(self):
        self.timeStr.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.window.after(1, self._setTime)

    def _quit(self):
        try:
            stop_watch()
        except:
            pass
        finally:
            self.window.quit()
            self.window.destroy()
            exit()

def log(s):
    print('[Monitor] %s' % s)

class MyFileSystemEventHandler(FileSystemEventHandler):

    def __init__(self, fn):
        super(MyFileSystemEventHandler, self).__init__()
        self.restart = fn

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: %s' % event.src_path)
            self.restart()

command = ['echo', 'ok']
process = None
observer = None

def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with code %s.' % process.returncode)

def start_process():
    global process, command
    log('Start process %s...' % ''.join(command))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

def restart_process():
    kill_process()
    start_process()

def start_watch(comm, path, callback):
    global command, observer
    if comm:
        command = comm
    observer = Observer()
    observer.schedule(MyFileSystemEventHandler(restart_process), path, recursive=True)
    observer.start()
    log('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def stop_watch():
    global observer
    kill_process()
    observer.stop()
    log('stop watch')

if __name__ == '__main__':
    myframe = MyFrame()
