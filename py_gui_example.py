# -*- coding: utf-8 -*-

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WXAgg')

import wx

class WxMatplotlibPanel(wx.Panel):
    
    def __init__(self, parent):

        from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
        from matplotlib.figure import Figure

        self.parent = parent
        wx.Panel.__init__(self, parent)

        self.figure = Figure(None)
        self.figure.set_facecolor((0.7, 0.7, 1.))
        self.subplot = self.figure.add_subplot(111)
        
        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.canvas.SetBackgroundColour(wx.Colour(100, 255, 255))

        self._SetSize()
        self.draw()
    
    def _SetSize(self):

        size = tuple(self.parent.GetClientSize())
        self.SetSize(size)
        self.canvas.SetSize(size)
        self.figure.set_size_inches(float(size[0])/self.figure.get_dpi(),
                float(size[1])/self.figure.get_dpi())

    def draw(self):
        from mpl_toolkits.mplot3d import Axes3D
        import numpy as np

        x = np.arange(-3, 3, 0.25)
        y = np.arange(-3, 3, 0.25)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(X) + np.cos(Y)

        ax = Axes3D(self.figure)
        #ax.plot_wireframe(X, Y, Z)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1)


application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, u"Editor",size=(640, 480), pos=(100, 100))
frame.CreateStatusBar()
frame.SetStatusText("application is ready.")

panel = WxMatplotlibPanel(frame)
frame.Show()

application.MainLoop()

