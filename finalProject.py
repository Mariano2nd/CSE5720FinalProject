import mysql.connector

conn = mysql.connector.connect(user = 'root',host = '127.0.0.1', password = 'Godinez680!', database = 'clothingstore')

#print(conn)

def insert_items(product_id,size,type,price):
    query = "INSERT INTO product(productid,size,type,price) VALUES(%s,%s,%s,%s);"
    dataqued = []
    args = (product_id,size,type,price)
    try:
        with conn.cursor() as cursor:

            cursor.execute(query,args)
            conn.commit()
            print('data committed')
            dataqued = cursor.execute("SELECT * FROM product;")
            print('test check:', dataqued)
        cursor.close()
    except:
        print("Could not insert")

    #conn.commit()
    
if __name__ == '__main__':
    insert_items('2','L','belt',10.00)
    conn.close()