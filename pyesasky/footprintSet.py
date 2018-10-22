
__all__ = ['FootprintSet']


class FootprintSet:
    
    _footprintSetName = ''
    _cooframe = 'J2000'
    _color = '#aa2345'
    _lineWidth = 10
    _footprints = []
    
    
    
    def __init__(self, footprintSetName, cooframe, color, lineWidth):
        self._footprintSetName = footprintSetName        
        
        if (cooframe == 'J2000' or cooframe == 'Galactic'): 
            self._cooframe = cooframe
        else:
            print('coordinates frame ' + cooframe + ' not recognized. Possible options are J2000 and Galactic. Applied J2000 by default.')
        
        if color:
            self._color = color
        
        self._lineWidth = lineWidth
        
    def addFootprint(self, name, stcs, id):
        currFootprint = {}
        #currFootprint['data'] = {}
        currFootprint['name'] = name
        if not id:
            currFootprint['id'] = len(self._footprints)
        else:
            currFootprint['id'] = int(id)
        currFootprint['stcs'] = stcs
        self._footprints.append(currFootprint)
        
    def toDict(self):
        
        # content = dict(
        #     footprintsSet=dict(
        #         overlayName=self._footprintSetName,
        #         cooframe=self._cooframe,
        #         color=self._color,
        #         lineWidth=self._lineWidth
        #     )
        # )

        content = dict(
            footprintsSet=dict(
                overlayName=self._footprintSetName,
                cooframe=self._cooframe,
                color=self._color,
                lineWidth=self._lineWidth,
                footprints=self._footprints
            )
        )
        return content