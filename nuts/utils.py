import pyfirmata
from utils.general import LOGGER

class JetController:
    Board = False
    
    def __init__(self) -> None:
        try:
            self.Board = pyfirmata.Arduino('/dev/ttyACM0')
        except:
            LOGGER.error(f"There was an error connecting to the Arduino")

    def TurnOnJet(self, index):
        try:
            self.Board.digital[index].write(1)
        except Exception:
            LOGGER.error(f"There was an error turning on jet {index}")
    
    def TurnOffJet(self, index):
        try:
            self.Board.digital[index].write(0)
        except Exception:
            LOGGER.error(f"There was an error turning on jet {index}")

class ConfidenceValues:
    def __init__(self, good, bad) -> None:
        self.Good = good
        self.Bad = bad

    def __str__(self) -> str:
        return f"Good: {self.Good}, Bad: {self.Bad}"
    

def GetJetIndex(xpos, colAlign):
    # Returns the index of the jet in who's path the nut falls.

    #Parameters:
    #    xpos (int): The xpos of the centre of the nut.
    #    colAlign (array (int)): An array of xpos of the end of columns. This should exclude the final column i.e if there are 13 columns, send 12.

    #Returns:
    #    colIndex (int): The index of the column in which the nut falls.   


    larger_cols = [colItem for colItem in colAlign if colItem >= xpos] # get all columns larger than the xpos

    if not larger_cols:
        return len(colAlign) # Return the final column if xpos does not fit in any of the colAlign

    larger_cols.sort()
    colIndex = colAlign.index(larger_cols[0]) # Get the index of the first column that xpos is less than

    return colIndex
    