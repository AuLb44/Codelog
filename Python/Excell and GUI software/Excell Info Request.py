##### GNU TERRY PRATCHETT ####
##### Code by Andrew Albee #####




##### Packages and Libraries Imported ####
import PIL.Image
import PIL.ImageTk
from tkinter import *
import pandas as pd
import numpy as np




#### GUI Settings ####

## creates Initial prompt RequestTracker to enter infomatiomation as well as formatting of RequestTracker and image information ##
RequestTracker = Tk()
RequestTracker.title( 'Part Order Input' )
RequestTracker.geometry( '650x500' )
RequestTracker.configure( background = 'dark grey')
ProcStatement = Label( RequestTracker, text = 'Please enter in the Order information below', fg = 'black', font = ('Arial', 16), background = 'dark grey')
ProcStatement.grid( row = 0, column = 0, padx = 56, columnspan = 3  )
pic = ImageTk.PhotoImage( PIL.Image.open( r'[PLACEHOLDER FOR LOGO]' ))
logo = Label( RequestTracker, image = pic)
logo.grid( row = 3, column = 2, rowspan = 2, columnspan = 3 )
icon = ImageTk.PhotoImage( PIL.Image.open( r'[PLACEHOLDER FOR ICON]' ) )
RequestTracker.iconphoto(False, icon)


## Creates text box and input for delivery date ##
DeliveryDate = Label( RequestTracker, text = 'Date to be Delivered by:', fg = 'black', font = ('Arial', 10),background = 'dark grey' )
DeliveryDate.grid( row = 1, column = 0, padx = 12, pady = 4 )
DeliveryDate_input = Entry( RequestTracker, width = 25 )
DeliveryDate_input.grid( row = 1, column = 1 )


## Creates text box and input for Deliver To section ##
Delivery2 = Label( RequestTracker, text = 'Department being delivered to:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
Delivery2.grid( row = 2, column = 0, padx = 12, pady = 4 )
Delivery2_input = Entry( RequestTracker, width = 25 )
Delivery2_input.grid( row = 2, column = 1 )


## Creates text box and input for SKU ##
SKU = Label( RequestTracker, text = 'Part Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
SKU.grid( row = 3, column = 0, padx = 12, pady = 4 )
SKU_input = Entry( RequestTracker, width = 25 )
SKU_input.grid( row = 3, column = 1 )


## Creates text box and input for lot number ##
Lotnum = Label( RequestTracker, text = 'Lot Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
Lotnum.grid( row = 4, column = 0, padx = 12, pady = 4 )
Lotnum_input = Entry( RequestTracker, width = 25 )
Lotnum_input.grid( row = 4, column = 1 )


## Creates text box and input for Description Section ##
description = Label( RequestTracker, text = 'Product Description:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
description.grid( row = 5, column = 0, padx = 12, pady = 4 )
description_input = Entry( RequestTracker, width = 25 )
description_input.grid( row = 5, column = 1 )


## Creates text box and input for Pallet Number ##
Palletnum = Label( RequestTracker, text = 'Thermo Fisher Pallet Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
Palletnum.grid( row = 6, column = 0, padx = 12, pady = 4 )
Palletnum_input = Entry( RequestTracker, width = 25 )
Palletnum_input.grid( row = 6, column = 1 )


## Creates text box and input for QTY data ##
QTY = Label( RequestTracker, text = 'Quantity', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
QTY.grid( row = 7, column = 0, padx = 12, pady = 4 )
QTY_input = Entry( RequestTracker, width = 25 )
QTY_input.grid( row = 7, column = 1 )


## Creates text box and input for Number of Load##
loadnumber = Label( RequestTracker, text = 'Load Number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
loadnumber.grid( row = 8, column = 0, padx = 12, pady = 4 )
loadnumber_input = Entry( RequestTracker, width = 25 )
loadnumber_input.grid( row = 8, column = 1 )


## Creates text box and input for delivery department ##
tobedeliveredby = Label( RequestTracker, text = 'Department to be delivered by:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
tobedeliveredby.grid( row = 9, column = 0, padx = 12, pady = 4 )
tobedeliveredby_input = Entry( RequestTracker, width = 25 )
tobedeliveredby_input.grid( row = 9, column = 1 )


## Creates text box and input for ##
transferrespons = Label( RequestTracker, text = 'Transfer Responsibility:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
transferrespons.grid( row = 10, column = 0, padx = 12 )
transferrespons_input = Entry( RequestTracker, width = 25 )
transferrespons_input.grid( row = 10, column = 1 )


## Creates text box and input for EOL data ##
EOL = Label( RequestTracker, text = 'End of lot number:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
EOL.grid( row = 11, column = 0, padx = 12, pady = 4 )
EOL_input = Entry( RequestTracker, width = 25 )
EOL_input.grid( row = 11, column = 1 )


## Creates text box and input for Location on Truck ##
locontruck = Label( RequestTracker, text = 'Location on Truck:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
locontruck.grid( row = 12, column = 0, padx = 12, pady = 4 )
locontruck_input = Entry( RequestTracker, width = 25 )
locontruck_input.grid( row = 12, column = 1 )


## Creates text box and input for  Ordered by section##
orderedby = Label( RequestTracker, text = 'Ordered By:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
orderedby.grid( row = 13, column = 0, padx = 12, pady = 4 )
orderedby_input = Entry( RequestTracker, width = 25 )
orderedby_input.grid( row = 13, column = 1 )


## Creates text box and input for Department needed section ##
deptneeded = Label( RequestTracker, text = 'Department Needed:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
deptneeded.grid( row = 14, column = 0, padx = 12, pady = 4 )
deptneeded_input = Entry( RequestTracker, width = 25 )
deptneeded_input.grid( row = 14, column = 1 )


## Creates text box and input for Add on order status##
addonorderstatus = Label( RequestTracker, text = 'Is this an Add-On order:', fg = 'black', font = ('Arial', 10), background = 'dark grey' )
addonorderstatus.grid( row = 15, column = 0, padx = 12, pady = 4 )
addonorderstatus_input = Entry( RequestTracker, width = 25 )
addonorderstatus_input.grid( row = 15, column = 1 )




#### Previous Data Importation Section ####

## Imports documents into python from file directory ## 
Tracker= pd.DataFrame( pd.read_excel(r'[PLACEHOLDER FOR OUTPUT]', usecols = "B:P", na_filter=False ) )
CallBack= pd.DataFrame( pd.read_excel(r'[PLACEHOLDER FOR REFERENCE]', usecols = "B:P", na_filter=False ) )

## tester dataframe to capture format of excel
## Tester = pd.DataFrame( pd.read_excel(r'C:/Users/andrew.albee/OneDrive - Thermo Fisher Scientific/Documents/CMT/tester.xlsx', usecols = "A:O", na_filter=False ) )


 

#### Function for taking input data and either adding to excel or giving error ####

def push_me():
  
  ## Gets each textbox input and assigns it to a specified variable ##
  pn =  Palletnum_input.get() 
  ln = Lotnum_input.get()
  sku = SKU_input.get()
  dd = DeliveryDate_input.get()
  qty = QTY_input.get()
  eol = EOL_input.get()
  d2 = Delivery2_input.get()
  desc = description_input.get()
  tloc = locontruck_input.get()
  lnum = loadnumber_input.get()
  ob = orderedby_input.get()
  dn = deptneeded_input.get()
  tbdb = tobedeliveredby_input.get()
  addon = addonorderstatus_input.get()
  tresp = transferrespons_input.get()
  
  
  ## combines input items into a data frame for combinations
  Order = pd.DataFrame( { 'Date To be Delivered' : dd, 
                                'Deliver To' : d2,
                                'Part Number' : sku,
                                'Lot Number' : ln,
                                'Description' : desc,
                                'Thermo pallet number' : pn,
                                'QTY' : qty,
                                'EOL' : eol,
                                'Location On Truck' : tloc,
                                'Load' : lnum,
                                'Ordered By' : ob,
                                'Dept. Needed' : dn,
                                'To Be Delivered By' : tbdb,
                                'Add On Order Status' : addon,
                                'Transfer Responsibility' : tresp
                        }, index = [len(CallBack.index)])
  
  ## Combines order with previous call back documentation ##
  CompiledCallBack = pd.concat( [CallBack, Order]  )
  
  
  
  
  #### Unique Value Verification section ####
  
  ## conditional statement to check if the value given for pallet number is unique or if present on callback
  if pn in CallBack.values:
    
    ## creates error RequestTracker on condition that pn requeted already present in callback 
    error = Tk()
    error.title( ' ' )
    error.geometry( '210x145' )
    ErrorStatement = Label( error, text = 'Error duplicate pallet number present', fg = 'Red', font = ('Arial', 14), wraplength = 200, justify = 'center')
    ErrorStatement.grid( row = 0, column = 0  )
    errorclarify = Label( error, text = 'pallet number requested either already on callback or presnt on site, please verify', fg = 'red', font = ('Arial', 8),  wraplength = 200, justify = 'center')
    errorclarify.grid( row = 1, column = 0, padx = 12, pady = 4 )


    ## close button for error message ##
    def close_error():
      error.destroy()
      return 
    closeerror = Button( error, text='Close', command=close_error)
    closeerror.grid( row = 2, column = 0)
    
    error.mainloop()
  
  
  elif pn not in Tracker.values:
    ## creates error RequestTracker on condition that pn requeted does not exist in Tracker
    badpallet = Tk()
    badpallet.title( ' ' )
    badpallet.geometry( '200x145' )
    ErrorStatement = Label( badpallet, text = 'No Pallet with Requested ID', fg = 'Red', font = ('Arial', 14), wraplength = 200, justify = 'center')
    ErrorStatement.grid( row = 0, column = 0  )
    errorclarify = Label( badpallet, text = 'pallet number requested not listed in Thermo Fisher record. Please verify pallet number', fg = 'red', font = ('Arial', 8),  wraplength = 200, justify = 'center')
    errorclarify.grid( row = 1, column = 0, padx = 12, pady = 4 )



    ## close button for error message ##
    def close_error():
      badpallet.destroy()
      return
    closeerror = Button( badpallet, text='Close', command=close_error)
    closeerror.grid( row = 2, column = 0)

    badpallet.mainloop()
  
  
  ## Condition where everything is good to go  
  else:
    
    ## writes information to call back order
    CompiledCallBack.to_excel( r'[PLACEHOLDER FOR REFERENCE]' )
    
    ## takes tracker excel and removes value from tracker that has been orderd by checking pallet number. Then writes it back to excel
    CompiledTracker = pd.concat( [Tracker, Order]  )
    RemovedOrder = CompiledTracker.drop_duplicates( 'Thermo pallet number', keep=False )
    RemovedOrder.to_excel( r'[PLACEHOLDER FOR OUTPUT]' )
    
    # closess the main RequestTracker
    RequestTracker.destroy()
  return 




#### Function for close button ####

def close_me():
  ## this is the command that says to destory the main RequestTracker
  RequestTracker.destroy()
  return 




#### GUI Button Creation and Placement ####

## Confirm button creation and placement
confirmbutton = Button( RequestTracker , text='Submit', command=push_me )
confirmbutton.grid( row = 15, column = 2, pady = 4)

## Close button Creation and Placement ##
closebutton = Button( RequestTracker, text='Close', command=close_me)
closebutton.grid( row = 15, column = 4, sticky = W, padx = 40, pady = 4)



## Keeps RequestTracker open until program ends ##
RequestTracker.mainloop()
