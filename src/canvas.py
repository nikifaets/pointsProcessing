import vtk

def createSphere(x,y,z):

    colors = vtk.vtkNamedColors()
    # Create a sphere
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(x, y, z)
    sphereSource.SetRadius(2.0)

    # Make the surface smooth.
    #sphereSource.SetPhiResolution(2)
    #sphereSource.SetThetaResolution(2)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d("Cornsilk"))
    colors = vtk.vtkNamedColors()

    return actor

def createScene():

    colors = vtk.vtkNamedColors()

    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Sphere")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
        
    renderer.SetBackground(colors.GetColor3d("DarkGreen"))

    
    return renderWindowInteractor

def addSpheres(renderWindow, pointsList):

    
    renderer = vtk.vtkRenderer()
    for p in pointsList:

        sphere = createSphere(p.X, p.Y, p.Z)
        renderer.AddActor(sphere)

    renderWindow.Render()
    renderWindow.Start()

