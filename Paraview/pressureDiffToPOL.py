#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
collectionParaviewpvd = FindSource('collectionParaview.pvd')

# create a new 'Probe Location'
probe = ProbeLocation(Input=collectionParaviewpvd,
    ProbeType='Fixed Radius Point Source')

# Properties modified on probeLocation1.ProbeType
probe.ProbeType.Center = [0.115, 0.0, 0.0]

# Properties modified on probeLocation1
probe.Tolerance = 2.22044604925031e-16

# Properties modified on probeLocation1.ProbeType
probe.ProbeType.Center = [0.115, 0.0, 0.0]

# extract pressure at probe at used time step...
probePoint = paraview.servermanager.Fetch(probe)
valueProbe = probePoint.GetPointData().GetArray('F0_Pressure_SG_waterIncomp').GetValue(0)


# create a new 'Calculator'
calculator = Calculator(Input=collectionParaviewpvd)
calculator.Function = ''
calculator.AttributeMode = 'Cell Data'

# Properties modified on calculator
calculator_exp = 'F0_Pressure_SG_waterIncomp - {}'.format(valueProbe)
calculator.ResultArrayName = 'P(r)-P(rInt)'
calculator.Function = calculator_exp

# Create new layout for the 'SpreadSheetViewCalc' and 'Line Chart View'
CreateLayout('DP')

# create a new 'Plot Over Line'
plotOverLineDP = PlotOverLine(Input=calculator,
    Source='High Resolution Line Source')
# Properties modified on plotOverLineDP.Source
plotOverLineDP.Source.Point1 = [0.0, 0.0, 0.0]
plotOverLineDP.Source.Point2 = [0.5, 0.0, 0.0]
plotOverLineDP.Tolerance = 2.22044604925031e-16

# Create a new 'Line Chart View'
lineChartViewDP = CreateView('XYChartView')
lineChartViewDP.ViewSize = [245, 197]
lineChartViewDP.LeftAxisRangeMaximum = 6.66
lineChartViewDP.BottomAxisRangeMaximum = 6.66
lineChartViewDP.RightAxisRangeMaximum = 6.66
lineChartViewDP.TopAxisRangeMaximum = 6.66
lineChartViewDP.ChartTitle = 'Time step ${TIME}'

# get layout
layout2 = GetLayout()

# place view in the layout
layout2.AssignView(0, lineChartViewDP)

# show data in view
plotOverLine2Display_1 = Show(plotOverLineDP, lineChartViewDP)
plotOverLine2Display_1.CompositeDataSetIndex = [0]
plotOverLine2Display_1.UseIndexForXAxis = 0
plotOverLine2Display_1.XArrayName = 'arc_length'
plotOverLine2Display_1.SeriesVisibility = ['P(r)-P(rInt)']
plotOverLine2Display_1.SeriesLabel = ['P(r)-P(rInt)']
plotOverLine2Display_1.SeriesColor = ['P(r)-P(rInt)', '1']
plotOverLine2Display_1.SeriesPlotCorner = ['P(r)-P(rInt)','0']
plotOverLine2Display_1.SeriesLabelPrefix = ''
plotOverLine2Display_1.SeriesLineStyle = ['P(r)-P(rInt)', '1']
plotOverLine2Display_1.SeriesLineThickness = ['P(r)-P(rInt)', '2']
plotOverLine2Display_1.SeriesMarkerStyle = ['P(r)-P(rInt)', '0']

layout2.SplitVertical(0, 0.5)

# show data in view
spreadSheetView1 = FindViewOrCreate('SpreadSheetView1', viewtype='SpreadSheetView')
layout2.AssignView(1, spreadSheetView1)
calculator1Display = Show(calculator, spreadSheetView1)
calculator1Display.FieldAssociation = 'Cell Data'
spreadSheetView1.Update()
