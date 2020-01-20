# Export Plot Over Line filter data from Paraview to CSV

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

print("Running exportParaviewCsv.py ...")

# Iterations to export
it = [20, 40, 60, 100]

# Views (= spreadsheet) to export
view = ['SpreadSheetView1', 'SpreadSheetView2', 'SpreadSheetView3']
# Corresponding to each view namely : view1 - view 2 - view3
nameView = ['EULER', 'RK2', 'RK4']

# Path to save exported files
path = '/some/path/'

for i in range(len(it)):
	# get animation scene
	animationScene1 = GetAnimationScene()

	# get the time-keeper
	timeKeeper1 = GetTimeKeeper()

	# Properties modified on animationScene1
	animationScene1.AnimationTime = it[i]

	# Properties modified on timeKeeper1
	timeKeeper1.Time = it[i]

	for vi in range(len(view)):
		# find view
		spreadSheetView1 = FindViewOrCreate(view[vi], viewtype='SpreadSheetView')

		# set active view
		SetActiveView(spreadSheetView1)

		# export view
		file = path + 'NAME_' + nameView[vi] + '_it' + str(it[i]) + '.csv'
		ExportView(file, view=spreadSheetView1)

	# Work status
	ws = int((i+1)/len(it) * 100)
	print("Work status " + str(ws) + "%")

print("Work done")