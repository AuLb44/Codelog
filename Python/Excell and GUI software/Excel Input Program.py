##### GNU TERRY PRATCHETT ####
##### Code by Andrew Albee #####




##### Packages and Libraries Imported ####
from tkinter import * 
import pandas as pd




#### GUI Settings ####

## creates Initial prompt TrackerInput to enter infomatiomation as well as formatting of TrackerInput and image information ##
TrackerInput = Tk()
TrackerInput.title( 'Thermo Fisher Transfer Input' )
TrackerInput.geometry( '650x350' )
TrackerInput.configure( background = 'dark grey')
ProcStatement = Label( TrackerInput, text = 'Please enter information below', fg = 'black', font = ('Arial', 16), background = 'dark grey')
ProcStatement.grid( row = 0, column = 0, padx = 56, columnspan = 3  )
pic = ImageTk.PhotoImage( PIL.Image.open( r'[PLACEHOLDER FOR LOGO]' ))
logo = Label( TrackerInput, image = pic)
logo.grid( row = 3, column = 2, rowspan = 2, columnspan = 3, padx = 20 )
icon = ImageTk.PhotoImage( PIL.Image.open( r'[PLACEHOLDER FOR ICON]' ) )
TrackerInput.iconphoto(False, icon)


## Creates text box and input for delivery date ##
DeliveryDate = Label( TrackerInput, text = 'Date to be Delivered by:', fg = 'black', font = ('Arial', 10),background = 'dark grey' )
DeliveryDate.grid( row = 1, column = 0, padx = 12, pady = 4 )
DeliveryDate_input = Entry( TrackerInput, width = 25 )
DeliveryDate_input.grid( row = 1, column = 1 )


## Creates text box and input for Deliver To section ##
Delivery2 = Label( TrackerInput, text = 'Department being delivered to:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
Delivery2.grid( row = 2, column = 0, padx = 12, pady = 4 )
Delivery2_input = Entry( TrackerInput, width = 25 )
Delivery2_input.grid( row = 2, column = 1 )


## Creates text box and input for SKU ##
SKU = Label( TrackerInput, text = 'Part Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
SKU.grid( row = 3, column = 0, padx = 12, pady = 4 )
SKU_input = Entry( TrackerInput, width = 25 )
SKU_input.grid( row = 3, column = 1 )


## Creates text box and input for lot number ##
Lotnum = Label( TrackerInput, text = 'Lot Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
Lotnum.grid( row = 4, column = 0, padx = 12, pady = 4 )
Lotnum_input = Entry( TrackerInput, width = 25 )
Lotnum_input.grid( row = 4, column = 1 )


## Creates text box and input for Description Section ##
description = Label( TrackerInput, text = 'Product Description:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
description.grid( row = 5, column = 0, padx = 12, pady = 4 )
description_input = Entry( TrackerInput, width = 25 )
description_input.grid( row = 5, column = 1 )


## Creates text box and input for Pallet Number ##
Palletnum = Label( TrackerInput, text = 'Thermo Fisher Pallet Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
Palletnum.grid( row = 6, column = 0, padx = 12, pady = 4 )
Palletnum_input = Entry( TrackerInput, width = 25 )
Palletnum_input.grid( row = 6, column = 1 )


## Creates text box and input for QTY data ##
QTY = Label( TrackerInput, text = 'Quantity', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
QTY.grid( row = 7, column = 0, padx = 12, pady = 4 )
QTY_input = Entry( TrackerInput, width = 25 )
QTY_input.grid( row = 7, column = 1 )


## Creates text box and input for Number of Load##
loadnumber = Label( TrackerInput, text = 'Load Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
loadnumber.grid( row = 8, column = 0, padx = 12, pady = 4 )
loadnumber_input = Entry( TrackerInput, width = 25 )
loadnumber_input.grid( row = 8, column = 1 )


## Creates text box and input for delivery department ##
tobedeliveredby = Label( TrackerInput, text = 'Department to be delivered by:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
tobedeliveredby.grid( row = 9, column = 0, padx = 12, pady = 4 )
tobedeliveredby_input = Entry( TrackerInput, width = 25 )
tobedeliveredby_input.grid( row = 9, column = 1 )


## Creates text box and input for ##
transferrespons = Label( TrackerInput, text = 'Transfer Responsibility:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
transferrespons.grid( row = 10, column = 0, padx = 12 )
transferrespons_input = Entry( TrackerInput, width = 25 )
transferrespons_input.grid( row = 10, column = 1 )




#### Previous Data Importation Section ####

## Imports documents into python from file directory ## 
Tracker= pd.DataFrame( pd.read_excel(r'[PLACEHOLDER FOR OUTPUT EXCEL]', usecols = "B:P", na_filter=False ) )





#### Function for taking input data and either adding to excel or giving error ####

def push_me():
  
  ## Gets each textbox input and assigns it to a specified variable ##
  pn =  Palletnum_input.get() 
  ln = Lotnum_input.get()
  sku = SKU_input.get()
  dd = DeliveryDate_input.get()
  qty = QTY_input.get()
  d2 = Delivery2_input.get()
  desc = description_input.get()
  lnum = loadnumber_input.get()
  tbdb = tobedeliveredby_input.get()
  tresp = transferrespons_input.get()
  
  
  ## combines input items into a data frame for combinations ##
  TFSinput = pd.DataFrame( { 'Date To be Delivered' : dd, 
                                'Deliver To' : d2,
                                'Part Number' : sku,
                                'Lot Number' : ln,
                                'Description' : desc,
                                'Thermo pallet number' : pn,
                                'QTY' : qty,
                                'Load' : lnum,
                                'To Be Delivered By' : tbdb,
                                'Transfer Responsibility' : tresp
                        }, index = [len(Tracker.index)])
  
  ## Combines order with previous call back documentation ##
  CompiledTracker = pd.concat( [Tracker, TFSinput]  )
  
  ## writes information to call back order ##
  CompiledTracker.to_excel( r'[PLACEHOLDER FOR OUTPUT EXCEL]' )


  return  TrackerInput.destroy()




#### Function for close button ####

def close_me():
  TrackerInput.destroy()
  return 




#### GUI Button Creation and Placement ####

## Confirm button creation and placement
confirmbutton = Button( TrackerInput , text='Submit', command=push_me )
confirmbutton.grid( row = 10, column = 3, pady = 4)

## Close button Creation and Placement ##
closebutton = Button( TrackerInput, text='Close', command=close_me)
closebutton.grid( row = 10, column = 4, sticky = W, padx = 40, pady = 4)



## Keeps TrackerInput open until program ends ##
TrackerInput.mainloop()
