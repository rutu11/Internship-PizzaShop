import tkinter as tk
from tkinter import *
import time
from datetime import datetime
from PIL import ImageTk, Image
from time import * 
import math
import pymysql        

#For maintaining COUNT
food_item ={'Margherita':0, 'Farm House': 0, 'Peppy Paneer': 0, 'Mexican Green Wave': 0, 'Cheese N Corn': 0, 'Veg Burger':0, 'Chessy dip':0, 'Drink':0, 'Veg Parcel':0 }

#Price of food_items
food_price_menu ={'Margherita':270, 'Farm House':180 , 'Peppy Paneer': 200, 'Mexican Green Wave': 299, 'Cheese N Corn': 290, 'Veg Burger':99, 'Chessy dip': 30, 'Drink':35, 'Veg Parcel':69}

#food_name and price
food_total ={'Margherita':0, 'Farm House':0 , 'Peppy Paneer': 0, 'Mexican Green Wave': 0, 'Cheese N Corn': 0, 'Veg Burger':0, 'Chessy dip': 0, 'Drink':0, 'Veg Parcel':0 }

#foodname and quantity
final_order_items = {}

def cal_total():
    total_bill = sum(food_total.values())
    total_count = sum(food_item.values())
    total_amount.delete('1.0', END)
    total_amount.insert(END,total_bill)
    print("totoal: ",total_bill,"cohnt: ",total_count)
    return total_bill, total_count

def incr_count(food_name):
    count = 0
    print(food_name)
    if food_name in food_item.keys():
        count = food_item[food_name]+1
        food_item[food_name] = count
        print("count: ",count)
    
    if(food_name == 'Margherita'):
        #Displaying Current total price
        food1_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food1_total.insert(END,current_food_price)#current_food_price)#270*food_item[food_name])
        food_total[food_name] = current_food_price
        print(food_total)
        print("-----")
        #food1_total.insert(END, food_price[food_name]*food_item[food_name])  #Total price of particular food
        
        #Displaying Food count
        food1_count.delete('1.0', END)
        food1_count.insert(END,count)
        
    elif(food_name == 'Farm House'):
        #Displaying Current total price
        food2_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food2_total.insert(END,current_food_price)#current_food_price)#270*food_item[food_name])
        food_total[food_name] = current_food_price
        
        food2_count.delete('1.0', END)
        food2_count.insert(END,count)
        
    elif(food_name == 'Peppy Paneer'):
        #Displaying Current total price
        food3_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food3_total.insert(END,current_food_price)
        food_total[food_name] = current_food_price
        
        food3_count.delete('1.0', END)
        food3_count.insert(END,count)    
        
    elif(food_name == 'Mexican Green Wave'):
        food4_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food4_total.insert(END,current_food_price)
        food_total[food_name] = current_food_price
        
        food4_count.delete('1.0', END)
        food4_count.insert(END,count)
        
    elif(food_name == 'Cheese N Corn'):
        food5_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food5_total.insert(END,current_food_price)
        food_total[food_name] = current_food_price
        
        food5_count.delete('1.0', END)
        food5_count.insert(END,count)
        
    elif(food_name == 'Veg Burger'):
        food6_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food6_total.insert(END,current_food_price)
        food_total[food_name] = current_food_price
        food6_count.delete('1.0', END)
        food6_count.insert(END,count)
        
    elif(food_name == 'Chessy dip'):
        food7_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food7_total.insert(END,current_food_price)
        food_total[food_name] = current_food_price
        food7_count.delete('1.0', END)
        food7_count.insert(END,count)
    
    elif(food_name == 'Drink'):
        food8_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food8_total.insert(END,current_food_price)
        food_total[food_name] = current_food_price
        food8_count.delete('1.0', END)
        food8_count.insert(END,count)
            
    elif(food_name == 'Veg Parcel'):
        food9_total.delete('1.0', END)
        current_food_price = food_price_menu[food_name]*food_item[food_name]
        food9_total.insert(END,current_food_price)
        food_total[food_name] = current_food_price
        food9_count.delete('1.0', END)
        food9_count.insert(END,count)
    print(food_item)
    
def dcr_count(food_name):
    if food_name in food_item.keys():
        count = food_item[food_name] - 1
        food_item[food_name] = count
        
    if(food_name == 'Margherita'):
        food1_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food1_total.insert(END,current_price) 
        #print(price)
        #food1_total.insert(END,float(price)/food_item[food_name])
        food1_count.delete('1.0', END)
        food1_count.insert(END,count)
        
    elif(food_name == 'Farm House'):
        food2_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food2_total.insert(END,current_price)
        
        food2_count.delete('1.0', END)
        food2_count.insert(END,count)
        
    elif(food_name == 'Peppy Paneer'):
        food3_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food3_total.insert(END,current_price)
        
        food3_count.delete('1.0', END)
        food3_count.insert(END,count)
        
    elif(food_name == 'Mexican Green Wave'):
        food4_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food4_total.insert(END,current_price)
        
        food4_count.delete('1.0', END)
        food4_count.insert(END,count)
        
    elif(food_name == 'Cheese N Corn'):
        food5_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food5_total.insert(END,current_price)
        
        food5_count.delete('1.0', END)
        food5_count.insert(END,count)
        
    elif(food_name == 'Veg Burger'):
        food6_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food6_total.insert(END,current_price)
        
        food6_count.delete('1.0', END)
        food6_count.insert(END,count)
        
    elif(food_name == 'Chessy dip'):
        food7_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food7_total.insert(END,current_price)
        
        food7_count.delete('1.0', END)
        food7_count.insert(END,count)
        
    elif(food_name == 'Drink'):
        food8_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food8_total.insert(END,current_price)
        
        food8_count.delete('1.0', END)
        food8_count.insert(END,count)
        
    elif(food_name == 'Veg Parcel'):
        food9_total.delete('1.0', END)
        current_price = food_total[food_name]-food_price_menu[food_name]
        food_total[food_name] = current_price
        food9_total.insert(END,current_price)
        
        food9_count.delete('1.0', END)
        food9_count.insert(END,count)
    
    print(food_item)

def billpage():

    details_of_customer = []
    def create_label(no):
        x_co = 0
        y_co = 0
        x_cut =0
        for i in range(no):
            for ordered_food_item, quantity in food_item.items():
                if(quantity != 0):
                    for food_name_ordered, total_price in food_total.items():
                        if(food_name_ordered == ordered_food_item):
                            
                            display_food_name = Label(child,text=ordered_food_item, font=('arial',12))
                            display_food_name.place(x=x_co+50, y=y_co+170)
                             
                            display_food_quantity = Label(child, text=quantity, font=('arial', 12))
                            display_food_quantity.place(x=x_co+295, y=y_co+170)
                            
                            display_total_foodprice = Label(child, text=total_price, font=('arial', 12,))
                            display_total_foodprice.place(x=x_co+425, y=y_co+170)
                            y_co = y_co+40
                            
                            final_order_items[ordered_food_item] = quantity
        print("final order: ",final_order_items)                    
        final_total_bill, final_total_count = cal_total()
        details_of_customer.append(int(final_total_bill))
        display_price.delete('1.0', END)
        display_price.insert(END, final_total_bill)
        display_quants.delete('1.0', END)
        display_quants.insert(END, final_total_count)
        
    db = pymysql.connect("localhost","root","","pizza_shop")
    cursor = db.cursor()    
    sql = "INSERT INTO customer_detail(name, contact,\
    total_bill) \
    VALUES ('%s', '%d', '%d')" % \
    (cust_name_text.get(), int(cust_contact_text.get()),sum(food_total.values()))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()   
            
    db.close()
    
    def close():
        root.destroy()
        child.destroy()
    
    child = Toplevel()
    child.geometry('500x650')
    child.configure(background='lavender')
    child.title('Pizza Shop Bill')
    
    
    customers_name = Label(child, text="Customer's Name: "+cust_name_text.get(), font=('arial',12))
    customers_name.place(x=20, y=90)
    
    customers_contact = Label(child, text="Customer's Contact No.: "+cust_contact_text.get(), font=('arial',12))
    customers_contact.place(x=20, y=116)
    
    image_icon = ImageTk.PhotoImage(Image.open("icon.png").resize((75,75)))
    shop_icon = Label(child, image=image_icon, background='lavender')
    shop_icon.place(x=145, y=5)
    
    shop_name = Label(child, text="MONDO PIZZA", font=('Rage Italic',20,'bold'), fg='purple4',background='lavender')
    shop_name.place(x=215, y=20)
    
    quantity = Label(child,text='QUANTITY', font=('arial',14,'bold'),fg='slate gray', background='lavender')
    quantity.place(x=250, y=140)
    
    display_total = Label(child,text='TOTAL', font=('arial',14,'bold'),fg='slate gray', background='lavender')
    display_total.place(x=402, y=140)
    
    total_bill = Label(child,text='TOTAL AMOUNT =', font=('arial',14,'bold'))
    total_bill.place(x=89, y=530)
    
    display_price = Text(child, width=7, height=2)
    display_price.place(x=409, y=530)
    
    display_quants = Text(child, width=7, height=2)
    display_quants.place(x=274, y=530)
    
    order_success = Label(child, text="Order Successfully!", font=('arial', 14, 'bold'), fg='Green')
    order_success.place(x=145, y=580)
    
    done = Button(child, text="DONE", font=('arial', 15,'bold'), command = close, bg='goldenrod')
    done.place(x=355, y=580)
    
    create_label(1)
    child.mainloop()    
    
def time(): 
    string = strftime('%H:%M:%S %p') 
    current_time.config(text = string) 
    current_time.after(1000, time)
    
root = Tk()
root.geometry('2000x2000')
root.configure(background='lavender')
root.title("PIZZA SHOP")

cust_name_text = StringVar()
cust_contact_text= IntVar()
    
customer_name = Label(root, text="Customer's Name: ", font=('arial',12),fg='slate gray', background='lavender')
customer_name.place(x=25, y=90)
    
cust_name_text = Entry(root, width=23, font=('arial', 12))
cust_name_text.place(x=165, y=94)
    
customer_contact = Label(root, text='Contact Number:', font=('arial',12),fg='slate gray', background='lavender')
customer_contact.place(x=25, y=116)
    
cust_contact_text = Entry(root, width=23, font=('arial', 12))
cust_contact_text.place(x=165, y=118)

image_icon = ImageTk.PhotoImage(Image.open("icon.png").resize((110,110)))
shop_icon = Label(root, image=image_icon, background='lavender')
shop_icon.place(x=475, y=5)

shop_name = Label(root, text="MONDO PIZZA", font=('Rage Italic',30,'bold'), fg='purple4',background='lavender')
#shop_name.pack()
shop_name.place(x=585, y=20)


current_time = Label(root,font=('Avant Garde', 15, 'bold'), fg='purple2', background='lavender')#,text=datetime.now().strftime("%H:%M:%S %p"))
current_time.place(x=635, y=95)
time()

piz_name = Label(root, text="MENU", font=('arial',13,'bold'),fg='slate gray', background='lavender')
piz_name.place(x=120,y=158)


quantity = Label(root, text="QUANTITY", font=('arial',13,'bold'),fg='slate gray', background='lavender')
quantity.place(x=245,y=158)


amount = Label(root, text="PRICE INR", font=('arial',13,'bold'),fg='slate gray', background='lavender')
amount.place(x=345,y=158)

ingredients = Label(root, text="INGREDIENTS", font=('arial',13,'bold'),fg='slate gray', background='lavender')
ingredients.place(x=560,y=158)


price_of_each = Label(root, text="BILL", font=('arial',13,'bold'),fg='slate gray', background='lavender')
price_of_each.place(x=825,y=158)

extra = Label(root, text="SIDES", font=('arial', 18,'bold'),fg='firebrick2', background='lavender')
extra.place(x=1055, y=145)


#FIRST PIZZA
img_piz1 = ImageTk.PhotoImage(Image.open("margherita.PNG").resize((65,65)))
food1 = Button(root,text = 'Margherita', font=('arial',11,'bold'), fg='navy',
               command= lambda: incr_count('Margherita'))
food1.config(image= img_piz1, width="175",height="65",activebackground="purple1",bg="light cyan", compound='left')
food1.place(x=40, y=190)

food1_count = Text(root, width=7, height=2)
food1_count.place(x=245, y=205)

food1_minus = Button(root, text="-", font=('arial',13,'bold'), 
                     command= lambda: dcr_count('Margherita'))
food1_minus.place(x=307, y=207)

food_price = Label(root, text="270 INR",font=('arial',13,'bold'), fg='gold4', bg='lavender')
food_price.place(x=353, y=210)

food_detail = Label(root,wraplength=350,justify=tk.LEFT,font=('arial',10),fg='gold4',bg='lavender',text="A hugely popular margherita, with a deliciously tangy single cheese topping")
food_detail.place(x=442, y=200)

food1_total = Text(root, width=7, height=2)
food1_total.place(x=815, y =200)


#SECOND PIZZA
img_piz2 = ImageTk.PhotoImage(Image.open("farm.PNG").resize((65,65)))
food2 = Button(root, wraplength=350,justify=tk.LEFT, text= 'Farm House',font=('arial',11,'bold'),fg='navy', 
               command=lambda: incr_count('Farm House'))
food2.config(image= img_piz2, width="175",height="65",activebackground="purple1",bg="light cyan", compound='left')
food2.place(x=40, y=280)

food2_count = Text(root, width=7, height=2)
food2_count.place(x=245, y=295)

food2_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Farm House'))
food2_minus.place(x=307,y=297)

food_price = Label(root, text="180 INR",font=('arial',12,'bold'), fg='red4', bg='lavender')
food_price.place(x=353, y=300)

food_detail = Label(root, wraplength=350,justify=tk.LEFT, fg='red4',bg='lavender',font=('arial',10),text="Check out this mouth watering overload of crunchy, crisp capsicum, succulent mushrooms and fresh tomatoes")
food_detail.place(x=442, y=290)

food2_total = Text(root, width=7, height=2)
food2_total.place(x=815, y =290)


#THIRD PIZZA
img_piz3 = ImageTk.PhotoImage(Image.open("peppy.PNG").resize((65,65)))
food3 = Button(root, text= 'Peppy Paneer',font=('arial',11,'bold'),fg='navy',
               command=lambda: incr_count('Peppy Paneer'))
food3.config(image= img_piz3, width="175",height="65",activebackground="purple1",bg="light cyan", compound='left')
food3.place(x=40, y=370)

food3_count = Text(root, width=7, height=2)
food3_count.place(x=245, y=385)

food3_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Peppy Paneer'))
food3_minus.place(x=307,y=387)

food_price = Label(root, text="200 INR",font=('arial',12,'bold'), fg='gold4', bg='lavender')
food_price.place(x=353, y=390)

food_detail = Label(root, wraplength=350,justify=tk.LEFT, fg='gold4',bg='lavender',font=('arial',10),text="Chunky paneer with crisp capsicum and spicy red pepper - quite a mouthful!")
food_detail.place(x=442, y=380)

food3_total = Text(root, width=7, height=2)
food3_total.place(x=815, y =380)


#FOURTH PIZZA
img_piz4 = ImageTk.PhotoImage(Image.open("mexi.PNG").resize((65,65)))
food4 = Button(root, text= 'Mexican Green',font=('arial',11,'bold'),fg='navy', 
               command= lambda: incr_count('Mexican Green Wave'))
food4.config(image= img_piz4, width="175",height="65",activebackground="purple1",bg="light cyan", compound='left')
food4.place(x=40, y=460)

food4_count = Text(root, width=7, height=2)
food4_count.place(x=245, y=475)

food4_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Mexican Green Wave'))
food4_minus.place(x=307,y=477)

food_price = Label(root, text="299 INR",font=('arial',12,'bold'), fg='red4', bg='lavender')
food_price.place(x=353, y=480)

food_detail = Label(root, wraplength=350,justify=tk.LEFT,fg='red4',bg='lavender', font=('arial',10),text="A pizza loaded with crunchy onions, crisp capsicum, juicy tomatoes and jalapeno with a liberal sprinkling of exotic Mexican herbs.")
food_detail.place(x=442, y=470)

food4_total = Text(root, width=7, height=2)
food4_total.place(x=815, y =470)


#FIFTH PIZZA
img_piz5 = ImageTk.PhotoImage(Image.open("cheese.PNG").resize((65,65)))
food5 = Button(root, text= 'Cheese N Corn',font=('arial',11,'bold'),fg='navy',
               command= lambda: incr_count('Cheese N Corn'))
food5.config(image= img_piz5, width="175",height="65",activebackground="purple1",bg="light cyan", compound='left')
food5.place(x=40, y=550)

food5_count = Text(root, width=7, height=2)
food5_count.place(x=245, y=565)

food5_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Cheese N Corn'))
food5_minus.place(x=307,y=567)

food_price = Label(root, text="290 INR",font=('arial',12,'bold'), fg='gold4', bg='lavender')
food_price.place(x=353, y=570)

food_detail = Label(root,wraplength=350,justify=tk.LEFT,fg='gold4',bg='lavender', font=('arial',10),text="Cheese I Golden Corn")
food_detail.place(x=442, y=560)

food5_total = Text(root, width=7, height=2)
food5_total.place(x=815, y =560)


#SIXTH PIZZA
img_piz6 = ImageTk.PhotoImage(Image.open("burger.PNG").resize((65,65)))
food6 = Button(root, text= 'Burger Pizza',font=('arial',11,'bold'),fg='navy',
               command= lambda: incr_count('Veg Burger'))
food6.config(image= img_piz6, width="175",height="65",activebackground="purple1",bg="light cyan", compound='left')
food6.place(x=40, y=640)

food6_count = Text(root, width=7, height=2)
food6_count.place(x=245, y=655)

food6_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Veg Burger'))
food6_minus.place(x=307,y=657)


food_price = Label(root, text="99 INR",font=('arial',12,'bold'), fg='red4', bg='lavender')
food_price.place(x=353, y=660)

food_detail = Label(root,wraplength=350,justify=tk.LEFT,fg='red4',bg='lavender', font=('arial',10),text="Crisp Capsicum l Tomato l Red Paprika l Paneer")
food_detail.place(x=442, y=650) 

food6_total = Text(root, width=7, height=2)
food6_total.place(x=815, y =650)

#SIDES 
#SEvENTH FOOD
img_piz7 = ImageTk.PhotoImage(Image.open("dip.PNG").resize((145,145)))     #, text= 'Chessy Dip',font=('arial',11,'bold'),
food7 = Button(root,
               command= lambda: incr_count('Chessy dip'))
food7.config(image= img_piz7, width="120",height="120",activebackground="purple1",bg="light cyan", compound='left')
food7.place(x=960, y=190)

food7_count = Text(root, width=5, height=2)
food7_count.place(x=1100, y=225)

food7_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Chessy dip'))
food7_minus.place(x=1145,y=227)

food_price = Label(root, text="30 INR",font=('arial',12,'bold'), fg='red4', bg='lavender')
food_price.place(x=1105, y=270)

food7_total = Text(root, width=7, height=2)
food7_total.place(x=1180, y =225)


#EIGHTH FOOD
img_piz8 = ImageTk.PhotoImage(Image.open("drink.PNG").resize((125,125)))     #, text= 'Chessy Dip',font=('arial',11,'bold'),
food8 = Button(root,
               command= lambda: incr_count('Drink'))
food8.config(image= img_piz8, width="120",height="120",activebackground="purple1",bg="light cyan", compound='left')
food8.place(x=960, y=330)

food8_count = Text(root, width=5, height=2)
food8_count.place(x=1100, y=365)

food8_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Drink'))
food8_minus.place(x=1145,y=367)

food_price = Label(root, text="35 INR",font=('arial',12,'bold'), fg='gold4', bg='lavender')
food_price.place(x=1105, y=410)

food8_total = Text(root, width=7, height=2)
food8_total.place(x=1180, y =365)


#NINETH FOOD
img_piz9 = ImageTk.PhotoImage(Image.open("parcel.PNG").resize((135,135)))     #, text= 'Chessy Dip',font=('arial',11,'bold'),
food9 = Button(root,
               command= lambda: incr_count('Veg Parcel'))
food9.config(image= img_piz9, width="120",height="120",activebackground="purple1",bg="light cyan", compound='left')
food9.place(x=960, y=470)

food9_count = Text(root, width=5, height=2)
food9_count.place(x=1100, y=505)

food9_minus = Button(root, text="-", font=('arial',13,'bold'),
                     command=lambda: dcr_count('Veg Parcel'))
food9_minus.place(x=1145,y=507)

food_price = Label(root, text="69 INR",font=('arial',12,'bold'), fg='red4', bg='lavender')
food_price.place(x=1105, y=550)

food9_total = Text(root, width=7, height=2)
food9_total.place(x=1180, y =505)


#TOTAL BILL
total = Button(root, text="TOTAL =", font=('arial', 15,'bold'),command = cal_total, bg='blue2', fg='white')
total.config(activebackground="purple1",bg="blue2", fg='white')
total.place(x=940,y=618)

total_amount = Text(root, width=7, height=2, bg='pale green')
total_amount.place(x=1050, y=620)

order = Button(root, text="ORDER", font=('arial',20,'bold'),
               command= billpage)
order.config(activebackground="purple1", bg="RoyalBlue1", fg="white")
order.place(x=1150, y=618)

mainloop()
