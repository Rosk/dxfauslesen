import Tkinter, tkFileDialog, dxfgrabber

__author__ = 'brillo,rosk'

if __name__ == '__main__':

    root = Tkinter.Tk()
    root.withdraw()
    file = tkFileDialog.askopenfilename(filetypes=[("DXF Dateien","*.dxf"),("All files","*")], title="DXF Datei waehlen",parent=root)
    dxf = dxfgrabber.readfile(file)

    print "----------------------------------------"
    print("DXF Version: {}".format(dxf.dxfversion))
    print "----------------------------------------"

    # jetzt alle Linien,Arcs,Circles und Polylines herausholen

    all_lines = [entity for entity in dxf.entities if entity.dxftype == 'LINE']
    all_arcs = [entity for entity in dxf.entities if entity.dxftype == 'ARC']
    all_circles = [entity for entity in dxf.entities if entity.dxftype == 'CIRCLE']
    all_polylines = [entity for entity in dxf.entities if entity.dxftype == 'POLYLINE']

    all_everything = [entity for entity in dxf.entities]

    layer_count = len(dxf.layers)  # collection of layer definitions
    all_layer_0_entities = [entity for entity in dxf.entities if entity.layer == '0']
    all_layer_1_entities = [entity for entity in dxf.entities if entity.layer == '1']


    print "Anzahl Lines: ", all_lines
    print "Anzahl Arcs: ", all_arcs
    print "Anzahl Circles: ", all_circles

    print "Alle enthaltenen Objekte in der Datei: ", all_everything

    print "Anzahl der Polylineelemente auf Layer 0: ", all_polylines[0].__len__()
    print "Anzahl der Polylineelemente auf Layer 1: ", all_polylines[1].__len__()

    print "Anzahl der Layer: ", layer_count
    print "Anzahl der Elemente auf Layer 0: ", all_layer_0_entities
    print "Anzahl der Elemente auf Layer 1: ", all_layer_1_entities
